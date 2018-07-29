# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:18:17 2018
Cousera Course 1 Week 3 assignment
@author: Chunxiao Li

"""
import pandas as pd
energy=pd.read_excel("Energy Indicators.xls", skiprows=17,skip_footer=38,\
                 usecols="C:F",no_values="...", \
                 names=['Country', 'Energy Supply', 'Energy Suppita', '% Renewable'])

energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})
energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
energy['Country'] = energy['Country'].str.replace('\d+', '')

print energy


