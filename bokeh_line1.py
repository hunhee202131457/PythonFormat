#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:43:28 2021

@author: hunheekim
"""

# prepare some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [i**2 for i in x]

a create a new plot
fig = go.figure(
    layout=dict(
        title="Example Plotly plot",
        yaxis_type="log",
        yaxis_range=[-3, 3],
        xaxis_title='sections',
        yaxis_title='particles',
        )
    )
fig.add_trace(go.Scatter(x=x, y=x, mode='makers', name="y=x,", marker=dict(color='royalblue', size=s)))
fig.add_trace(go.Scatter(x=x, y=y, name="yx^w", line=dict(width=3)))

fig.show()