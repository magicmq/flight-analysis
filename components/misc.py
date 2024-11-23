from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

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

def construct_graph_container(id):
    return dmc.ScrollArea(
        [
            html.Div(
                [
                    dcc.Graph(
                        id=id,
                        config={'responsive': False}
                    )
                ],
                style={'width': '100%', 'min-width': '1100px'},
            )
        ],
        type='auto'
    )