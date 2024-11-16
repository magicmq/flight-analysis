from dash import dcc, Output, Input, ALL, set_props, callback_context, no_update
import dash_mantine_components as dmc

from data import get_data, get_data_as
from graphs import get_graphs
from components.misc import construct_error
from components.misc import construct_no_flight

from constants import COMPATIBLE_VARIABLES
from constants import FLAT_COLUMN_LABELS
from constants import SCREENSHOT_URL

def init_callbacks(app):
    @app.callback(
        Output('group-by-state', 'data'),
        Output('graphs-accordion-container', 'children'),
        Output('graphs-accordion-container', 'value'),
        Input('group-by-selector', 'value')
    )
    def update_accordion_items(selected_group):
        unique_items = get_data()[selected_group].unique()

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

        return get_graphs(group_by, graph_type, x_axis, y_axes)
    
    @app.callback(
        Output('selected-flight', 'children'),
        Input({'graph-group': ALL}, 'hoverData'),
        Input('graph-type-selector', 'value'),
        prevent_initial_call=True
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
                x_axis = f'{FLAT_COLUMN_LABELS[customdata[2]]}: {point["x"]}'
                screenshot_url = SCREENSHOT_URL.format(hash=customdata[1])

                return dmc.Card([
                    dmc.Title(f'{header_text}', order=4),
                    dmc.Text(f'{x_axis}'),
                    dmc.Image(src=screenshot_url, alt='Standby list not found')
                ], withBorder=True)

        return construct_no_flight()
    
    @app.callback(
        Output('download-data', 'data'),
        Input('download-csv', 'n_clicks'),
        Input('download-excel', 'n_clicks'),
        Input('download-json', 'n_clicks'),
        prevent_initial_call=True
    )
    def download_data(n_clicks_csv, n_clicks_excel, n_clicks_json):
        triggered_id = callback_context.triggered_id
        if triggered_id == 'download-csv':
            return dcc.send_data_frame(get_data_as('csv'), 'data.csv')
        elif triggered_id == 'download-excel':
            return dcc.send_data_frame(get_data_as('excel'), 'data.xlsx', sheet_name='Sheet1')
        elif triggered_id == 'download-json':
            return dcc.send_data_frame(get_data_as('json'), 'data.json')