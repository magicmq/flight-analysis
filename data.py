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
        flight_no_order = ['7', '143', '32', '39', '837', '875', '881', '803', '131']
        _data['flight_no'] = pd.Categorical(_data['flight_no'], categories=flight_no_order, ordered=True)

        _data['date'] = pd.to_datetime(_data['date'])

        _data['route'] = _data.apply(lambda row: f'UAL{row["flight_no"]} ({row["origin"]}-{row["destination"]})', axis=1)
        route_order = ['UAL7 (IAH-NRT)', 'UAL143 (DEN-NRT)', 'UAL32 (LAX-NRT)', 'UAL39 (LAX-HND)', 'UAL837 (SFO-NRT)', 'UAL875 (SFO-HND)', 'UAL881 (ORD-HND)', 'UAL803 (IAD-HND)', 'UAL131 (EWR-HND)']
        _data['route'] = pd.Categorical(_data['route'], categories=route_order, ordered=True)

        _data['day_of_week_name'] = _data['day_of_week'].map({i: day for i, day in enumerate(calendar.day_name)})
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        _data['day_of_week_name'] = pd.Categorical(_data['day_of_week_name'], categories=day_order, ordered=True)

        _data['flight_time'] = _data['flight_time'].str.replace('a', 'AM').str.replace('p', 'PM')
        _data['flight_time'] = pd.to_datetime(_data['flight_time'], format='%I:%M%p')
        _data['actual_flight_time'] = _data['actual_flight_time'].str.replace('a', 'AM').str.replace('p', 'PM')
        _data['actual_flight_time'] = pd.to_datetime(_data['actual_flight_time'], format='%I:%M%p')
        _data['minutes_late'] = ((_data['actual_flight_time'] - _data['flight_time']).dt.total_seconds()) / 60

        _data['p_av_bu'] = _data['p_ca_bu'] - _data['p_bo_bu'] - _data['p_ps_bu'] - _data['p_he_bu'] - _data['p_re_bu']
        _data['p_av_co'] = _data['p_ca_co'] - _data['p_bo_co'] - _data['p_ps_co'] - _data['p_he_co'] - _data['p_re_co']
        _data['p_av_pp'] = _data['p_ca_pp'] - _data['p_bo_pp'] - _data['p_ps_pp'] - _data['p_he_pp'] - _data['p_re_pp']
        _data['p_av_to'] = _data['p_ca_to'] - _data['p_bo_to'] - _data['p_ps_to'] - _data['p_he_to'] - _data['p_re_to']

        _data['p_cl_to_to'] = _data['p_cl_to_bu'] + _data['p_cl_to_co'] + _data['p_cl_to_pp']
        _data['p_sy_to_to'] = _data['p_sy_to_bu'] + _data['p_sy_to_co'] + _data['p_sy_to_pp']
        _data['p_cl_ug_to'] = _data['p_cl_ug_bu'] + _data['p_cl_ug_co'] + _data['p_cl_ug_pp']
        _data['p_sy_ug_to'] = _data['p_sy_ug_bu'] + _data['p_sy_ug_co'] + _data['p_sy_ug_pp']
        _data['p_cl_sa_to'] = _data['p_cl_sa_bu'] + _data['p_cl_sa_co'] + _data['p_cl_sa_pp']
        _data['p_sy_sa_to'] = _data['p_sy_sa_bu'] + _data['p_sy_sa_co'] + _data['p_sy_sa_pp']

        _data['net_pos_va'] = _data['av_to'] - _data['pos_va']
        _data['net_pos_pe'] = _data['av_to'] - _data['pos_pe']

        _data['p_net_pos_va_bu'] = _data['p_cl_to_bu'] - _data['pos_va']
        _data['p_net_pos_pe_bu'] = _data['p_cl_to_bu'] - _data['pos_pe']

    return _transform_data(data)

def get_data(hash=None):
    data = fetch_data()
    transform_data(data)
    if hash:
        return data[data['hash'] == hash]
    else:
        return data

def get_data_as(type):
    if type == 'csv':
        return get_data().to_csv
    elif type == 'json':
        return get_data().to_json
    elif type == 'excel':
        return get_data().to_excel