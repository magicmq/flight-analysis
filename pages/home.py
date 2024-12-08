import dash
from dash import html, dcc
import dash_mantine_components as dmc
import dash_new_tab as dnt

from components.appshell import construct_appshell
from components.flightmodal import construct_flight_modal

dash.register_page(__name__, title='Flight Analysis', path='/')

layout = html.Div([
    construct_appshell(),
    dmc.NotificationProvider(position='bottom-left'),
    construct_flight_modal(),
    html.Div(id='notifications-container'),
    dcc.Download(id='download-data'),
    dcc.Store(id='group-by-state'),
    dnt.NewTab(id='new-tab-handler', n_opens=0)
])