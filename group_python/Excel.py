#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:10:16 2021

@author: hunheekim
"""

import openpyxl
import pandas as pd

xlsxFile = 'group_python.xlsx'
sheetList = {}

wb = openpyxl.load_workbook(xlsxFile)
for i in wb.sheetnames:
    sheetList.append(i)
    
    xlsx = pd.ExcelFile(xlsxFile)
    
    for j in sheetList:
        df = pd.read_excel(xlsx.j)
        print('%s 인원들 데이터입니다.' %j)
        print(df)
        print('*' * 50)