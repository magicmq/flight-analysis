from dash import Dash, _dash_renderer
import dash_mantine_components as dmc

from layout import get_layout
import callbacks
from data import init_cache

_dash_renderer._set_react_version('18.2.0')

app = Dash(__name__, external_stylesheets=dmc.styles.ALL, suppress_callback_exceptions=True)

init_cache(app)

app.layout = get_layout()

callbacks.init_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)