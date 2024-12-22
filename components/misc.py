from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd

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

def construct_group_summary(group, grouped_data):
    if group == 'route':
        return construct_group_summary_route(grouped_data)
    else:
        return construct_group_summary_dow(grouped_data)

def construct_group_summary_route(grouped_data):
    date_range = pd.date_range(start=grouped_data['date'].min(), end=grouped_data['date'].max())
    missing_dates = date_range.difference(grouped_data['date'])
    day_of_week_counts = grouped_data['day_of_week'].value_counts()

    return [
        dmc.Text([dmc.Text('Total Data Points Collected:', fw=500, span=True), f' {len(grouped_data)}'], mb=10),
        dmc.SimpleGrid(
            [
                dmc.Card(
                    [
                        dmc.Title('By Date', order=4),
                        dmc.Text([dmc.Text('Available Dates:', fw=500, span=True), f' {grouped_data['date'].dt.strftime('%m/%d/%Y').tolist()}']),
                        dmc.Text([dmc.Text('Number of Missing Dates:', fw=500, span=True), f' {len(missing_dates)}']),
                        dmc.Text([dmc.Text('Missing Dates:', fw=500, span=True), f' {missing_dates.strftime('%m/%d/%Y').tolist()}'])
                    ],
                    withBorder=True
                ),
                dmc.Card(
                    [
                        dmc.Title('By Day of Week', order=4),
                        dmc.Text([dmc.Text('Available Data Points for Monday:', fw=500, span=True), f' {day_of_week_counts.get(0, 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for Tuesday:', fw=500, span=True), f' {day_of_week_counts.get(1, 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for Wednesday:', fw=500, span=True), f' {day_of_week_counts.get(2, 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for Thursday:', fw=500, span=True), f' {day_of_week_counts.get(3, 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for Friday:', fw=500, span=True), f' {day_of_week_counts.get(4, 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for Saturday:', fw=500, span=True), f' {day_of_week_counts.get(5, 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for Sunday:', fw=500, span=True), f' {day_of_week_counts.get(6, 0)}'])
                    ],
                    withBorder=True
                ),
            ],
            cols={'base': 1, 'md': 2, 'lg': 3},
            spacing='md',
            verticalSpacing='md'
        )
    ]

def construct_group_summary_dow(grouped_data):
    date_range = pd.date_range(start=grouped_data['date'].min(), end=grouped_data['date'].max())
    missing_dates = date_range.difference(grouped_data['date'])
    flight_no_counts = grouped_data['flight_no'].value_counts()

    print(flight_no_counts)

    return [
        dmc.Text([dmc.Text('Total Data Points Collected:', fw=500, span=True), f' {len(grouped_data)}'], mb=10),
        dmc.SimpleGrid(
            [
                dmc.Card(
                    [
                        dmc.Title('By Date*', order=4),
                        dmc.Text([dmc.Text('Available Dates:', fw=500, span=True), f' {grouped_data['date'].dt.strftime('%m/%d/%Y').tolist()}']),
                        dmc.Text([dmc.Text('Number of Missing Dates:', fw=500, span=True), f' {len(missing_dates)}']),
                        dmc.Text([dmc.Text('Missing Dates:', fw=500, span=True), f' {missing_dates.strftime('%m/%d/%Y').tolist()}'], mb=5),
                        dmc.Text('* Includes all flight numbers, so duplicate dates are possible.', fs='italic')
                    ],
                    withBorder=True
                ),
                dmc.Card(
                    [
                        dmc.Title('By Flight Number', order=4),
                        dmc.Text([dmc.Text('Available Data Points for UAL7:', fw=500, span=True), f' {flight_no_counts.get('7', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL143:', fw=500, span=True), f' {flight_no_counts.get('143', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL32:', fw=500, span=True), f' {flight_no_counts.get('32', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL39:', fw=500, span=True), f' {flight_no_counts.get('39', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL837:', fw=500, span=True), f' {flight_no_counts.get('837', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL875:', fw=500, span=True), f' {flight_no_counts.get('875', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL881:', fw=500, span=True), f' {flight_no_counts.get('881', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL803:', fw=500, span=True), f' {flight_no_counts.get('803', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL131:', fw=500, span=True), f' {flight_no_counts.get('131', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL79:', fw=500, span=True), f' {flight_no_counts.get('79', 0)}']),
                        dmc.Text([dmc.Text('Available Data Points for UAL35:', fw=500, span=True), f' {flight_no_counts.get('35', 0)}'])
                    ],
                    withBorder=True
                ),
            ],
            cols={'base': 1, 'md': 2, 'lg': 3},
            spacing='md',
            verticalSpacing='md'
        )
    ]