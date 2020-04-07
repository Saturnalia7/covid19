

import pandas as pd
import connection

path = r'C:\Users\comil\OneDrive\Documents\GitHub' \
    r'\covid19\data\dim\sources.txt'
df = pd.read_csv(
    path,
    sep='\t',
    names=['name','alias','url']
)

cnxn, crsr, engine = connection.connect()
df.to_sql(
    name='dim_sources',
    con=engine,
    if_exists='append',
    index=False
)

connection.disconnect(cnxn, crsr, engine)
