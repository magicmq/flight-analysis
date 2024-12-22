import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import dcc

def construct_header(name):
    return dmc.AppShellHeader(
        children=[
            dmc.Stack(
                children=[
                    dmc.Grid(
                        children=[
                            dmc.GridCol(
                                dmc.Title(name, order=1),
                                span='content'
                            ),
                            dmc.GridCol(
                                dmc.Flex(
                                    dcc.Link(
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