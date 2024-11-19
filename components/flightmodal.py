import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html, clientside_callback, Output, Input, State

def construct_flight_modal():
    return html.Div([
        dmc.Affix(
            dmc.Button(
                'SA List for Selected Flight',
                leftSection=DashIconify(icon='mdi:airplane'),
                id='selected-flight-modal-open',
                style={'boxShadow': '-2px 4px 6px rgba(0, 0, 0, 0.3)'}
            ),
            position={'bottom': 20, 'right': 20},
            hiddenFrom='lg'
        ),
        dmc.Modal(
            dmc.Stack(
                [
                    dmc.Box(id='selected-flight-modal-content'),
                    dmc.Group(
                        [
                            html.A(
                                dmc.Button(
                                    'Open In New Tab',
                                    leftSection=DashIconify(icon='gg:external'),
                                    variant='outline',
                                ),
                                id='selected-flight-modal-external',
                                target='_blank'
                            ),
                            dmc.Button(
                                'Close',
                                leftSection=DashIconify(icon='mdi:close'),
                                color='red',
                                variant='outline',
                                id="selected-flight-modal-close",
                            ),
                        ],
                        justify='flex-end',
                        gap='md'
                    )
                ],
                gap='md'
            ),
            id='selected-flight-modal'
        )
    ])

clientside_callback(
    """function(n_clicks_1, n_clicks_2, opened) { return !opened }""",
    Output('selected-flight-modal', 'opened'),
    Input('selected-flight-modal-open', 'n_clicks'),
    Input('selected-flight-modal-close', 'n_clicks'),
    State('selected-flight-modal', 'opened'),
    prevent_initial_call=True
)