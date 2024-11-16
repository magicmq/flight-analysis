from dash import Dash, _dash_renderer
import dash_mantine_components as dmc

from layout import get_layout
import callbacks
from data import init_cache

from constants import HOST
from constants import PORT
from constants import DEBUG

_dash_renderer._set_react_version('18.2.0')

app = Dash(__name__, external_stylesheets=dmc.styles.ALL, suppress_callback_exceptions=True)
server = app.server

init_cache(app)

app.layout = get_layout()

callbacks.init_callbacks(app)

if __name__ == '__main__':
    app.run_server(
        debug=True if DEBUG == 'True' else False,
        host=HOST,
        port=PORT
    )