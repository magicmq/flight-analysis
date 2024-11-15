from sqlalchemy import create_engine, MetaData, Table
import pandas as pd
import calendar

from flask_caching import Cache

from constants import MYSQL_IP
from constants import MYSQL_PORT
from constants import MYSQL_USERNAME
from constants import MYSQL_PASSWORD

cache = None

def init_cache(app):
    global cache

    cache = Cache(app.server, config={
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 21600
    })

def fetch_data():
    @cache.memoize()
    def _fetch_data():
        engine = create_engine(f'mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_IP}:{MYSQL_PORT}/data')
        metadata = MetaData()

        left_table = Table('data', metadata, autoload_with=engine)
        right_table = Table('data_post', metadata, autoload_with=engine)

        exclude_left_columns = ['flight_raw', 'pass_rider_raw']
        exclude_right_columns = ['p_data_raw']
        join_column = 'hash'

        left_columns = [col.name for col in left_table.columns if col.name not in exclude_left_columns]
        right_columns = [
            col.name for col in right_table.columns
            if col.name not in exclude_right_columns and col.name not in left_columns and col.name != join_column
        ]

        left_columns_str = ", ".join([f'data.{col}' for col in left_columns])
        right_columns_str = ", ".join([f'data_post.{col}' for col in right_columns])

        query = f"""
            SELECT {left_columns_str}, {right_columns_str}
            FROM data
            JOIN data_post ON data.{join_column} = data_post.{join_column}
        """

        with engine.connect() as connection:
            data = pd.read_sql_query(query, connection)
        
        return data

    return _fetch_data()

def transform_data(data):
    @cache.memoize()
    def _transform_data(_data):
        _data['flight_no'] = _data['flight_no'].str.lstrip('0')

        _data['date'] = pd.to_datetime(_data['date'])

        _data['route'] = _data.apply(lambda row: f'UAL{row["flight_no"]} ({row["origin"]}-{row["destination"]})', axis=1)

        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        _data['day_of_week_name'] = _data['day_of_week'].map({i: day for i, day in enumerate(calendar.day_name)})
        _data['day_of_week_name'] = pd.Categorical(_data['day_of_week_name'], categories=day_order, ordered=True)

        _data['p_av_bu'] = _data['p_ca_bu'] - _data['p_bo_bu'] - _data['p_ps_bu'] - _data['p_he_bu'] - _data['p_re_bu']
        _data['p_av_co'] = _data['p_ca_co'] - _data['p_bo_co'] - _data['p_ps_co'] - _data['p_he_co'] - _data['p_re_co']
        _data['p_av_pp'] = _data['p_ca_pp'] - _data['p_bo_pp'] - _data['p_ps_pp'] - _data['p_he_pp'] - _data['p_re_pp']
        _data['p_av_to'] = _data['p_ca_to'] - _data['p_bo_to'] - _data['p_ps_to'] - _data['p_he_to'] - _data['p_re_to']

        _data['net_pos_va'] = _data['av_to'] - _data['pos_va']
        _data['net_pos_pe'] = _data['av_to'] - _data['pos_pe']

    return _transform_data(data)

def get_data():
    data = fetch_data()
    transform_data(data)
    return data

def get_data_as(type):
    if type == 'csv':
        return get_data().to_csv
    elif type == 'json':
        return get_data().to_json
    elif type == 'excel':
        return get_data().to_excel