from components.appshell import construct_appshell
from components.flightmodal import construct_flight_modal

import dash_mantine_components as dmc
from dash import dcc, html

def get_layout():
    return dmc.MantineProvider(
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
            construct_appshell(),
            dmc.NotificationProvider(position='bottom-left'),
            construct_flight_modal(),
            html.Div(id='notifications-container'),
            dcc.Download(id='download-data'),
            dcc.Store(id='group-by-state')
        ],
    )