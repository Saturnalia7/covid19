# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:31:07 2020

@author: comil
"""



from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import pandas as pd
import time
import requests
from requests_html import HTMLSession

url = r'https://www.nbcdfw.com/news/coronavirus/dallas-county-reports-20-new-covid-19-cases-1-death/2334317/'
# settings = webdriver.FirefoxOptions()
# settings.add_argument('-headless')

# driver = webdriver.Firefox(options=settings)
# driver.get(url)

# html = driver.find_element_by_tag_name('html').get_attribute('outerHTML')
# driver.quit()

session = HTMLSession()
resp = HTMLSession().get(url)
resp.html.render()


# print(html.find("table table-striped table-sm"))
# soup = BeautifulSoup(html, 'lxml')


# data = []
# table = soup.find('div', attrs={'id':'theTableTX'})
# print(table.text)

# table_body = table.find_all('tbody')

# rows = table_body.find_all('tr')
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     data.append([ele for ele in cols if ele])
