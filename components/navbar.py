import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from constants import ALL_COLUMNS

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
                    data=ALL_COLUMNS,
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