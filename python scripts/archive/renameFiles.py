# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:33:21 2020

@author: comil
"""
import os
from os.path import isfile, join

x = 'NBC'
dir = r'C:\Users\comil\OneDrive\Documents\GitHub\covid19\data\{}'.format(x)
print(dir)

list = os.listdir(dir)
for idx, val in enumerate(os.listdir(dir)):
    src = '\\'.join([dir,val])
    dst = src.replace('_{}'.format(x),'')
    #print(src, dst)
    os.rename(src,dst)
