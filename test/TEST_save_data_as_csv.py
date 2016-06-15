
# coding: utf-8


# In[22]:

import wget
import os
import pandas as pd

import sys
sys.path.append('./source')

from save_data_as_csv import save_data_as_csv


def Test_save_data_as_csv():
    
    currentpath=os.getcwd()
    f_path=currentpath+'/DataFiles_Test/st.Johns_Test_Function.csv'
    
    #File_Data = pd.read_csv('/home/mehrzad/workspace/P6950T3/DataFiles_Test/GDD_Data_st.Johns.csv')
    filename = wget.download('http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50089&Year=2015&Month=12&Day=31&timeframe=2&submit= Download+Data')
    File_Data = pd.read_csv(filename, encoding = 'ISO-8859-1', delimiter = ',', skiprows=25)
    
    save_data_as_csv(File_Data, f_path)
    
    if os.path.exists(f_path):
        print('\n\n*****************************************')
        print('*****************************************\n')
        print('\nData is saved in the Given path correctly\n')
        print('\n*****************************************')
        print('*****************************************\n\n')
    else:
        print('\n***********************************************\n')
        print('\nThere is a problem in saving file at given path\n')
        print('\n***********************************************\n')
        
Test_save_data_as_csv()



