from dash import dcc, Output, Input, State, ALL, set_props, callback_context, no_update
import dash_mantine_components as dmc

from data import get_data, get_data_as
from graphs import get_graphs
from components.misc import construct_error, construct_graph_container, construct_group_summary

from columns import get_label
from constants import COMPATIBLE_VARIABLES, FLIGHT_PAGE_URL, SCREENSHOT_URL

def init_callbacks(app):
    @app.callback(
        Output('group-by-store', 'data'),
        Output('graph-type-store', 'data'),
        Output('x-axis-store', 'data'),
        Output('y-axis-store', 'data'),
        Output('color-store', 'data'),
        State('group-by-store', 'data'),
        State('graph-type-store', 'data'),
        State('x-axis-store', 'data'),
        State('y-axis-store', 'data'),
        State('color-store', 'data'),
        Input({'location': ALL, 'selector': 'group-by-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'graph-type-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'x-axis-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'y-axis-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'color-selector'}, 'value'),
        prevent_initial_call=True
    )
    def set_input_stores_navbar(group_by_current, graph_type_current, x_axis_current, y_axes_current, color_current, *args):
        args_grouping = callback_context.args_grouping
        inputs_only = [item for item in args_grouping if isinstance(item, list)]
        triggered_item = next(d for group in inputs_only for d in group if d['triggered'])
        selector = triggered_item['id']['selector']
        value = triggered_item['value']

        if selector == 'group-by-selector':
            if group_by_current != value:
                return value, no_update, no_update, no_update, no_update
        elif selector == 'graph-type-selector':
            if graph_type_current != value:
                return no_update, value, no_update, no_update, no_update
        elif selector == 'x-axis-selector':
            if x_axis_current != value:
                return no_update, no_update, value, no_update, no_update
        elif selector == 'y-axis-selector':
            if y_axes_current != value:
                return no_update, no_update, no_update, value, no_update
        else:
            if color_current != value:
                return no_update, no_update, no_update, no_update, value
        
        return no_update, no_update, no_update, no_update, no_update
    
    @app.callback(
        Output({'location': ALL, 'selector': 'group-by-selector'}, 'value'),
        Output({'location': ALL, 'selector': 'graph-type-selector'}, 'value'),
        Output({'location': ALL, 'selector': 'x-axis-selector'}, 'value'),
        Output({'location': ALL, 'selector': 'y-axis-selector'}, 'value'),
        Output({'location': ALL, 'selector': 'color-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'group-by-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'graph-type-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'x-axis-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'y-axis-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'color-selector'}, 'value'),
        prevent_initial_call=True
    )
    def sync_inputs(*args):
        args_grouping = callback_context.args_grouping
        triggered_item = next(d for group in args_grouping for d in group if d['triggered'])
        triggered_loc = triggered_item['id']['location']
        selector = triggered_item['id']['selector']
        value = triggered_item['value']

        if triggered_loc == 'drawer':
            if selector == 'group-by-selector':
                return [value, no_update], [no_update, no_update], [no_update, no_update], [no_update, no_update], [no_update, no_update]
            elif selector == 'graph-type-selector':
                return [no_update, no_update], [value, no_update], [no_update, no_update], [no_update, no_update], [no_update, no_update]
            elif selector == 'x-axis-selector':
                return [no_update, no_update], [no_update, no_update], [value, no_update], [no_update, no_update], [no_update, no_update]
            elif selector == 'y-axis-selector':
                return [no_update, no_update], [no_update, no_update], [no_update, no_update], [value, no_update], [no_update, no_update]
            else:
                return [no_update, no_update], [no_update, no_update], [no_update, no_update], [no_update, no_update], [value, no_update]
        else:
            if selector == 'group-by-selector':
                return [no_update, value], [no_update, no_update], [no_update, no_update], [no_update, no_update], [no_update, no_update]
            elif selector == 'graph-type-selector':
                return [no_update, no_update], [no_update, value], [no_update, no_update], [no_update, no_update], [no_update, no_update]
            elif selector == 'x-axis-selector':
                return [no_update, no_update], [no_update, no_update], [no_update, value], [no_update, no_update], [no_update, no_update]
            elif selector == 'y-axis-selector':
                return [no_update, no_update], [no_update, no_update], [no_update, no_update], [no_update, value], [no_update, no_update]
            else:
                return [no_update, no_update], [no_update, no_update], [no_update, no_update], [no_update, no_update], [no_update, value]

    @app.callback(
        Output('group-by-state', 'data'),
        Output('graphs-accordion-container', 'children'),
        Output('graphs-accordion-container', 'value'),
        Input('group-by-store', 'data')
    )
    def update_accordion_items(selected_group):
        unique_items = get_data()[selected_group].cat.categories

        accordion_items = []
        active_items = []
        for item in unique_items:
            item_id = item.lower().replace(' ', '_')
            accordion_items.append(
                dmc.AccordionItem([
                        dmc.AccordionControl(dmc.Title(item, order=4)),
                        dmc.AccordionPanel(construct_graph_container({'graph-group': item})),
                    ],
                    value=item_id
                )
            )
            active_items.append(item_id)
        
        return selected_group, accordion_items, active_items
    
    @app.callback(
        Output({'graph-group': ALL}, 'figure'),
        Input('group-by-state', 'data'),
        Input('graph-type-store', 'data'),
        Input('x-axis-store', 'data'),
        Input('y-axis-store', 'data'),
        Input('color-store', 'data')
    )
    def update_graphs(group_by, graph_type, x_axis, y_axes, color):
        if not COMPATIBLE_VARIABLES[group_by][graph_type][x_axis]:
            set_props('notifications-container', {'children': construct_error(
                id=f'error-{group_by}-{graph_type}-{x_axis}-{y_axes}',
                title='Incompatible Variables',
                message='The selected variables are incompatible. Please select different variables.'
            )})

            return [no_update] * len(callback_context.outputs_list)

        return get_graphs(group_by, graph_type, x_axis, y_axes, color)
    
    @app.callback(
        Output('selected-flight-navbar-title', 'children'),
        Output('selected-flight-navbar-text', 'children'),
        Output('selected-flight-navbar-img', 'children'),
        Output('selected-flight-navbar-external', 'href'),
        Output('selected-flight-navbar-external', 'style'),
        Output({'graph-group': ALL}, 'hoverData'),
        Input({'graph-group': ALL}, 'hoverData'),
        Input('graph-type-store', 'data'),
        prevent_initial_call=True
    )
    def display_hovered_flight(hover_data, graph_type):
        if graph_type == 'bar_means' or graph_type == 'box':
            return (
                'Disabled',
                'Cannot view standby listings with this graph type selected.',
                None,
                '/',
                {'display': 'none'},
                [None for _ in range(len(hover_data))]
            )

        for points in hover_data:
            if points is not None:
                point = points['points'][0]
                try:
                    customdata = point['customdata']
                except KeyError:
                    return [no_update] * len(callback_context.outputs_list)

                header_text = customdata[0]
                flight_hash = customdata[1]
                x_axis_label = f'{get_label(customdata[2])}: '
                x_axis_value = point["x"]
                flight_page_url = FLIGHT_PAGE_URL.format(hash=flight_hash)
                screenshot_url = SCREENSHOT_URL.format(hash=flight_hash)

                return (
                    header_text,
                    [dmc.Text(x_axis_label, fw=500, span=True), x_axis_value],
                    dmc.Image(src=screenshot_url, alt='Standby list not found for this flight.'),
                    flight_page_url,
                    {'display': 'block'},
                    [None for _ in range(len(hover_data))]
                )

        return (
            'No flight selected.',
            'Hover over a data point to view the standby list for that flight.',
            None,
            '/',
            {'display': 'none'},
            [None for _ in range(len(hover_data))]
        )
    
    @app.callback(
        Output('new-tab-handler', 'href'),
        Output('new-tab-handler', 'n_opens'),
        Output({'graph-group': ALL}, 'clickData'),
        Input('new-tab-handler', 'n_opens'),
        Input({'graph-group': ALL}, 'clickData'),
        State('graph-type-store', 'data'),
        prevent_initial_call=True
    )
    def open_clicked_flight(n_opens, clicked_data, graph_type):
        if graph_type == 'bar_means' or graph_type == 'box':
            return no_update, no_update, [None for _ in clicked_data]

        for points in clicked_data:
            if points is not None:
                point = points['points'][0]
                try:
                    customdata = point['customdata']
                except KeyError:
                    return [no_update] * len(callback_context.outputs_list)

                flight_hash = customdata[1]
                flight_page_url = FLIGHT_PAGE_URL.format(hash=flight_hash)

                return (
                    flight_page_url,
                    n_opens + 1,
                    [None for _ in clicked_data]
                )

        return no_update, no_update, [None for _ in clicked_data]

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
        
    @app.callback(
        Output('group-by-summary-state', 'data'),
        Output('group-by-summary-container', 'children'),
        Output('group-by-summary-container', 'value'),
        Input('group-by-summary-selector', 'value')
    )
    def update_data_summary(selected_group):
        unique_items = get_data()[selected_group].cat.categories

        accordion_items = []
        active_items = []
        for item in unique_items:
            item_id = item.lower().replace(' ', '_')
            accordion_items.append(
                dmc.AccordionItem([
                        dmc.AccordionControl(dmc.Title(item, order=4)),
                        dmc.AccordionPanel(dmc.Box(id={'group-summary': item})),
                    ],
                    value=item_id
                )
            )
            active_items.append(item_id)
        
        return selected_group, accordion_items, active_items
    
    @app.callback(
        Output({'group-summary': ALL}, 'children'),
        Input('group-by-summary-state', 'data'),
    )
    def update_data_summary_containers(group):
        containers = []

        grouped_data = get_data().groupby(group, observed=False)

        for _, grouped_data in grouped_data:
            containers.append(construct_group_summary(group, grouped_data))

        return containers