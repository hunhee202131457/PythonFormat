#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:45:47 2021

@author: hunheekim
"""
from functools import reduce

my_floats = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
my_names = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15]
my_numbers = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))    
filter_result = list(filter(lambda name: len(name)10, my_names))
reduce_result =list(reduce(lambda num1, num2: num1 * num2, my_numbers))

    print(map_result)
    print(filter_result)
    print(reduce_result)