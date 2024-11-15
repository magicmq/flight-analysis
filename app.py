import sqlite3
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, ALL, _dash_renderer, no_update, set_props, callback_context
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import calendar

from constants import COLUMN_LABELS
from constants import FLAT_COLUMN_LABELS
from constants import COMPATIBLE_VARIABLES

SCREENSHOT_URL='https://magicmq.dev/flight-analysis/pass-list-screenshots/{hash}.png'

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

left_table = 'data'
right_table = 'data_post'
join_column = 'hash'

cursor.execute(f'PRAGMA table_info({left_table})')
left_columns = [col[1] for col in cursor.fetchall()]

cursor.execute(f'PRAGMA table_info({right_table})')
right_columns = [col[1] for col in cursor.fetchall()]

unique_right_columns = [col for col in right_columns if col not in left_columns and col != join_column]

left_columns_str = ", ".join([f'{left_table}.{col}' for col in left_columns])
right_columns_str = ", ".join([f'{right_table}.{col}' for col in unique_right_columns])

query = f"""
    SELECT {left_columns_str}, {right_columns_str}
    FROM {left_table}
    JOIN {right_table} ON {left_table}.{join_column} = {right_table}.{join_column}
"""

data = pd.read_sql_query(query, connection)
connection.close()

data['flight_no'] = data['flight_no'].str.lstrip('0')

data['date'] = pd.to_datetime(data['date'])

data['route'] = data.apply(lambda row: f'UAL{row["flight_no"]} ({row["origin"]}-{row["destination"]})', axis=1)

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
data['day_of_week_name'] = data['day_of_week'].map({i: day for i, day in enumerate(calendar.day_name)})
data['day_of_week_name'] = pd.Categorical(data['day_of_week_name'], categories=day_order, ordered=True)

data['p_av_bu'] = data['p_ca_bu'] - data['p_bo_bu'] - data['p_ps_bu'] - data['p_he_bu'] - data['p_re_bu']
data['p_av_co'] = data['p_ca_co'] - data['p_bo_co'] - data['p_ps_co'] - data['p_he_co'] - data['p_re_co']
data['p_av_pp'] = data['p_ca_pp'] - data['p_bo_pp'] - data['p_ps_pp'] - data['p_he_pp'] - data['p_re_pp']
data['p_av_to'] = data['p_ca_to'] - data['p_bo_to'] - data['p_ps_to'] - data['p_he_to'] - data['p_re_to']

data['net_pos_va'] = data['av_to'] - data['pos_va']
data['net_pos_pe'] = data['av_to'] - data['pos_pe']

total_columns = [{'label': value, 'value': key} for key, value in COLUMN_LABELS['total'].items()]
polaris_columns = [{'label': value, 'value': key} for key, value in COLUMN_LABELS['polaris'].items()]
pp_columns = [{'label': value, 'value': key} for key, value in COLUMN_LABELS['premium_plus'].items()]
economy_columns = [{'label': value, 'value': key} for key, value in COLUMN_LABELS['economy'].items()]
standby_columns = [{'label': value, 'value': key} for key, value in COLUMN_LABELS['standby'].items()]

columns = total_columns + polaris_columns + pp_columns + economy_columns + standby_columns

def construct_graph_settings():
    return dmc.Stack([
        dmc.Flex(
            [
                dmc.Select(
                    id='graph-type-selector',
                    label='Graph Type',
                    data=[
                        {'label': 'Time Series', 'value': 'time_series'},
                        {'label': 'Scatter Plot', 'value': 'scatter'},
                        {'label': 'Bar Graph', 'value': 'bar'},
                        {'label': 'Bar Graph (Mean Values)', 'value': 'bar_means'}
                    ],
                    value='time_series',
                    w=200
                ),
                dmc.HoverCard(
                    [
                        dmc.HoverCardTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.HoverCardDropdown(
                            dmc.Stack([
                                dmc.Divider(label=[dmc.Title('Graph Type', size='lg', order=4, c='black')], labelPosition='left', color='black'),
                                dmc.Text([dmc.Text('Time Series: ', fw=700, span=True), 'A scatter plot with time (date) on the x-axis, and lines connecting each point.']),
                                dmc.Text([dmc.Text('Scatter Plot: ', fw=700, span=True), 'A graph consisting of points.']),
                                dmc.Text([dmc.Text('Bar Graph: ', fw=700, span=True), 'A graph consisting of vertical bars. Each bar corresponds to an x-axis value and the height of each bar corresponds to the y-axis value.']),
                                dmc.Text([dmc.Text('Bar Graph (Mean Values): ', fw=700, span=True), 'A bar graph, except that the y-axis is the average of all available data points for each x-axis group.']),
                            ], gap='xs')
                        )
                    ],
                    width=400,
                    position='bottom',
                    withArrow=True,
                    shadow='md',
                    closeOnClickOutside=True
                ),
            ],
            align='center',
            justify='space-between'
        ),
        dmc.Flex(
            [
                dmc.Select(
                    id='x-axis-selector',
                    label='X-Axis Variable',
                    data=[
                        {'label': 'Date', 'value': 'date'},
                        {'label': 'Flight Number', 'value': 'flight_no'},
                        {'label': 'Day Of Week', 'value': 'day_of_week_name'}
                    ],
                    value='date',
                    w=200
                ),
                dmc.HoverCard(
                    [
                        dmc.HoverCardTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.HoverCardDropdown(
                            dmc.Stack([
                                dmc.Divider(label=[dmc.Title('X-Axis Variable', size='lg', order=4, c='black')], labelPosition='left', color='black'),
                                dmc.Text([dmc.Text('Date: ', fw=700, span=True), 'Arrange the data on the x-axis according to the date of the flight.']),
                                dmc.Text([dmc.Text('Flight Number: ', fw=700, span=True), 'Arrange the data on the x-axis according to the flight number of the flight.']),
                                dmc.Text([dmc.Text('Day of Week: ', fw=700, span=True), 'Arrange the data on the x-axis according to the day of the week. ', dmc.Text('NOTE:', fw=500, span=True), ' This x-axis value is only allowed when \'Data Grouping\' is set to \'Route/Flight Number\' and \'Graph Type\' is set to \'Bar Graph (Mean Values)\'.'])
                            ], gap='xs')
                        )
                    ],
                    width=400,
                    position='bottom',
                    withArrow=True,
                    shadow='md',
                    closeOnClickOutside=True
                ),
            ],
            align='center',
            justify='space-between'
        ),
        dmc.Flex(
            [
                dmc.MultiSelect(
                    id='y-axis-selector',
                    label='Y-Axis Variables',
                    data=columns,
                    value=['av_to', 'pos_pe'],
                    w=425
                ),
                dmc.HoverCard(
                    [
                        dmc.HoverCardTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.HoverCardDropdown(
                            dmc.Stack([
                                dmc.Divider(label=[dmc.Title('Y-Axis Variables', size='lg', order=4, c='black')], labelPosition='left', color='black'),
                                dmc.Text('Variables to be represented on the y-axis. May select multiple variables in order to show multiple traces/series on the same graph.')
                            ], gap='xs'))
                    ],
                    width=400,
                    position='bottom',
                    withArrow=True,
                    shadow='md'
                ),
            ],
            align='center',
            justify='space-between'
        ),
    ], mx=10)

def construct_header():
    return dmc.AppShellHeader(
        children=[
            dmc.Stack(
                children=[
                    dmc.Grid(
                        children=[
                            dmc.GridCol(
                                dmc.Title('Flight Data Analysis', order=1),
                                span='content'
                            ),
                            dmc.GridCol(
                                dmc.Group(
                                    [
                                        html.A(
                                            dmc.Tooltip(
                                                dmc.ActionIcon(
                                                    DashIconify(icon='material-symbols:download-sharp', width=25),
                                                    variant='transparent',
                                                    size='xl',
                                                    color='gray'
                                                ),
                                                label='Download Raw Data',
                                                position='top'
                                            ),
                                            href='TODO',
                                            target="_blank",
                                            rel='noopener noreferrer'
                                        ),
                                        html.A(
                                            dmc.Tooltip(
                                                dmc.ActionIcon(
                                                    DashIconify(icon='mdi:github', width=25),
                                                    variant='transparent',
                                                    size='lg',
                                                    color='gray'
                                                ),
                                                label='View Source Code',
                                                position='top'
                                            ),
                                            href='https://github.com',
                                            target="_blank",
                                            rel='noopener noreferrer'
                                        ),
                                    ],
                                    justify='flex-end',
                                    gap='sm'
                                ),
                                span='auto'
                            )
                        ],
                        justify='space-between'
                    )
                ],
                justify='center',
                h=60
            )
        ],
        px=20
    )

def construct_navbar():
    return dmc.AppShellNavbar([
        dmc.Divider(label=[dmc.Text('Data Grouping', size='xl', c='black')], labelPosition='left', color='black'),

        dmc.SegmentedControl(
            id='group-by-selector',
            data=[
                {'label': 'Route/Flight Number', 'value': 'route'},
                {'label': 'Day of Week', 'value': 'day_of_week_name'}
            ],
            value='route',
            mx=10,
            mb=3
        ),

        dmc.Divider(label=[dmc.Text('Graph Settings', size='xl', c='black')], labelPosition='left', color='black'),

        construct_graph_settings(),

        dmc.Divider(label=[dmc.Text('Selected Flight', size='xl', c='black')], labelPosition='left', color='black'),

        html.Div(id='selected-flight'),

        dmc.Divider(my=5)
    ], p=10)

def construct_main():
    return dmc.AppShellMain([
        dmc.Accordion(
            children=[],
            id='graphs-accordion-container',
            multiple=True,
            variant='separated'
        ),

        dcc.Store(id='group-by-state')
    ])

_dash_renderer._set_react_version('18.2.0')
external_stylesheets=[
    'https://unpkg.com/@mantine/dates@7.13.4/styles.css',
    'https://unpkg.com/@mantine/code-highlight@7.13.4/styles.css',
    'https://unpkg.com/@mantine/charts@7.13.4/styles.css',
    'https://unpkg.com/@mantine/carousel@7.13.4/styles.css',
    'https://unpkg.com/@mantine/notifications@7.13.4/styles.css',
    'https://unpkg.com/@mantine/nprogress@7.13.4/styles.css'
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = dmc.MantineProvider(
    forceColorScheme="light",
    theme={
        "primaryColor": "indigo",
        "fontFamily": "Roboto, sans-serif",
        "components": {
            "Button": {"defaultProps": {"fw": 400}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
            "Badge": {"styles": {"root": {"fontWeight": 500}}},
            "Progress": {"styles": {"label": {"fontWeight": 500}}},
            "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
            "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
            "Table": {
                "defaultProps": {
                    "highlightOnHover": True,
                    "withTableBorder": True,
                    "verticalSpacing": "sm",
                    "horizontalSpacing": "md",
                }
            },
        },
    },
    children=[
        dmc.AppShell(
            children = [
                construct_header(),
                construct_navbar(),
                construct_main(),
            ],
            header={
                'height': 60,
            },
            navbar={
                'width': 520,
                'breakpoint': 'lg',
                'collapsed': {'mobile': True}
            },
            padding='xl'
        ),
        dmc.NotificationProvider(position='bottom-left'),
        html.Div(id='notifications-container')
    ],
)

def construct_scatter(grouped_data, group_column, x_axis, y_axes, mode='markers'):
    fig = go.Figure()

    customdata = grouped_data[[group_column, 'hash']].values
    x_axis_static = np.full((len(grouped_data), 1), x_axis)
    customdata = np.concatenate([customdata, x_axis_static], axis=1)

    for y_axis in y_axes:
        fig.add_trace(go.Scatter(
            x=grouped_data[x_axis],
            y=grouped_data[y_axis],
            mode=mode,
            name=f'{FLAT_COLUMN_LABELS[y_axis]}',
            hovertemplate=(
                '%{customdata[0]}<br>' +
                f'{FLAT_COLUMN_LABELS[x_axis]}: '  + '%{x}<br>' +
                'Count: %{y}'
            ),
            customdata=customdata
        ))

    fig.update_layout(
        title=", ".join([FLAT_COLUMN_LABELS[y_axis] for y_axis in y_axes]),
        xaxis_title=FLAT_COLUMN_LABELS[x_axis],
        yaxis_title='Count',
        height=600
    )

    return fig

def construct_time_series(grouped_data, group_column, x_axis, y_axes):
    return construct_scatter(grouped_data, group_column, x_axis, y_axes, mode='lines+markers')

def construct_bar(grouped_data, group_column, x_axis, y_axes):
    fig = go.Figure()

    customdata = grouped_data[[group_column, 'hash']].values
    x_axis_static = np.full((len(grouped_data), 1), x_axis)
    customdata = np.concatenate([customdata, x_axis_static], axis=1)

    for y_axis in y_axes:
        fig.add_trace(go.Bar(
            x=grouped_data[x_axis],
            y=grouped_data[y_axis],
            text=grouped_data[y_axis],
            textposition='auto',
            name=f'{FLAT_COLUMN_LABELS[y_axis]}',
            hovertemplate=(
                '%{customdata[0]}<br>' +
                'Count: %{y}'
            ),
            customdata=customdata
        ))

    fig.update_layout(
        title=", ".join([FLAT_COLUMN_LABELS[y_axis] for y_axis in y_axes]),
        xaxis_title=f'{FLAT_COLUMN_LABELS[x_axis]}',
        yaxis_title='Count'
    )

    return fig

def construct_bar_means(grouped_data, x_axis, y_axes):
    mean_data = grouped_data.groupby([x_axis], observed=False)[y_axes].mean().reset_index()

    fig = go.Figure()

    for y_axis in y_axes:
        fig.add_trace(go.Bar(
            x=mean_data[x_axis],
            y=mean_data[y_axis],
            text=mean_data[y_axis],
            textposition='auto',
            name=f'Mean of {FLAT_COLUMN_LABELS[y_axis]}',
            hovertemplate=(
                f'{FLAT_COLUMN_LABELS[x_axis]}: ' + '%{x}<br>' +
                'Mean: %{y}'
            ),
        ))

    fig.update_layout(
        title=", ".join([f'Mean of {FLAT_COLUMN_LABELS[y_axis]}' for y_axis in y_axes]),
        xaxis_title=f'{FLAT_COLUMN_LABELS[x_axis]}',
        yaxis_title='Mean'
    )

    return fig

def no_flight_selected():
    return dmc.Card([
        dmc.Title(f'No flight selected.', order=4),
        dmc.Text(f'Hover over a data point to view the standby list for that flight.')
    ], withBorder=True)

def construct_error(id, title, message):
    return dmc.Notification(
        id=id,
        title=title,
        message=message,
        color='red',
        icon=DashIconify(icon='material-symbols:error'),
        action='show',
        autoClose=10000
    )

@app.callback(
    Output('group-by-state', 'data'),
    Output('graphs-accordion-container', 'children'),
    Output('graphs-accordion-container', 'value'),
    Input('group-by-selector', 'value')
)
def update_accordion_items(selected_group):
    unique_items = data[selected_group].unique()

    accordion_items = []
    active_items = []
    for item in unique_items:
        item_id = item.lower().replace(' ', '_')
        accordion_items.append(
            dmc.AccordionItem([
                    dmc.AccordionControl(dmc.Title(item, order=4)),
                    dmc.AccordionPanel(dcc.Graph(
                        id={'graph-group': item},
                        clear_on_unhover=True
                    )),
                ],
                value=item_id
            )
        )
        active_items.append(item_id)
    
    return selected_group, accordion_items, active_items

@app.callback(
    Output({'graph-group': ALL}, 'figure'),
    Input('group-by-state', 'data'),
    Input('graph-type-selector', 'value'),
    Input('x-axis-selector', 'value'),
    Input('y-axis-selector', 'value')
)
def update_graphs(group_by, graph_type, x_axis, y_axes):
    if not COMPATIBLE_VARIABLES[group_by][graph_type][x_axis]:
        set_props('notifications-container', {'children': construct_error(
            id=f'error-{group_by}-{graph_type}-{x_axis}-{y_axes}',
            title='Incompatible Variables',
            message='The selected variables are incompatible. Please select different variables.'
        )})

        return [no_update] * len(callback_context.outputs_list)

    figs = []
    
    for group in data[group_by].unique():
        grouped_data = data[data[group_by] == group]

        fig = None
        if graph_type == 'time_series':
            fig = construct_time_series(grouped_data, group_by, x_axis, y_axes)
        elif graph_type == 'scatter':
            fig = construct_scatter(grouped_data, group_by, x_axis, y_axes)
        elif graph_type == 'bar':
            fig = construct_bar(grouped_data, group_by, x_axis, y_axes)
        elif graph_type == 'bar_means':
            fig = construct_bar_means(grouped_data, x_axis, y_axes)

        if fig is None:
            fig = go.Figure()

        fig['layout']['uirevision'] = True

        figs.append(fig)

    return figs

@app.callback(
    Output('selected-flight', 'children'),
    Input({'graph-group': ALL}, 'hoverData'),
    Input('graph-type-selector', 'value'),
    prevent_initial_call=True,
)
def display_selected_flight(hover_data, graph_type):
    if graph_type == 'bar_means':
        return dmc.Card([
            dmc.Title(f'Disabled', order=4),
            dmc.Text(f'Cannot view standby listings when showing mean values.')
        ], withBorder=True)

    for points in hover_data:
        if points is not None:
            point = points['points'][0]
            try:
                customdata = point['customdata']
            except KeyError:
                return no_update

            header_text = customdata[0]
            x_axis = f'{FLAT_COLUMN_LABELS[customdata[2]]}: {point['x']}'
            screenshot_url = SCREENSHOT_URL.format(hash=customdata[1])

            return dmc.Card([
                dmc.Title(f'{header_text}', order=4),
                dmc.Text(f'{x_axis}'),
                dmc.Image(src=screenshot_url, alt='Standby list not found')
            ], withBorder=True)

    return no_flight_selected()

app.run(debug=True)