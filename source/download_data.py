import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
from checkGDD import checkGDD

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
	## Save Data in Local directory as cvs file
        currentpath = os.getcwd()
        filepath= (currentpath+'/Desktop/download_data/data.csv')
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
