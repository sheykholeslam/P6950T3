import wget
import numpy as np
import pandas as pd
import time as time
import math
from checkGDD import checkGDD

def download_data(stationid, start, end, baseTemp, smonth):
    while (start<=end):
        url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='+str(stationid)+'&Year='+str(start)+'&Month='+str(smonth)+'&Day=31&timeframe=2&submit= Download+Data'
        filename=wget.download(url)
        hourly_data=pd.read_csv(filename,encoding='ISO-8859-1',delimiter=",", skiprows=25)
        df = pd.DataFrame(hourly_data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
        df.replace('', np.nan, inplace=True)
        df2 = df.dropna()
        df2['GDD']  = ((df2['Max Temp (°C)']+df2['Min Temp (°C)'])/2)- baseTemp
        df2['GDD'] = checkGDD(df2['GDD'])        
        A, B = np.array(df2['Min Temp (°C)']), np.array(df2['Max Temp (°C)'])
        start=start+1 
    return df2, A, B
