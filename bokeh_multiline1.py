# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:56:30 2021

@author: DeskTop
"""

from bokeh.models import ColumnDataSource, HoverTool, Legend
from bokeh.plotting import output_notebook
from bokeh.plotting import figure, show
import pandas as pd
from bokeh.palettes import Category10
import itertools

def plot_lines_multi(df,lw=2,pw=700,ph=400,t_str="save,pan,box_zoom,reset,wheel_zoom",t_loc='above'):
    '''...
    reference: https://docs.bokeh.org/en/latest/docs/user_guide/styling.html
    '''
#    source = ColumnDataSource(df)
#    col_names = source.column_names
    p = figure(x_axis_type="auto",plot_width=pw, plot_height=ph,toolbar_location=t_loc, tools=t_str)
    p_dict = dict()
    for col, c in zip(df.columns, color_g):
        #p_dict[col] = p.line(x=df.index, y=df[col], source=source, color=c, line_width=lw)
        p_dict[col] = p.line(df.index, df[col], color=c, line_width=lw) #, legend_label=col)
        p.add_tools(HoverTool(
            renderers=[p_dict[col]],
            tooltips=[('Year', '$index'),(col, ''),],
            formatters={},
            mode='mouse'
        ))
    # TODO: legend group
    legend = Legend(items=[(x, [p_dict[x]]) for x in df.columns])
    p.add_layout(legend,'right')
    show(p)
    
def color_gen():
    yield from itertools.cycle(Category10[10])
color_g = color_gen()

df = pd.read_csv("http://pythonhow.com/data/bachelors.csv")
output_notebook()
#df['Year'] = pd.to_datetime(df['Year'])
df.set_index("Year", inplace=True)
plot_lines_multi(df)