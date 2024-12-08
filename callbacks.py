from dash import dcc, Output, Input, State, ALL, set_props, callback_context, no_update
import dash_mantine_components as dmc

from data import get_data, get_data_as
from graphs import get_graphs
from components.misc import construct_error, construct_graph_container

from columns import get_label
from constants import COMPATIBLE_VARIABLES, FLIGHT_PAGE_URL, SCREENSHOT_URL

def init_callbacks(app):
    @app.callback(
        Output('group-by-state', 'data'),
        Output('graphs-accordion-container', 'children'),
        Output('graphs-accordion-container', 'value'),
        Input({'location': ALL, 'selector': 'group-by-selector'}, 'value'),
        State('navbar-drawer', 'opened')
    )
    def update_accordion_items(selected_group_all, navbar_opened):
        index = 1 if navbar_opened else 0
        selected_group = selected_group_all[index]

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
        Input({'location': ALL, 'selector': 'graph-type-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'x-axis-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'y-axis-selector'}, 'value'),
        Input({'location': ALL, 'selector': 'color-selector'}, 'value'),
        State('navbar-drawer', 'opened')
    )
    def update_graphs(group_by, graph_type_all, x_axis_all, y_axes_all, color_all, navbar_opened):
        index = 1 if navbar_opened else 0
        graph_type = graph_type_all[index]
        x_axis = x_axis_all[index]
        y_axes = y_axes_all[index]
        color = color_all[index]

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
        Input({'location': ALL, 'selector': 'graph-type-selector'}, 'value'),
        State('navbar-drawer', 'opened'),
        prevent_initial_call=True
    )
    def display_hovered_flight(hover_data, graph_type_all, navbar_opened):
        index = 1 if navbar_opened else 0
        graph_type = graph_type_all[index]

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
        State({'location': ALL, 'selector': 'graph-type-selector'}, 'value'),
        State('navbar-drawer', 'opened'),
        prevent_initial_call=True
    )
    def open_clicked_flight(n_opens, clicked_data, graph_type_all, navbar_opened):
        index = 1 if navbar_opened else 0
        graph_type = graph_type_all[index]

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