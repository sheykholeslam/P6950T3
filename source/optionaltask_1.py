
# coding: utf-8

# In[37]:

import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
from bokeh.plotting import output_file, show
from bokeh.plotting import Figure
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DataRange1d, Range1d, VBox, HBox, Select
from bokeh.palettes import Blues4

def make_plot(source,AverageTemp,Parcentile_5_Min,Parcentile_5_Max,Parcentile_25_Min,Parcentile_25_Max,MinTemp,MaxTemp,plotDate):
    plot = Figure(x_axis_type="datetime", plot_width=1000, tools="", toolbar_location=None)
    plot.title = "GDD"
    colors = Blues4[0:3]
    
    plot.quad(top=Parcentile_5_Max, bottom=Parcentile_5_Min, left='left',right='right',source=source,color="#00ffcc", legend="Percentile 5-95")
    plot.quad(top=Parcentile_25_Max, bottom=Parcentile_25_Min,left='left',right='right',source=source,color="#ffff00",legend="percentile 25-75")
    plot.line(plotDate,AverageTemp,source=source,line_color='Red', line_width=0.5, legend='AverageTemp')
    
    # fixed attributes
    plot.border_fill_color = "whitesmoke"
    plot.xaxis.axis_label = None
    plot.yaxis.axis_label = "Temperature (C)"
    plot.axis.major_label_text_font_size = "8pt"
    plot.axis.axis_label_text_font_size = "8pt"
    plot.axis.axis_label_text_font_style = "bold"
    plot.x_range = DataRange1d(range_padding=0.0, bounds=None)
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12

    return plot


CurrentPath = os.getcwd()
FilePath= (CurrentPath+'/DataFiles/GDD_Data.csv')
Hourly_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = "\t" ,skiprows=0)
Data = pd.DataFrame(Hourly_Data, columns = ['Date/Time','Max Temp (Â°C)', 'Min Temp (Â°C)'])
Data.replace('', np.nan, inplace = True)
Data = Data.dropna()
Date,MinTemp, MaxTemp = np.array(Data['Date/Time']),np.array(Data['Min Temp (Â°C)']), np.array(Data['Max Temp (Â°C)'])

Data['date'] = pd.to_datetime(Date)
Data['left'] = Data.date - pd.DateOffset(days=0.5)
Data['right'] = Data.date + pd.DateOffset(days=0.5)
PlotDate =[]
plotDate = Data['left']
Data = Data.set_index(['date'])
Data.sort_index(inplace=True)
source = ColumnDataSource(data=Data)

AverageTemp = []
for index in range(len(MinTemp)):
    Average=(MinTemp[index]+MaxTemp[index])/2
    AverageTemp.append(Average)

Parcentile_5_Min = []
Parcentile_5_Max = []
Parcentile_25_Min = []
Parcentile_25_Max = []
FivePercent = int(365*.05)
TwentyFivePercent = int(365*.25)
## Delete 5 % lowest From MINTEMP and 5% Highest from MAXTEMP
Parcentile_5_Min = np.delete(MinTemp,MinTemp.argsort()[-FivePercent:])
Parcentile_5_Max = np.delete(MaxTemp,MaxTemp.argsort()[-FivePercent:])
## Delete 25 % lowest From MINTEMP and 25% Highst from MAX TEMP
Parcentile_25_Min = np.delete(MinTemp,MinTemp.argsort()[-TwentyFivePercent:])
Parcentile_25_Max = np.delete(MaxTemp,MaxTemp.argsort()[-TwentyFivePercent:])

plot = make_plot(source,AverageTemp,Parcentile_5_Min,Parcentile_5_Max,Parcentile_25_Min,Parcentile_25_Max,MinTemp,MaxTemp,plotDate)
output_file("GDD.html", title="GDD Example")
show(plot)




# In[ ]:



