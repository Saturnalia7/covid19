# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:27:21 2020

@author: comil
"""

import connection

cnxn, crsr, engine = connection.connect()

dim_county = '''
CREATE TABLE if not exists dim_county(
    id int AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    location_x float,
    location_Y float,
    PRIMARY KEY (id)
);'''
dim_sources = '''
CREATE TABLE if not exists dim_sources (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(45),
  alias varchar(10),
  url varchar(255),
  PRIMARY KEY (id)
);'''
fact_cases = '''
CREATE TABLE if not exists fact_cases(
    county_id int NOT NULL,
    source_id int NOT NULL,
    report_date date NOT NULL,
    cases int,
    deaths int,
    notes varchar(255),
    PRIMARY KEY (county_id, source_id, report_date)
);'''

drop = [('dim_sources'),('fact_cases')]
for i in drop:
    crsr.execute('DROP TABLE if exists {};'.format(i))

crsr.execute(dim_county)
crsr.execute(fact_cases)
crsr.execute(dim_sources)
cnxn.commit()
connection.disconnect(cnxn,crsr,engine)
