import dash
from dash import Dash, _dash_renderer
import dash_mantine_components as dmc

import callbacks
from data import init_cache

from constants import HOST
from constants import PORT
from constants import DEBUG

_dash_renderer._set_react_version('18.2.0')

app = Dash(__name__, external_stylesheets=dmc.styles.ALL, use_pages=True, update_title=None, suppress_callback_exceptions=True)
server = app.server

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
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

app.layout = dmc.MantineProvider(
    forceColorScheme="light",
    theme={
        "primaryColor": "indigo",
        "fontFamily": "Roboto, sans-serif",
        "components": {
            "Button": {"defaultProps": {"fw": 400}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
            "Badge": {"styles": {"root": {"fontWeight": 500}}},
            "Progress": {"styles": {"label": {"fontWeight": 500}}},
            "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
            "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
            "Table": {
                "defaultProps": {
                    "highlightOnHover": True,
                    "withTableBorder": True,
                    "verticalSpacing": "sm",
                    "horizontalSpacing": "md",
                }
            },
        },
    },
    children=[dash.page_container]
)

init_cache(app)

callbacks.init_callbacks(app)

if __name__ == '__main__':
    app.run_server(
        debug=DEBUG,
        host=HOST,
        port=PORT
    )