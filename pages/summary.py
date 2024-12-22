import dash
from dash import html, dcc
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from components.genericheader import construct_header
from data import get_data

dash.register_page(__name__, title='Data Summary', path='/summary')

def construct_total_summary():
    data = get_data()
    return dmc.Box(children=[
        dmc.Divider(label=[dmc.Text('Total Data Summary', size='xl', c='black')], labelPosition='left', color='black'),
        dmc.Text([dmc.Text('Total Data Points:', fw=500, span=True), f' {len(data)}'])
    ])

def construct_grouping_summary():
    return dmc.Box(children=[
        dmc.Divider(label=[dmc.Text('Data Grouping', size='xl', c='black')], labelPosition='left', color='black'),

        dmc.SegmentedControl(
            id='group-by-summary-selector',
            data=[
                {'label': 'Route/Flight Number', 'value': 'route'},
                {'label': 'Day of Week', 'value': 'day_of_week_name'}
            ],
            value='route',
            mb=10
        ),

        dmc.Accordion(
            children=[],
            id='group-by-summary-container',
            multiple=True,
            variant='separated'
        ),
    ])

def construct_main():
    return dmc.AppShellMain(
        dmc.Box(children=[
            construct_total_summary(),
            construct_grouping_summary()
        ])
    )

def layout(**kwargs):
    return html.Div([
        dmc.AppShell(
            children = [
                construct_header('Data Summary'),
                construct_main()
            ],
            header={
                'height': 60,
            },
            padding='md'
        ),
        dcc.Store(id='group-by-summary-state')
    ])