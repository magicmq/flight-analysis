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

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Flight Data Analysis</title>
        {%favicon%}
        {%css%}
        <link rel="icon" type="image/png" href="/assets/favicon-96x96.png" sizes="96x96" />
        <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />
        <link rel="shortcut icon" href="/assets/favicon.ico" />
        <link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png" />
        <meta name="apple-mobile-web-app-title" content="Flight Analysis" />
        <link rel="manifest" href="/assets/site.webmanifest" />
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

app.layout = get_layout()

init_cache(app)

callbacks.init_callbacks(app)

if __name__ == '__main__':
    app.run_server(
        debug=DEBUG,
        host=HOST,
        port=PORT
    )