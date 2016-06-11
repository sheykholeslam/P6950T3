from os.path import join, dirname
import numpy as np
import pandas as pd
import wget
import os

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DataRange1d, Range1d, VBox, HBox, Select
from bokeh.palettes import Blues4
from bokeh.plotting import Figure
from scipy.signal import savgol_filter

STATISTICS = ['record_min_temp', 'actual_min_temp', 'average_min_temp', 'average_max_temp', 'actual_max_temp', 'record_max_temp']

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
        Data['GDD'] = ((Data['Max Temp (°C)'] + Data['Min Temp (°C)'])/2)- baseTemp
        Data['GDD'] = checkGDD(Data['GDD'])        
        MinTemp, MaxTemp = np.array(Data['Min Temp (°C)']), np.array(Data['Max Temp (°C)'])
        startYear = startYear + 1
		
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
 
    return Data, MinTemp, MaxTemp


def make_plot(source, city):
    plot = Figure(x_axis_type="datetime", plot_width=1000, tools="", toolbar_location=None)
    plot.title = city
    colors = Blues4[0:3]
    
    X = np.linspace(1, 12, 365, endpoint=True)
    plot.line(X, source)
#    plot.quad(top='record_max_temp', bottom='record_min_temp', left='left', right='right', color=colors[2], source=source, legend="Record")
#    plot.quad(top='average_max_temp', bottom='average_min_temp', left='left', right='right', color=colors[1], source=source, legend="Average")
#    plot.quad(top='actual_max_temp', bottom='actual_min_temp', left='left', right='right', color=colors[0], alpha=0.5, line_color="black", source=source, legend="Actual")


    # fixed attributes
    plot.border_fill_color = "whitesmoke"
    plot.xaxis.axis_label = None
    plot.yaxis.axis_label = "Accumulated GDD"
    plot.axis.major_label_text_font_size = "8pt"
    plot.axis.axis_label_text_font_size = "8pt"
    plot.axis.axis_label_text_font_style = "bold"
    plot.x_range = DataRange1d(range_padding=0.0, bounds=None)
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12

    return plot



city = 'St. John\'s'
startYear = 2015
endYear = 2015
baseTemp=10


stationId = [50089,51157,50430]


cities = { 
    'Calgary',
    'Montreal',
    'St. John\'s'
}

cities2 = {
    'Calgary': {
        'ID': '50430'
    },
    'Montreal': {
        'ID': '51157'
    },
    'St. John\'s': {
        'ID': '50089'
    }
}


startYear = 2015
endYear = 2015
baseTemp=10
stationId = [50089,51157,50430]
cityName = ['St. John\'s', 'Montreal', 'Calgary']
cityData = []

city_select = Select(value=city, title='City:', options=cityName)

for i in range(len(stationId)):
    data, minTemp, maxTemp = download_data(stationId[i], startYear, endYear, baseTemp)
    cityData.append(data['GDD'])

plot = make_plot(cityData[0], city)


#source = get_dataset(df, cities[city]['airport'], distribution)
#plot = make_plot(source, cities[city]['title'])

#city_select.on_change('value', update_plot)

# add to document
curdoc().add_root(HBox(city_select, plot))
