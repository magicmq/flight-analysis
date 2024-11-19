from components.header import construct_header
from components.navbar import construct_navbar, construct_navbar_drawer
from components.main import construct_main

import dash_mantine_components as dmc

def construct_appshell():
    return dmc.AppShell(
        children = [
            construct_header(),
            construct_navbar(),
            construct_navbar_drawer(),
            construct_main()
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
    )