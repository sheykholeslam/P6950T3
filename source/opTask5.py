from os.path import join, dirname
import numpy as np
import pandas as pd
import wget
import os
import argparse
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DataRange1d, Range1d, VBox, HBox, Select
from bokeh.palettes import Blues4
from bokeh.plotting import Figure, output_file, show, save
from scipy.signal import savgol_filter
from extract_data_from_csv import extract_data_from_csv

# Read data from .csv and manipulating the data based on program need
def DataSet(cityName):
    CurrentPath = os.getcwd()
    FilePath= (CurrentPath+'/DataFiles/GDD_Data_'+cityName+'.csv')
    Data, Date, MaxTemp, MinTemp = extract_data_from_csv(FilePath) 
    Data['date'] = pd.to_datetime(Date)
    Data['max'] = MaxTemp   
    Data['min'] = MinTemp
    Data['left'] = Data.date - pd.DateOffset(days=0.5)
    Data['right'] = Data.date + pd.DateOffset(days=0.5)
    Data['dateStr'] = Date
    NewGDD = Data['GDD']
    del Data['GDD']
    Data['GDD'] = NewGDD
    del Data['Unnamed: 0']
    del Data['Date/Time']
    del Data['Max Temp (ÃÂ°C)']
    del Data['Min Temp (ÃÂ°C)']        
    Data = Data.set_index(['date'])
    Data.sort_index(inplace=True) 
    return ColumnDataSource(data=Data)


def make_plot(src, city):
    plot = Figure(x_axis_type="datetime", plot_width=1000, title_text_font_size='12pt', tools="", toolbar_location=None)
    plot.title = city
    colors = Blues4[0:3]
    plot.line(x='date', y='GDD',source=src)
    
    plot.border_fill_color = "whitesmoke"
    plot.xaxis.axis_label = "Months"
    plot.yaxis.axis_label = "Accumulated GDD"
    plot.axis.major_label_text_font_size = "10pt"
    plot.axis.axis_label_text_font_size = "12pt"
    plot.axis.axis_label_text_font_style = "bold"
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12

    return plot

# set up callbacks for list select city data update interaction
def update_plot(attrname, old, new):
    src = DataSet(city_select.value)
    source.data.update(src.data)
    plot.title = city_select.value


def Main():
    # Taking the arguments from command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
	
    args = parser.parse_args()
	
    cityData = {}
	
	# Creating an object to make the list of dropdown and pass values to the make plot function. 
    cities = { 
        args.cityName[0] : {'ID':args.stationId[0]},
        args.cityName[1] : {'ID':args.stationId[1]},
        args.cityName[2] : {'ID':args.stationId[2]}
    }
	
    city = args.cityName[0]
    city_select = Select(value=city, title='City:', options=list(cities.keys()))
    
    for c in cities.keys():
        cityData[c] = DataSet(c)

    source = cityData[city]
    plot = make_plot(source, city)
    city_select.on_change('value', update_plot)
	
    # Saving the plot into disk
    output_file("./Plots/Op5.html", title="Optional Task # 5")
    save(HBox(city_select, plot))
	
	#curdoc().add_root(HBox(city_select, plot))

if __name__ == '__main__':
    Main()

#Main()
