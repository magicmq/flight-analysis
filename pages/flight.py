import dash
import dash_mantine_components as dmc
from datetime import datetime
import pytz

from components.genericheader import construct_header
from data import get_data

from columns import COLUMNS, get_columns_by_category
from constants import SCREENSHOT_URL

def title(hash=None, **kwargs):
    data = get_data(hash)
    return f'UAL{data.iloc[0]["flight_no"]} On {data.iloc[0]["date"].strftime("%m/%d/%Y")}'

dash.register_page(__name__, title=title, path_template='/flight/<hash>')

def layout(hash=None, **kwargs):
    data = get_data(hash)
    return dmc.AppShell(
        children = [
            construct_header('Flight Info'),
            construct_main(data)
        ],
        header={
            'height': 60,
        },
        padding='md'
    )

def construct_main(data):
    return dmc.AppShellMain(dmc.Box(
        [
            dmc.Title(f'{data.iloc[0]["route"]} On {data.iloc[0]["date"].strftime("%m/%d/%Y")}', order=2, mb=10),
            dmc.Accordion(
                [
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl(
                                dmc.Title('General Flight Information', order=3)
                            ),
                            dmc.AccordionPanel(
                                construct_flight_info(data)
                            )
                        ],
                        value='flight_info'
                    ),
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl(
                                dmc.Title('Total Values (All Cabins)', order=3)
                            ),
                            dmc.AccordionPanel(
                                construct_data_tables(
                                    data,
                                    'total',
                                    'Pre-Departure',
                                    'Post-Departure',
                                    'Pre-departure total values for this flight (all cabins).',
                                    'Post-departure total values for this flight (all cabins).'
                                )
                            )
                        ],
                        value='total_data'
                    ),
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl(
                                dmc.Title('Standby List Values', order=3)
                            ),
                            dmc.AccordionPanel(
                                construct_standby_data_tables(data)
                            )
                        ],
                        value='standby_data'
                    ),
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl(
                                dmc.Title('Polaris Cabin Values', order=3),
                            ),
                            dmc.AccordionPanel(
                                construct_data_tables(
                                    data,
                                    'polaris',
                                    'Pre-Departure',
                                    'Post-Departure',
                                    'Pre-departure Polaris cabin values for this flight.',
                                    'Post-departure Polaris cabin values for this flight.'
                                )
                            )
                        ],
                        value='polaris_data'
                    ),
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl(
                                dmc.Title('Premium Plus Cabin Values', order=3),
                            ),
                            dmc.AccordionPanel(
                                construct_data_tables(
                                    data,
                                    'premium_plus',
                                    'Pre-Departure',
                                    'Post-Departure',
                                    'Pre-departure Premium Plus cabin values for this flight.',
                                    'Post-departure Premium Plus cabin values for this flight.'
                                )
                            )
                        ],
                        value='pp_data'
                    ),
                    dmc.AccordionItem(
                        [
                            dmc.AccordionControl(
                                dmc.Title('Economy Cabin Values', order=3),
                            ),
                            dmc.AccordionPanel(
                                construct_data_tables(
                                    data,
                                    'economy',
                                    'Pre-Departure',
                                    'Post-Departure',
                                    'Pre-departure Economy cabin values for this flight.',
                                    'Post-departure Economy cabin values for this flight.'
                                )
                            )
                        ],
                        value='economy_data'
                    )
                ],
                multiple=True,
                value=['flight_info'],
                radius='sm',
                variant='separated'
            )
        ]
    ))

def construct_flight_info(data):
    return dmc.SimpleGrid(
        [
            dmc.Card(
                [
                    dmc.Title('Overview', order=4, mb=5),
                    dmc.Text([dmc.Text('Date: ', fw=500, span=True), data.iloc[0]['date'].strftime('%m/%d/%Y')]),
                    dmc.Text([dmc.Text('Day of Week: ', fw=500, span=True), data.iloc[0]['day_of_week_name']]),
                    dmc.Text([dmc.Text('Scheduled Departure Time: ', fw=500, span=True), data.iloc[0]['flight_time'].strftime('%I:%M %p (local time)')]),
                    dmc.Text([dmc.Text('Actual Departure Time: ', fw=500, span=True), data.iloc[0]['actual_flight_time'].strftime('%I:%M %p (local time)')]),
                    dmc.Text([dmc.Text('Delay: ', fw=500, span=True), format_minutes_late(data.iloc[0]['minutes_late'])]),
                    dmc.Text([dmc.Text('Data Obtained At: ', fw=500, span=True), format_timestamp(data.iloc[0]['data_timestamp'])]),
                    dmc.Text([dmc.Text('Post-Departure Data Obtained At: ', fw=500, span=True), format_timestamp(data.iloc[0]['p_data_timestamp'])]),
                    dmc.Title('What Ifs', order=4, mt=10, mb=5),
                    dmc.Text([dmc.Text('Would a passrider with SA3V priority have gotten on this flight? ', fw=500, span=True), get_what_if(data.iloc[0]['net_pos_va'], 0, '>=')]),
                    dmc.Text([dmc.Text('Would a passrider with SA4P priority have gotten on this flight? ', fw=500, span=True), get_what_if(data.iloc[0]['net_pos_pe'], 0, '>=')]),
                    dmc.Text([dmc.Text('Would a passrider with SA3V priority have gotten a polaris seat on this flight? ', fw=500, span=True), get_what_if(data.iloc[0]['p_net_pos_va_bu'], 0, '>=')]),
                    dmc.Text([dmc.Text('Would a passrider with SA4P priority have gotten a polaris seat on this flight? ', fw=500, span=True), get_what_if(data.iloc[0]['p_net_pos_pe_bu'], 0, '>=')]),
                    dmc.Title('Data Rundown', order=4, mt=10),
                    construct_data_rundown(data)
                ],
                withBorder=True
            ),
            dmc.Card(
                [
                    dmc.Title('Standby List', order=4, mb=10),
                    dmc.Image(src=SCREENSHOT_URL.format(hash=data.iloc[0]['hash']), alt='Standby list not found for this flight.')
                ],
                withBorder=True
            )
        ],
        cols={'base': 1, 'lg': 2},
        spacing='md',
        verticalSpacing='md'
    )

def construct_data_rundown(data):
    rows = [
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['av_to']['label']),
                dmc.TableTd(data.iloc[0]['av_to'])
            ]
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['av_bu']['label']),
                dmc.TableTd(data.iloc[0]['av_bu'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['he_to']['label']),
                dmc.TableTd(data.iloc[0]['he_to'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['pos_pe']['label']),
                dmc.TableTd(data.iloc[0]['pos_pe'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['pos_va']['label']),
                dmc.TableTd(data.iloc[0]['pos_va'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['p_net_pos_pe_bu']['label']),
                dmc.TableTd(data.iloc[0]['p_net_pos_pe_bu'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['p_net_pos_va_bu']['label']),
                dmc.TableTd(data.iloc[0]['p_net_pos_va_bu'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['p_cl_sa_bu']['label']),
                dmc.TableTd(data.iloc[0]['p_cl_sa_bu'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['p_cl_sa_pp']['label']),
                dmc.TableTd(data.iloc[0]['p_cl_sa_pp'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd(COLUMNS['p_cl_sa_co']['label']),
                dmc.TableTd(data.iloc[0]['p_cl_sa_co'])
            ],
        ),
        dmc.TableTr(
            [
                dmc.TableTd('Standbys Not Cleared'),
                dmc.TableTd(data.iloc[0]['p_sy_sa_co_net'])
            ],
        ),
    ]

    body = dmc.TableTbody(rows)

    return dmc.Table(
        [body],
        striped=True,
        highlightOnHover=True,
        withTableBorder=False,
        withColumnBorders=False,
        horizontalSpacing=10
    )

def construct_standby_data_tables(data):
    return dmc.SimpleGrid(
        [
            dmc.Box(
                [
                    dmc.Title('Personal Standby Values', order=4, mb=10),
                    construct_data(data, 'standby', 'personal', 'Personal standby data for this flight.')
                ]
            ),
            dmc.Box(
                [
                    dmc.Title('Total Values (All Cabins)', order=4, mb=10),
                    construct_data(data, 'standby', 'total', 'Total standby values for this flight (all cabins).')
                ]
            ),
            dmc.Box(
                [
                    dmc.Title('Polaris Cabin Values', order=4, mb=10),
                    construct_data(data, 'standby', 'polaris', 'Polaris standby values for this flight.')
                ]
            ),
            dmc.Box(
                [
                    dmc.Title('Premium Plus Cabin Values', order=4, mb=10),
                    construct_data(data, 'standby', 'premium_plus', 'Premium plus standby values for this flight.')
                ]
            ),
            dmc.Box(
                [
                    dmc.Title('Economy Cabin Values', order=4, mb=10),
                    construct_data(data, 'standby', 'economy', 'Economy standby values for this flight.')
                ]
            )
        ],
        cols={'base': 1, 'sm': 2, 'lg': 3, 'xl': 4},
        spacing='md',
        verticalSpacing='md'
    )

def construct_data_tables(data, section, title_1, title_2, caption_1, caption_2):
    return dmc.SimpleGrid(
        [
            dmc.Box(
                [
                    dmc.Title(title_1, order=4, mb=10),
                    construct_data(data, section, 'pre', caption_1)
                ]
            ),
            dmc.Box(
                [
                    dmc.Title(title_2, order=4, mb=10),
                    construct_data(data, section, 'post', caption_2)
                ]
            )
        ],
        cols={'base': 1, 'lg': 2},
        spacing='md',
        verticalSpacing='md'
    )

def construct_data(data, section, pre_post, caption):
    rows = []
    for key, value in get_columns_by_category(section, pre_post).items():
        number = data.iloc[0][key]
        rows.append(dmc.TableTr(
            [
                dmc.TableTd(value['label']),
                dmc.TableTd(number)
            ]
        ))

    body = dmc.TableTbody(rows)
    caption = dmc.TableCaption(caption)

    return dmc.Card(
        [
            dmc.Table(
                [body, caption],
                striped=False,
                highlightOnHover=True,
                withTableBorder=False,
                withColumnBorders=False,
                horizontalSpacing=1
            )
        ],
        withBorder=True
    )

def format_minutes_late(minutes_late):
    if minutes_late >= 10:
        hours = int(minutes_late // 60)
        minutes = int(minutes_late % 60)
        return f'Flight departed {hours} hours, {minutes} minutes late'
    else:
        return 'Flight departed on time'


def format_timestamp(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    central_tz = pytz.timezone('US/Central')
    central_time = pytz.utc.localize(utc_time).astimezone(central_tz)
    return central_time.strftime('%m/%d/%Y %I:%M:%S %p %Z')

def get_what_if(value_1, value_2, operator):
    operators = {
        '<': lambda x, y: x < y,
        '>': lambda x, y: x > y,
        '==': lambda x, y: x == y,
        '<=': lambda x, y: x <= y,
        '>=': lambda x, y: x >= y
    }

    return 'Yes' if operators[operator](value_1, value_2) else 'No'