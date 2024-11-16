import dash_mantine_components as dmc

def construct_main():
    return dmc.AppShellMain([
        dmc.Accordion(
            children=[],
            id='graphs-accordion-container',
            multiple=True,
            variant='separated'
        ),
    ])