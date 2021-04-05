# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:55:56 2021

@author: johnl
"""
#reference: https://stackoverflow.com/questions/42145097/why-do-bokeh-tutorials-use-explicit-imports-rather-than-aliases

from bokeh.plotting import figure, output_file, show
import pandas as pd

df=pd.read_csv("adbe.csv", parse_dates=["Date"], index_col=0) #or index_col=["Date"]
# ref: https://rfriend.tistory.com/536
# Date, Open, High, Low, Close, Volume

output_file("TimeSeries1.html")
p = figure(width=500, height=300, x_axis_type="datetime")
p.line(df.index, df["Close"], color="red", alpha=0.5)
show(p)

#ref: https://docs.bokeh.org/en/latest/docs/gallery.html
