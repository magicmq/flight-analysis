from dotenv import load_dotenv
import os

load_dotenv()
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
DEBUG = bool(os.getenv('DEBUG'))
MYSQL_IP = os.getenv('MYSQL_IP')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

SCREENSHOT_URL='/pass-list-screenshots/{hash}.png'

COLUMN_LABELS = {
    'general': {
        'id': 'ID',
        'data_timestamp': 'Data Obtained Timestamp',
        'p_data_timestamp': 'Post-Departure Data Obtained Timestamp',
        'hash': 'Hash',
        'flight_no': 'Flight Number',
        'origin': 'Origin',
        'destination': 'Destination',
        'route': 'Route',
        'date': 'Date',
        'day_of_week': 'Day of Week',
        'day_of_week_name': 'Day of Week',
        'flight_time': 'Scheduled Departure Time',
        'actual_flight_time': 'Actual Departure Time'
    },
    'total': {
        'pre': {
            'av_to': 'Total Seats Available',
            'ca_to': 'Total Capacity',
            'au_to': 'Total Authorized',
            'bo_to': 'Total Booked',
            'ps_to': 'Total PS',
            'sa_to': 'Total SA',
            'he_to': 'Total Held',
            'gr_to': 'Total Group',
            're_to': 'Total Revenue Standby'
        },
        'post': {
            'p_av_to': '(Post-Departure Data) Total Seats Available',
            'p_ca_to': '(Post-Departure Data) Total Capacity',
            'p_au_to': '(Post-Departure Data) Total Authorized',
            'p_bo_to': '(Post-Departure Data) Total Booked',
            'p_ps_to': '(Post-Departure Data) Total PS',
            'p_sa_to': '(Post-Departure Data) Total SA',
            'p_he_to': '(Post-Departure Data) Total Held',
            'p_gr_to': '(Post-Departure Data) Total Group',
            'p_re_to': '(Post-Departure Data) Total Revenue Standby',
            'p_ci_to': '(Post-Departure Data) Total Checked In'
        }
    },
    'polaris': {
        'pre': {
            'av_bu': 'Polaris Seats Available',
            'ca_bu': 'Polaris Capacity',
            'au_bu': 'Polaris Authorized',
            'bo_bu': 'Polaris Booked',
            'ps_bu': 'Polaris PS',
            'sa_bu': 'Polaris SA',
            'he_bu': 'Polaris Held',
            'gr_bu': 'Polaris Group',
            're_bu': 'Polaris Revenue Standby'
        },
        'post': {
            'p_av_bu': '(Post-Departure Data) Polaris Available',
            'p_ca_bu': '(Post-Departure Data) Polaris Capacity',
            'p_au_bu': '(Post-Departure Data) Polaris Authorized',
            'p_bo_bu': '(Post-Departure Data) Polaris Booked',
            'p_ps_bu': '(Post-Departure Data) Polaris PS',
            'p_sa_bu': '(Post-Departure Data) Polaris SA',
            'p_he_bu': '(Post-Departure Data) Polaris Held',
            'p_gr_bu': '(Post-Departure Data) Polaris Group',
            'p_re_bu': '(Post-Departure Data) Polaris Revenue Standby',
            'p_ci_bu': '(Post-Departure Data) Polaris Checked In'
        }
    },
    'premium_plus': {
        'pre': {
            'av_pp': 'Premium Plus Seats Available',
            'ca_pp': 'Premium Plus Capacity',
            'au_pp': 'Premium Plus Authorized',
            'bo_pp': 'Premium Plus Booked',
            'ps_pp': 'Premium Plus PS',
            'sa_pp': 'Premium Plus SA',
            'he_pp': 'Premium Plus Held',
            'gr_pp': 'Premium Plus Group',
            're_pp': 'Premium Plus Revenue Standby'
        },
        'post': {
            'p_av_pp': '(Post-Departure Data) Premium Plus Available',
            'p_ca_pp': '(Post-Departure Data) Premium Plus Capacity',
            'p_au_pp': '(Post-Departure Data) Premium Plus Authorized',
            'p_bo_pp': '(Post-Departure Data) Premium Plus Booked',
            'p_ps_pp': '(Post-Departure Data) Premium Plus PS',
            'p_sa_pp': '(Post-Departure Data) Premium Plus SA',
            'p_he_pp': '(Post-Departure Data) Premium Plus Held',
            'p_gr_pp': '(Post-Departure Data) Premium Plus Group',
            'p_re_pp': '(Post-Departure Data) Premium Plus Revenue Standby',
            'p_ci_pp': '(Post-Departure Data) Premium Plus Checked In'
        }
    },
    'economy': {
        'pre': {
            'av_co': 'Economy Seats Available',
            'ca_co': 'Economy Capacity',
            'au_co': 'Economy Authorized',
            'bo_co': 'Economy Booked',
            'ps_co': 'Economy PS',
            'sa_co': 'Economy SA',
            'he_co': 'Economy Held',
            'gr_co': 'Economy Group',
            're_co': 'Economy Revenue Standby'
        },
        'post': {
            'p_av_co': '(Post-Departure Data) Economy Available',
            'p_ca_co': '(Post-Departure Data) Economy Capacity',
            'p_au_co': '(Post-Departure Data) Economy Authorized',
            'p_bo_co': '(Post-Departure Data) Economy Booked',
            'p_ps_co': '(Post-Departure Data) Economy PS',
            'p_sa_co': '(Post-Departure Data) Economy SA',
            'p_he_co': '(Post-Departure Data) Economy Held',
            'p_gr_co': '(Post-Departure Data) Economy Group',
            'p_re_co': '(Post-Departure Data) Economy Revenue Standby',
            'p_ci_co': '(Post-Departure Data) Economy Checked In'
        }
    },
    'standby': {
        'personal': {
            'pos_va': 'Position with Vacation Pass (SA3V)',
            'pos_pe': 'Position with Personal Pass (SA4P)',
            'net_pos_va': 'Total Available Minus Vacation Pass Position',
            'net_pos_pe': 'Total Available Minus Personal Pass Position'
        },
        'total': {
            'p_cl_to_to': 'Total Cleared',
            'p_sy_to_to': 'Total Not Cleared',
            'p_cl_ug_to': 'Total Upgrades Cleared',
            'p_sy_ug_to': 'Total Upgrades Not Cleared',
            'p_cl_sa_to': 'Total Standbys Cleared',
            'p_sy_sa_to': 'Total Standbys Not Cleared'
        },
        'polaris': {
            'p_cl_to_bu': 'Polaris Total Cleared',
            'p_sy_to_bu': 'Polaris Total Not Cleared',
            'p_cl_ug_bu': 'Polaris Upgrades Cleared',
            'p_sy_ug_bu': 'Polaris Upgrades Not Cleared',
            'p_cl_sa_bu': 'Polaris Standbys Cleared',
            'p_sy_sa_bu': 'Polaris Standbys Not Cleared'
        },
        'premium_plus': {
            'p_cl_to_pp': 'Premium Plus Total Cleared',
            'p_sy_to_pp': 'Premium Plus Total Not Cleared',
            'p_cl_ug_pp': 'Premium Plus Upgrades Cleared',
            'p_sy_ug_pp': 'Premium Plus Upgrades Not Cleared',
            'p_cl_sa_pp': 'Premium Plus Standbys Cleared',
            'p_sy_sa_pp': 'Premium Plus Standbys Not Cleared'
        },
        'economy': {
            'p_cl_to_co': 'Economy Total Cleared',
            'p_sy_to_co': 'Economy Total Not Cleared',
            'p_cl_ug_co': 'Economy Upgrades Cleared',
            'p_sy_ug_co': 'Economy Upgrades Not Cleared',
            'p_cl_sa_co': 'Economy Standbys Cleared',
            'p_sy_sa_co': 'Economy Standbys Not Cleared'
        }
    }
}

TOTAL_COLUMNS = [{'label': value, 'value': key}
    for section in COLUMN_LABELS['total'].values()
    for key, value in section.items()
]
POLARIS_COLUMNS = [
    {'label': value, 'value': key}
    for section in COLUMN_LABELS['polaris'].values()
    for key, value in section.items()
]
PP_COLUMNS = [
    {'label': value, 'value': key}
    for section in COLUMN_LABELS['premium_plus'].values()
    for key, value in section.items()
]
ECONOMY_COLUMNS = [
    {'label': value, 'value': key}
    for section in COLUMN_LABELS['economy'].values()
    for key, value in section.items()
]
STANDBY_COLUMNS = [
    {'label': value, 'value': key}
    for section in COLUMN_LABELS['standby'].values()
    for key, value in section.items()
]

ALL_COLUMNS = TOTAL_COLUMNS + POLARIS_COLUMNS + PP_COLUMNS + ECONOMY_COLUMNS + STANDBY_COLUMNS

FLAT_COLUMN_LABELS = {}
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['general'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['total']['pre'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['total']['post'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['polaris']['pre'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['polaris']['post'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['premium_plus']['pre'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['premium_plus']['post'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['economy']['pre'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['economy']['post'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['standby']['personal'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['standby']['total'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['standby']['polaris'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['standby']['premium_plus'])
FLAT_COLUMN_LABELS.update(COLUMN_LABELS['standby']['economy'])

COMPATIBLE_VARIABLES = {
    'route': {
        'time_series': {
            'date': True,
            'flight_no': False,
            'day_of_week_name': False
        },
        'scatter': {
            'date': True,
            'flight_no': False,
            'day_of_week_name': False            
        },
        'bar': {
            'date': True,
            'flight_no': False,
            'day_of_week_name': False            
        },
        'bar_means': {
            'date': False,
            'flight_no': False,
            'day_of_week_name': True
        }
    },
    'day_of_week_name': {
        'time_series': {
            'date': False,
            'flight_no': False,
            'day_of_week_name': False
        },
        'scatter': {
            'date': True,
            'flight_no': True,
            'day_of_week_name': False
        },
        'bar': {
            'date': True,
            'flight_no': True,
            'day_of_week_name': False
        },
        'bar_means': {
            'date': True,
            'flight_no': True,
            'day_of_week_name': False
        }
    }
}