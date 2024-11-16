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

def construct_no_flight():
    return dmc.Card([
        dmc.Title(f'No flight selected.', order=4),
        dmc.Text(f'Hover over a data point to view the standby list for that flight.')
    ], withBorder=True)