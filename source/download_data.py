import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import argparse
from calculate_GDD import calculate_GDD

def download_data(startYear, endYear, baseTemp, stationId, cityName):
    while (startYear <= endYear):
        url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='+str(stationId)+'&Year='+str(startYear)+'&Month=12&Day=31&timeframe=2&submit= Download+Data'
        filename = wget.download(url)
        hourly_data = pd.read_csv(filename, encoding = 'ISO-8859-1', delimiter = ",", skiprows=25)
        Data = pd.DataFrame(hourly_data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
        Data.replace('', np.nan, inplace = True)
        Data = Data.dropna()
        Data = calculate_GDD(Data, baseTemp)        
        startYear = startYear + 1
		
	# Save Data in Local directory as cvs file
        currentpath = os.getcwd()
        filepath= (currentpath+'/DataFiles/GDD_Data_'+cityName+'.csv')
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
        with open(filepath, 'w') as datafile:
            Data.to_csv(filepath, sep='\t', encoding='utf-8')
 
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("startYear", help="Please insert start year for weather history data.", type=int)
    parser.add_argument("endYear", help="Please insert end year for weather history data.", type=int)
    parser.add_argument("baseTemp", help="Please set base temperature.", type=int)
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
	
    args = parser.parse_args()
	
    for i in range(len(args.stationId)):
        data = download_data(args.startYear, args.endYear, args.baseTemp, args.stationId[i], args.cityName[i])
		
if __name__ == '__main__':
    Main()
