import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

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
                                dmc.Flex(
                                    html.A(
                                        dmc.Button(
                                            'Home',
                                            leftSection=DashIconify(icon='mdi:home'),
                                            variant='outline'
                                        ),
                                        href='/'
                                    ),
                                    justify='flex-end'
                                ),
                                span='auto'
                            )
                        ],
                        justify='space-between',
                        align='center'
                    )
                ],
                justify='center',
                h=60
            )
        ],
        px=20
    )