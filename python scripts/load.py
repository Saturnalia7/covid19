# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import connection
import re
import sys

def county_id(engine):
    df = connection.select(engine, 'dim_county', ['id','name'])
    return df

def source_id(engine):
    df = connection.select(engine, 'dim_sources', ['id', 'alias'])
    return df

def load(date=None, method=None):
    try:
        r = re.compile('.{2}/.{2}/.{4}')
        if r.match(date) is None:
            raise SyntaxError
        if method not in ['bno','dshs','hc','nbc']:
            print('''Method paramter must be in
                ['bno','dshs','hc','nbc']''')
            return
        date = date.replace('/', '')
        file_date = date[-2:] + date[:2] + date[2:4]
        dir = r'C:\Users\comil\OneDrive\Documents\GitHub\covid19\data\{}'.format(method)
        path = dir + '/{}.txt'.format(file_date)

        df = pd.read_csv(path, sep='\t',
            names=['county','cases','deaths','notes']
        )
        df['county'] = df['county'].str.replace(' County', "")
        return df
    except SyntaxError:
        print('Date needs to be in MM-DD-YYYY format')


date = '04/02/2020'
method = 'nbc'

cnxn, crsr, engine = connection.connect()

df_county = county_id(engine)
df_county.set_index(['name'], inplace=True)

df_src = source_id(engine)
df_src = df_src[df_src.alias.eq(method)]

df_load = load(date,method)
df_load.set_index(['county'], inplace=True)
df_load = df_load.join(df_county, on='county')
df_load.set_index(['id'], inplace=True)
df_load['report_date'] = pd.to_datetime(date)
df_load['source_id'] = df_src.iloc[0]['id']

df_load.to_sql(
        name='fact_cases',
        con=engine,
        if_exists='append',
        index_label='county_id')

connection.disconnect(cnxn, crsr, engine)
