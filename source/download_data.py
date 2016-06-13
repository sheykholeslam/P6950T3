import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import argparse
from save_data_as_csv import save_data_as_csv

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
 
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("startYear", help="Please insert start year for weather history data.", type=int)
    parser.add_argument("endYear", help="Please insert end year for weather history data.", type=int)
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
	
    args = parser.parse_args()
	
    for i in range(len(args.stationId)):
        download_data(args.startYear, args.endYear, args.stationId[i], args.cityName[i])
		
if __name__ == '__main__':
    Main()
