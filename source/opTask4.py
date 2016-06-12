from os.path import join, dirname
import numpy as np
import pandas as pd
import wget
import os

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DataRange1d, Range1d, VBox, HBox, Select, HoverTool, BoxSelectTool
from bokeh.palettes import Spectral11
from bokeh.plotting import Figure
from scipy.signal import savgol_filter

startYear = 2015
endYear = 2015
baseTemp=10
cityData = {}


def checkGDD(values):
    gdd = []
    item = 0
    for i in values:
        if i >= 0:
            item += i
        gdd.append(item)
    return gdd

def download_data(stationId, startYear, endYear, baseTemp):
    while (startYear <= endYear):
        url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='+str(stationId)+'&Year='+str(startYear)+'&Month=12&Day=31&timeframe=2&submit= Download+Data'
        filename = wget.download(url)
        hourly_data = pd.read_csv(filename, encoding = 'ISO-8859-1', delimiter = ",", skiprows=25)        
        Data = pd.DataFrame(hourly_data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
        Data.replace('', np.nan, inplace = True)
        Data = Data.dropna() 
        Data['date'] = pd.to_datetime(Data['Date/Time'])
        Data['min'] = Data['Min Temp (°C)']
        Data['max'] = Data['Max Temp (°C)']        
        Data['left'] = Data.date - pd.DateOffset(days=0.5)
        Data['right'] = Data.date + pd.DateOffset(days=0.5)
        Data['dateStr'] = Data['Date/Time']
        del Data['Date/Time']
        del Data['Max Temp (°C)']
        del Data['Min Temp (°C)']
        
        Data = Data.set_index(['date'])
        Data.sort_index(inplace=True)                                                        

        Data['GDD'] = ((Data['max'] + Data['min'])/2)- baseTemp
        Data['GDD'] = checkGDD(Data['GDD'])        
        MinTemp, MaxTemp = np.array(Data['min']), np.array(Data['max'])
        startYear = startYear + 1
        os.remove(filename)

        # Save Data in Local directory as cvs file
        currentpath = os.getcwd()
        filepath= (currentpath+'/DataFiles/GDD_Data.csv')
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
        with open(filepath, 'w') as datafile:
            Data.to_csv(filepath, sep='\t', encoding='utf-8')
 
    return ColumnDataSource(data=Data)


def make_plot(cityData):
    
    hover = HoverTool(
        tooltips=[
            ("GDD", "$y"),
            ("Date", "@dateStr")            
        ]
    )
    TOOLS = [BoxSelectTool(), hover]
    plot = Figure(x_axis_type="datetime", plot_width=1000, tools=TOOLS)
    plot.title = "Accumulated GDD of cities of Canada"
    colors = Spectral11[0:len(cityData)]    
    index = 0
    for src in cityData: 
        plot.line(x='date', y='GDD',source=cityData[src], color=colors[index], line_width=4, legend=src)
        index = index + 1
#    plot.quad(top='max', bottom='min', left='left', right='right', color=colors[2], source=src, legend="Record")

    # fixed attributes
    plot.border_fill_color = "whitesmoke"
    plot.xaxis.axis_label = None
    plot.yaxis.axis_label = "Accumulated GDD"
    plot.axis.major_label_text_font_size = "8pt"
    plot.axis.axis_label_text_font_size = "8pt"
    plot.axis.axis_label_text_font_style = "bold"
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12

    return plot

# set up callbacks
def update_plot(attrname, old, new):
    src = download_data(cities[city_select.value]['ID'], startYear, endYear, baseTemp)
    source.data.update(src.data)

#    source.data.update(cityData[city_select.value].data)
    plot.title = city_select.value



startYear = 2015
endYear = 2015
baseTemp=10
cities = { 
    'Calgary': {'ID':50430},
    'Montreal' : {'ID':51157},
    'St. John\'s' : {'ID':50089}
}
for c in cities.keys():
    cityData[c] = download_data(cities[c]['ID'], startYear, endYear, baseTemp)

    
plot = make_plot(cityData)

# add to document
curdoc().add_root(plot)
