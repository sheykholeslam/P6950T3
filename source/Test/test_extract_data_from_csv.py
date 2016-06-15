import numpy as np
import pandas as pd
import os

import sys
sys.path.append('./source')

from extract_data_from_csv import extract_data_from_csv

def test_extract_data_from_csv():
        
    cityName = 'St_Johns'
    #currentpath = os.getcwd()
    currentpath='/home/mehrzad/workspace/P6950T3'
    FilePath= ('./DataFiles/GDD_Data_'+cityName+'.csv')
    a, b, c, d= extract_data_from_csv(FilePath)

    File_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = ',' ,skiprows=0)
    Data = pd.DataFrame(File_Data)
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    Index = Data.keys()
    Date, maxTemp, minTemp = np.array(Data[Index[1]]),np.array(Data[Index[2]]), np.array(Data[Index[3]])
    
    if b.all() != Date.all() or c.all() != maxTemp.all() or d.all() != minTemp.all():
        raise ValueError("Data is not extracted correctly.")     
       
test_extract_data_from_csv()
