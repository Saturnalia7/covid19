# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:35:55 2020

@author: comil
"""

import pandas as pd
from sqlalchemy import create_engine
import config


def connect():
    conn_str = 'mysql+mysqlconnector://' \
    '{user}:{password}@{host}:3306/{database}' \
    .format(**config.mysql)
    engine = create_engine(conn_str)
    cnxn = engine.raw_connection()
    crsr = cnxn.cursor()

    return cnxn, crsr, engine

def disconnect(cnxn,crsr,engine):
    crsr.close()
    cnxn.close()
    engine.dispose()
    return

def select(engine,table,columns=['*']):
    '''
    Parameters
    ----------
    table : str, optional
        table name. The default is None.
    columns : list-str, optional
        list of column names. The default is ['*'].

    Returns
    -------
    data : list-tuple or pandas Dataframe
        Data from query.
    '''

    #cnxn, crsr, engine = connect()
    query = """SELECT {0} FROM {1}""".format(
        ','.join(columns),table
    )
    data = pd.read_sql(query, engine)

    #disconnect(cnxn, crsr, engine)
    return data


'''
def insert(table,columns,values):
    cnxn, crsr = make_connect()
    query = """INSERT INTO {0}({1})""".format(
        table,
        ','.join(columns),
    )
    close_connect(cnxn, crsr)
    return 'Success'
'''
