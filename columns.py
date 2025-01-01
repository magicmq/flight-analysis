COLUMNS = {
    'id': {
        'category': 'general',
        'sub_category': '',
        'label': 'ID',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'data_timestamp': {
        'category': 'general',
        'sub_category': '',
        'label': 'Data Obtained Timestamp',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'p_data_timestamp': {
        'category': 'general',
        'sub_category': '',
        'label': 'Post-Departure Data Obtained Timestamp',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'hash': {
        'category': 'general',
        'sub_category': '',
        'label': 'Hash',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'flight_no': {
        'category': 'general',
        'sub_category': '',
        'label': 'Flight Number',
        'x_axis': True,
        'y_axis': False,
        'color': False
    },
    'origin': {
        'category': 'general',
        'sub_category': '',
        'label': 'Origin',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'destination': {
        'category': 'general',
        'sub_category': '',
        'label': 'Destination',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'route': {
        'category': 'general',
        'sub_category': '',
        'label': 'Route',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'date': {
        'category': 'general',
        'sub_category': '',
        'label': 'Date',
        'x_axis': True,
        'y_axis': False,
        'color': False
    },
    'day_of_week': {
        'category': 'general',
        'sub_category': '',
        'label': 'Day of Week',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'day_of_week_name': {
        'category': 'general',
        'sub_category': '',
        'label': 'Day of Week',
        'x_axis': True,
        'y_axis': False,
        'color': False
    },
    'flight_time': {
        'category': 'general',
        'sub_category': '',
        'label': 'Scheduled Departure Time',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'actual_flight_time': {
        'category': 'general',
        'sub_category': '',
        'label': 'Actual Departure Time',
        'x_axis': False,
        'y_axis': False,
        'color': False
    },
    'minutes_late': {
        'category': 'general',
        'sub_category': '',
        'label': 'Minutes Late',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'av_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Seats Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'ca_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'au_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'bo_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'ps_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'sa_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'he_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'gr_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    're_to': {
        'category': 'total',
        'sub_category': 'pre',
        'label': 'Total Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_av_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Seats Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_ca_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_au_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_bo_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ps_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sa_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_he_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_gr_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_re_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ci_to': {
        'category': 'total',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Total Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'av_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Seats Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'ca_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'au_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'bo_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'ps_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'sa_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'he_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'gr_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    're_bu': {
        'category': 'polaris',
        'sub_category': 'pre',
        'label': 'Polaris Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_av_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_ca_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_au_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_bo_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ps_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sa_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_he_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_gr_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_re_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ci_bu': {
        'category': 'polaris',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Polaris Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'av_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Seats Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'ca_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'au_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'bo_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'ps_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'sa_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'he_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'gr_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    're_pp': {
        'category': 'premium_plus',
        'sub_category': 'pre',
        'label': 'Premium Plus Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_av_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_ca_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_au_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_bo_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ps_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sa_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_he_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_gr_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_re_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ci_pp': {
        'category': 'premium_plus',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Premium Plus Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'av_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Seats Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'ca_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'au_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'bo_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'ps_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'sa_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'he_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'gr_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    're_co': {
        'category': 'economy',
        'sub_category': 'pre',
        'label': 'Economy Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_av_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Available',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_ca_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Capacity',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_au_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Authorized',
        'x_axis': False,
        'y_axis': True,
        'color': False
    },
    'p_bo_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Booked',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ps_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy PS',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sa_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy SA',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_he_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Held',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_gr_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Group',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_re_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Revenue Standby',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_ci_co': {
        'category': 'economy',
        'sub_category': 'post',
        'label': '(Post-Departure Data) Economy Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'pos_va': {
        'category': 'standby',
        'sub_category': 'personal',
        'label': 'Position with Vacation Pass (SA3V)',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'pos_pe': {
        'category': 'standby',
        'sub_category': 'personal',
        'label': 'Position with Personal Pass (SA4P)',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'net_pos_va': {
        'category': 'standby',
        'sub_category': 'personal',
        'label': 'Total Available Minus SA3V Position',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'net_pos_pe': {
        'category': 'standby',
        'sub_category': 'personal',
        'label': 'Total Available Minus SA4P Position',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_net_pos_va_bu': {
        'category': 'standby',
        'sub_category': 'personal',
        'label': 'Polaris Total Cleared Minus SA3V Position',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_net_pos_pe_bu': {
        'category': 'standby',
        'sub_category': 'personal',
        'label': 'Polaris Total Cleared Minus SA4P Position',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_to_to': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_to_to_net': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
        'p_sy_to_to_nci': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_ug_to': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Upgrades Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_ug_to_net': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Upgrades Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_ug_to_nci': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Upgrades Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_sa_to': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Standbys Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_sa_to_net': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Standbys Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_sa_to_nci': {
        'category': 'standby',
        'sub_category': 'total',
        'label': 'Total Standbys Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_to_bu': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Total Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_to_bu_net': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Total Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_to_bu_nci': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Total Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_ug_bu': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Upgrades Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_ug_bu_net': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Upgrades Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_ug_bu_nci': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Upgrades Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_sa_bu': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Standbys Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_sa_bu_net': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Standbys Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_sa_bu_nci': {
        'category': 'standby',
        'sub_category': 'polaris',
        'label': 'Polaris Standbys Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_to_pp': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Total Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_to_pp_net': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Total Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_to_pp_nci': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Total Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_ug_pp': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Upgrades Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_ug_pp_net': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Upgrades Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_ug_pp_nci': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Upgrades Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_sa_pp': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Standbys Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_sa_pp_net': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Standbys Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_sa_pp_nci': {
        'category': 'standby',
        'sub_category': 'premium_plus',
        'label': 'Premium Plus Standbys Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_to_co': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Total Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_to_co_net': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Total Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_to_co_nci': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Total Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_ug_co': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Upgrades Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_ug_co_net': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Upgrades Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_ug_co_nci': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Upgrades Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_cl_sa_co': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Standbys Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
    'p_sy_sa_co_net': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Standbys Not Cleared',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn_r',
        }
    },
    'p_sy_sa_co_nci': {
        'category': 'standby',
        'sub_category': 'economy',
        'label': 'Economy Standbys Not Checked In',
        'x_axis': False,
        'y_axis': True,
        'color': True,
        'color_info': {
            'scale': 'RdYlGn',
        }
    },
}

def get_columns_by_category(category, sub_category=''):
    to_return = {}
    for key, value in COLUMNS.items():
        if value['category'] == category:
            if sub_category == '':
                to_return[key] = value
                continue
            if value['sub_category'] == sub_category:
                to_return[key] = value
    return to_return

def get_x_axis_columns():
    to_return = []
    for key, value in COLUMNS.items():
        if value['x_axis']:
            to_return.append({'value': key, 'label': COLUMNS[key]['label']})
    return to_return

def get_y_axis_columns(category):
    to_return = []
    columns = get_columns_by_category(category)
    for key, value in columns.items():
        if value['y_axis']:
            to_return.append({'value': key, 'label': value['label']})
    return to_return

def get_color_columns(category):
    to_return = []
    columns = get_columns_by_category(category)
    for key, value in columns.items():
        if value['color']:
            to_return.append({'value': key, 'label': value['label']})
    return to_return

def get_color_info(key):
    return COLUMNS[key]['color_info']

def get_label(key):
    return COLUMNS[key]['label']