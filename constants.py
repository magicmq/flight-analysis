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

FLIGHT_PAGE_URL = '/flight/{hash}'
SCREENSHOT_URL = '/pass-list-screenshots/{hash}.png'

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