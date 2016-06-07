import wget
import numpy as np
import pandas as pd
import time as time
import math
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
    return Data, MinTemp, MaxTemp
