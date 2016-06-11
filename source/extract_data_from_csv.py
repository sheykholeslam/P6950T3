import numpy as np
import pandas as pd
import os

def extract_data_from_csv(cityName):
    CurrentPath = os.getcwd()
    FilePath= (CurrentPath+'/DataFiles/GDD_Data_'+cityName+'.csv')
    Hourly_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = "\t" ,skiprows=0)
    Data = pd.DataFrame(Hourly_Data, columns = ['Date/Time','Max Temp (Â°C)', 'Min Temp (Â°C)', 'GDD'])
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    Date, minTemp, maxTemp = np.array(Data['Date/Time']),np.array(Data['Min Temp (Â°C)']), np.array(Data['Max Temp (Â°C)'])
    
    return Data, Date, minTemp, maxTemp



 
