import json
from bokeh.io import show
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper, Slider)
from bokeh.layouts import column, row, widgetbox
from bokeh.palettes import brewer
from bokeh.plotting import figure
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
#import contextily as ctx

pd.set_option('display.max_columns', None)

pluto_EV = gpd.read_file('data/geojson/pluto_manhattan.geojson' )
print(pluto_EV.head)
geosource = GeoJSONDataSource(geojson = pluto_EV.to_json())
print(type(geosource))

#map_df = gpd.read_file(gpd.datasets.get_path('nybb'))

#print(map_df.head)

def plot_map():
    p = figure(title = 'Manhattan_housing',
               plot_height = 1200 ,
               plot_width = 950,
               toolbar_location = 'below',
               tools = 'pan, wheel_zoom, box_zoom, reset')
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    lots = p.patches('xs','ys', source = geosource,
                       fill_color = None,
                       line_color = 'gray',
                       line_width = 0.25,
                       fill_alpha = 1)

    p.add_tools(HoverTool(renderers = [lots],
                          tooltips = [('Address','@address'),
                                    ('Block','@block')]))

    show(p)


plot_map()
