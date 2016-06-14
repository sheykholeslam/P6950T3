
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd
import os

import sys
sys.path.append('/home/mehrzad/workspace/P6950T3/source')

from extract_data_from_csv import extract_data_from_csv


# In[32]:

def test_extract_data_from_csv():
        
    cityName = 'st. Johns'
    #currentpath = os.getcwd()
    currentpath='/home/mehrzad/workspace/P6950T3'
    FilePath= (currentpath+'/DataFiles/GDD_Data_'+cityName+'.csv')
    a, b, c, d= extract_data_from_csv(FilePath)

    File_Data = pd.read_csv(currentpath+'/DataFiles/GDD_Data_st. Johns.csv', encoding = 'ISO-8859-1', delimiter = ',' ,skiprows=0)
    Data = pd.DataFrame(File_Data)
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    Index = Data.keys()
    Date, maxTemp, minTemp = np.array(Data[Index[1]]),np.array(Data[Index[2]]), np.array(Data[Index[3]])
    
    try: 
        if b.all() == Date.all() and c.all() == maxTemp.all() and d.all() == minTemp.all():
	    print ('**** Data is extracted correctly ****')
    except:
            print('**** Data is not extracted correctly ****')
            
test_extract_data_from_csv()



