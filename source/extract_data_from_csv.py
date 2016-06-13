import numpy as np
import pandas as pd
import os

def extract_data_from_csv(FilePath):
    File_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = ',' ,skiprows=0)
    Data = pd.DataFrame(File_Data)
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    Index = Data.keys()
    Date, minTemp, maxTemp = np.array(Data[Index[1]]),np.array(Data[Index[2]]), np.array(Data[Index[3]])
    
    return Data, Date, minTemp, maxTemp



 
