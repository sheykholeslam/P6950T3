from os.path import join, dirname
import numpy as np
import pandas as pd
import wget
import os
import argparse
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DataRange1d, Range1d, VBox, HBox, Select, BoxSelectTool
from bokeh.palettes import Blues4
from bokeh.plotting import Figure, output_file, show, save
from scipy.signal import savgol_filter

source = ColumnDataSource()

stationId = [50089, 51157, 50430]
cityName = ['St_Johns', 'Montreal','Calgary']
	
cityData = {}
cities = { 
cityName[0] : {'ID':stationId[0]},
cityName[1] : {'ID':stationId[1]},
cityName[2] : {'ID':stationId[2]}
}
	
city = cityName[0]
city_select = Select(value=city, title='City:', options=list(cities.keys()))

plot = Figure()

def extract_data_from_csv(FilePath):
    File_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = ',' ,skiprows=0)
    Data = pd.DataFrame(File_Data)
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    Index = Data.keys()
    Date, maxTemp, minTemp = np.array(Data[Index[1]]),np.array(Data[Index[2]]), np.array(Data[Index[3]])
    
    return Data, Date, maxTemp, minTemp


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
    TOOLS = [BoxSelectTool()]
    global plot
    plot = Figure(x_axis_type="datetime", plot_width=1000, title_text_font_size='12pt', tools=TOOLS)
    plot.title = city
    colors = Blues4[0:3]
    plot.line(x='date', y='GDD',source=src, line_width=4)
    
    plot.border_fill_color = "whitesmoke"
    plot.xaxis.axis_label = "Months"
    plot.yaxis.axis_label = "Accumulated GDD"
    plot.axis.major_label_text_font_size = "10pt"
    plot.axis.axis_label_text_font_size = "12pt"
    plot.axis.axis_label_text_font_style = "bold"
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12

    return plot

# set up callbacks
def update_plot(attrname, old, new):
    src = DataSet(city_select.value)
    source.data.update(src.data)
    global plot
    plot.title = city_select.value
#    plot.line(x='date', y='GDD',source=source, line_width=4)
#    plot=make_plot(src,city_select.value)
 

def Main():
#    parser = argparse.ArgumentParser()
#    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
#    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
	
#    args = parser.parse_args()
	
#city = args.cityName[0]
	
    #cities = { 
    #    args.cityName[0] : {'ID':args.stationId[0]},
    #    args.cityName[1] : {'ID':args.stationId[1]},
    #    args.cityName[2] : {'ID':args.stationId[2]}
    #}
	
   
#    for c in cities.keys():
    
    global source
    source = DataSet('St_Johns')
    plot = make_plot(source, city)
    city_select.on_change('value', update_plot)
	
    # add to document
    output_file("./Plots/Op5.html", title="Optional Task # 5")
    save(HBox(city_select, plot))
	
    curdoc().add_root(HBox(city_select, plot))

#if __name__ == '__main__':
Main()

