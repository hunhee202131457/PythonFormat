#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:28:16 2021

@author: hunheekim
"""

score = int(input("input Score:"))
if 100 >= score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "c"
elif 70 > score >= 60:
    
else:
    grade = "F"
    
print("Grade is"+grade)