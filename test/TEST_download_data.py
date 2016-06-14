
# coding: utf-8

# In[8]:

import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import argparse
import os

def save_data_as_csv(Data, filepath):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
    with open(filepath, 'w') as datafile:
        Data.to_csv(filepath, sep=',', encoding='utf-8')

def download_data(startYear, endYear, stationId, cityName):
    while (startYear <= endYear):
        url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='+str(stationId)+'&Year='+str(startYear)+'&Month=12&Day=31&timeframe=2&submit= Download+Data'
        filename = wget.download(url)
        File_Data = pd.read_csv(filename, encoding = 'ISO-8859-1', delimiter = ',', skiprows=25)
        Data = pd.DataFrame(File_Data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
        Data.replace('', np.nan, inplace = True)
        Data = Data.dropna()       
        startYear = startYear + 1
        currentpath = os.getcwd()
        filepath= (currentpath+'/DataFiles/GDD_Data_'+cityName+'.csv')
        save_data_as_csv(Data, filepath)
        os.remove(filename)
download_data(2015, 2016, 50089, 'st. Johns' )


# In[ ]:




# In[11]:

def test_download_data():
    startyear=2015
    endyear=2016
    stationId=50089
    cityName='st.Johns'
        
    download_data(startyear, endyear, stationId, cityName)
    try:
        currentpath = os.getcwd()
        File_Data = pd.read_csv(currentpath+'/DataFiles/GDD_Data_st.Johns.csv')
        print ("File is downloaded")
        #Data = pd.DataFrame(File_Data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
    except:
        raise ValueError("Jupiter is not where it should be!")

test_download_data()


# In[ ]:



