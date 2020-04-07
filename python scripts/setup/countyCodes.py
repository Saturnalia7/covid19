# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:31:18 2020

@author: comil
"""

import pandas as pd
import connection

path = r'C:\Users\comil\OneDrive\Documents\GitHub\covid19\data\dim'
fname = r'\PHR_MSA_County_masterlist.xlsx'

df = pd.ExcelFile(path + fname).parse('Sheet1')

df.rename(columns={'County Name': 'name'}, inplace=True)
df.drop(df.tail(2).index, inplace=True)
df = df.append({'name': 'Pending Assignment'}, ignore_index=True)

cnxn, crsr, engine = connection.connect()

df['name'].to_sql(
    name='dim_county',
    con=engine,
    if_exists='append',
    index=False)

connection.disconnect(cnxn, crsr, engine)
