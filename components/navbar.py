import dash_mantine_components as dmc
from dash_iconify import DashIconify

from components.flightcard import construct_flight_card

from columns import get_x_axis_columns, get_y_axis_columns, get_color_columns

def construct_graph_settings(loc):
    return dmc.Stack([
        dmc.Flex(
            [
                dmc.Select(
                    id={'location': loc, 'selector': 'graph-type-selector'},
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
                dmc.Popover(
                    [
                        dmc.PopoverTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.PopoverDropdown(
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
                    trapFocus=False,
                    shadow='md',
                    closeOnClickOutside=True
                ),
            ],
            gap='xs',
            align='center',
            justify='flex-start'
        ),
        dmc.Flex(
            [
                dmc.Select(
                    id={'location': loc, 'selector': 'x-axis-selector'},
                    label='X-Axis Variable',
                    data=get_x_axis_columns(),
                    value='date',
                    w=200
                ),
                dmc.Popover(
                    [
                        dmc.PopoverTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.PopoverDropdown(
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
                    trapFocus=False,
                    shadow='md',
                    closeOnClickOutside=True
                ),
            ],
            gap='xs',
            align='center',
            justify='flex-start'
        ),
        dmc.Flex(
            [
                dmc.MultiSelect(
                    id={'location': loc, 'selector': 'y-axis-selector'},
                    label='Y-Axis Variables',
                    data=[
                        {
                            'group': 'General',
                            'items': get_y_axis_columns('general')
                        },                        
                        {
                            'group': 'Totals',
                            'items': get_y_axis_columns('total')
                        },
                        {
                            'group': 'Polaris',
                            'items': get_y_axis_columns('polaris')
                        },
                        {
                            'group': 'Premium Plus',
                            'items': get_y_axis_columns('premium_plus')
                        },
                        {
                            'group': 'Economy',
                            'items': get_y_axis_columns('economy')
                        },
                        {
                            'group': 'Standby',
                            'items': get_y_axis_columns('standby')
                        }
                    ],
                    value=['av_to', 'pos_pe']
                ),
                dmc.Popover(
                    [
                        dmc.PopoverTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.PopoverDropdown(
                            dmc.Stack([
                                dmc.Divider(label=[dmc.Title('Y-Axis Variables', size='lg', order=4, c='black')], labelPosition='left', color='black'),
                                dmc.Text('Variables to be represented on the y-axis. May select multiple variables in order to show multiple traces/series on the same graph.')
                            ], gap='xs'))
                    ],
                    width=400,
                    position='bottom',
                    withArrow=True,
                    trapFocus=False,
                    shadow='md',
                    closeOnClickOutside=True
                ),
            ],
            gap='xs',
            align='center',
            justify='flex-start',
            wrap='nowrap'
        ),
        dmc.Flex(
            [
                dmc.Select(
                    id={'location': loc, 'selector': 'color-selector'},
                    label='Color',
                    data=[
                        {
                            'group': 'General',
                            'items': get_color_columns('general')
                        },                        
                        {
                            'group': 'Totals',
                            'items': get_color_columns('total')
                        },
                        {
                            'group': 'Polaris',
                            'items': get_color_columns('polaris')
                        },
                        {
                            'group': 'Premium Plus',
                            'items': get_color_columns('premium_plus')
                        },
                        {
                            'group': 'Economy',
                            'items': get_color_columns('economy')
                        },
                        {
                            'group': 'Standby',
                            'items': get_color_columns('standby')
                        }
                    ],
                    value=[],
                    w=300
                ),
                dmc.Popover(
                    [
                        dmc.PopoverTarget(
                            dmc.ActionIcon(
                                DashIconify(icon='material-symbols:info-outline', width=20),
                                size='lg',
                                variant='transparent',
                                color='gray',
                                mt=25
                            )
                        ),
                        dmc.PopoverDropdown(
                            dmc.Stack([
                                dmc.Divider(label=[dmc.Title('Color', size='lg', order=4, c='black')], labelPosition='left', color='black'),
                                dmc.Text('(Optional) Applies a color to each data point (or bar) on the graphs according to the selected value.')
                            ], gap='xs'))
                    ],
                    width=400,
                    position='bottom',
                    withArrow=True,
                    trapFocus=False,
                    shadow='md',
                    closeOnClickOutside=True
                ),
            ],
            gap='xs',
            align='center',
            justify='flex-start',
            wrap='nowrap'
        )
    ], mx=10)

def construct_navbar_content(loc):
    to_return = [
        dmc.Divider(label=[dmc.Text('Data Grouping', size='xl', c='black')], labelPosition='left', color='black'),

        dmc.SegmentedControl(
            id={'location': loc, 'selector': 'group-by-selector'},
            data=[
                {'label': 'Route/Flight Number', 'value': 'route'},
                {'label': 'Day of Week', 'value': 'day_of_week_name'}
            ],
            value='route',
            mx=10,
            mb=3
        ),

        dmc.Divider(label=[dmc.Text('Graph Settings', size='xl', c='black')], labelPosition='left', color='black'),

        construct_graph_settings(loc)
    ]

    if loc == 'navbar':
        to_return.append(dmc.Divider(label=[dmc.Text('Selected Flight', size='xl', c='black')], labelPosition='left', color='black')),
        to_return.append(construct_flight_card())

    return to_return

def construct_navbar():
    return dmc.AppShellNavbar(
        dmc.ScrollArea(
            construct_navbar_content('navbar'),
            offsetScrollbars=True,
            type='scroll',
            style={"height": "100%"}
        ),
        p=10
    )

def construct_navbar_drawer():
    return dmc.Drawer(
        construct_navbar_content('drawer'),
        id='navbar-drawer',
        size=350,
        trapFocus=False
    )