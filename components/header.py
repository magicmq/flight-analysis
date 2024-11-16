import dash_mantine_components as dmc
from dash_iconify import DashIconify

def construct_header():
    return dmc.AppShellHeader(
        children=[
            dmc.Stack(
                children=[
                    dmc.Grid(
                        children=[
                            dmc.GridCol(
                                dmc.Title('Flight Data Analysis', order=1),
                                span='content'
                            ),
                            dmc.GridCol(
                                dmc.Group(
                                    [
                                        dmc.Menu(
                                            children=[
                                                dmc.MenuTarget(
                                                    dmc.ActionIcon(
                                                        DashIconify(icon='mdi:github', width=25),
                                                        variant='transparent',
                                                        size='xl',
                                                        color='gray'
                                                    ),
                                                ),
                                                dmc.MenuDropdown(
                                                    children=[
                                                        dmc.MenuLabel('View Source For'),
                                                        dmc.MenuItem(
                                                            'Data Scraping',
                                                            href='https://github.com/magicmq/flight-scraper',
                                                            target='_blank',
                                                            leftSection=DashIconify(icon='mdi:database')
                                                        ),
                                                        dmc.MenuItem(
                                                            'Website',
                                                            href='https://github.com/magicmq/flight-analysis',
                                                            target='_blank',
                                                            leftSection=DashIconify(icon='mdi:web')
                                                        )
                                                    ]
                                                )
                                            ],
                                            trigger='hover',
                                            openDelay=100,
                                            closeDelay=500
                                        ),
                                        dmc.Menu(
                                            children=[
                                                dmc.MenuTarget(
                                                    dmc.ActionIcon(
                                                        DashIconify(icon='material-symbols:download-sharp', width=25),
                                                        variant='transparent',
                                                        size='xl',
                                                        color='gray'
                                                    ),
                                                ),
                                                dmc.MenuDropdown(
                                                    children=[
                                                        dmc.MenuLabel('Download Raw Data As'),
                                                        dmc.MenuItem(
                                                            'CSV',
                                                            id='download-csv',
                                                            leftSection=DashIconify(icon='mdi:table')
                                                        ),
                                                        dmc.MenuItem(
                                                            'Excel Spreadsheet',
                                                            id='download-excel',
                                                            leftSection=DashIconify(icon='mdi:microsoft-excel')
                                                        ),
                                                        dmc.MenuItem(
                                                            'JSON',
                                                            id='download-json',
                                                            leftSection=DashIconify(icon='mdi:code-braces')
                                                        )
                                                    ]
                                                )
                                            ],
                                            trigger='hover',
                                            openDelay=100,
                                            closeDelay=500
                                        ),
                                    ],
                                    justify='flex-end',
                                    gap='sm'
                                ),
                                span='auto'
                            )
                        ],
                        justify='space-between'
                    )
                ],
                justify='center',
                h=60
            )
        ],
        px=20
    )