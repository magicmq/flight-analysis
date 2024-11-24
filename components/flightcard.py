import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

def construct_flight_card():
    return dmc.Card(
        [
            dmc.Title(id='selected-flight-navbar-title', order=4),
            dmc.Text(id='selected-flight-navbar-text'),
            dmc.Box(id='selected-flight-navbar-img'),
            dmc.Group(
                html.A(
                    dmc.Button(
                        'Open In New Tab',
                        leftSection=DashIconify(icon='gg:external'),
                        variant='outline',
                    ),
                    id='selected-flight-navbar-external',
                    target='_blank',
                    style={'display': 'none'}
                ),
                justify='flex-end',
                mt=10
            )
        ],
        withBorder=True,
        visibleFrom='lg'
    )