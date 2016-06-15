import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import argparse
import os

import sys
sys.path.append('./source')
from save_data_as_csv import save_data_as_csv
from download_data import download_data


def test_download_data():
    startyear=2015
    endyear=2016
    stationId=50089
    cityName='st.Johns'
        
    download_data(startyear, endyear, stationId, cityName)
    try:
        currentpath = os.getcwd()
        File_Data = pd.read_csv(currentpath+'/DataFiles/GDD_Data_st.Johns.csv')
        #Data = pd.DataFrame(File_Data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
    except:
        raise ValueError("Downloading file is failed!!!")

test_download_data()
