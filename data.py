import sqlite3
import pandas as pd
import calendar

def fetch_data():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    left_table = 'data'
    right_table = 'data_post'
    exclude_left_columns = ['flight_raw', 'pass_rider_raw']
    exclude_right_columns = ['p_data_raw']
    join_column = 'hash'

    cursor.execute(f'PRAGMA table_info({left_table})')
    left_columns = [col[1] for col in cursor.fetchall()]

    cursor.execute(f'PRAGMA table_info({right_table})')
    right_columns = [col[1] for col in cursor.fetchall()]

    filtered_left_columns = [col for col in left_columns if col not in exclude_left_columns]
    filtered_right_columns = [col for col in right_columns if col not in exclude_right_columns and col not in left_columns and col != join_column]

    left_columns_str = ", ".join([f'{left_table}.{col}' for col in filtered_left_columns])
    right_columns_str = ", ".join([f'{right_table}.{col}' for col in filtered_right_columns])

    query = f"""
        SELECT {left_columns_str}, {right_columns_str}
        FROM {left_table}
        JOIN {right_table} ON {left_table}.{join_column} = {right_table}.{join_column}
    """

    data = pd.read_sql_query(query, connection)

    connection.close()

    return data

def transform_data(data):
    data['flight_no'] = data['flight_no'].str.lstrip('0')

    data['date'] = pd.to_datetime(data['date'])

    data['route'] = data.apply(lambda row: f'UAL{row["flight_no"]} ({row["origin"]}-{row["destination"]})', axis=1)

    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    data['day_of_week_name'] = data['day_of_week'].map({i: day for i, day in enumerate(calendar.day_name)})
    data['day_of_week_name'] = pd.Categorical(data['day_of_week_name'], categories=day_order, ordered=True)

    data['p_av_bu'] = data['p_ca_bu'] - data['p_bo_bu'] - data['p_ps_bu'] - data['p_he_bu'] - data['p_re_bu']
    data['p_av_co'] = data['p_ca_co'] - data['p_bo_co'] - data['p_ps_co'] - data['p_he_co'] - data['p_re_co']
    data['p_av_pp'] = data['p_ca_pp'] - data['p_bo_pp'] - data['p_ps_pp'] - data['p_he_pp'] - data['p_re_pp']
    data['p_av_to'] = data['p_ca_to'] - data['p_bo_to'] - data['p_ps_to'] - data['p_he_to'] - data['p_re_to']

    data['net_pos_va'] = data['av_to'] - data['pos_va']
    data['net_pos_pe'] = data['av_to'] - data['pos_pe']

    return data

def get_data():
    data = fetch_data()
    data = transform_data(data)
    return data

def get_data_as(type):
    if type == 'csv':
        return get_data().to_csv
    elif type == 'json':
        return get_data().to_json
    elif type == 'excel':
        return get_data().to_excel