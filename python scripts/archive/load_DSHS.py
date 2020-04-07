# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import sqlite3 as sql

date =  '03-14-2020'
file_date = date.replace('-', '')
file_date = file_date[-2:] + file_date[:2] + file_date[2:4]
root_dir = 'C:\\Users\\comil\\Documents\\'
testFile = root_dir + '{}.txt'.format(file_date)
inputFile = open(testFile, "r")


lst = []
for idx, line in enumerate(inputFile):
    line = line.replace(' \t', "@").replace('\n', '').split('@')
    lst.append(line)

lst.pop()
inputFile.close()

input_df = pd.DataFrame(data=lst, columns=['county','cases'])

cnxn = sql.connect('covid19.db')

cnty_sql = 'SELECT id, name FROM dim_county'
cnty_df = pd.read_sql(cnty_sql, cnxn, index_col='name')

input_df.set_index(['county'], inplace=True)
input_df = input_df.join(cnty_df, on='county')
input_df.set_index(['id'], inplace=True)
# input_df.insert(0, 'report_date', date)


cnxn.commit()
cnxn.close()