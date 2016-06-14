from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json
from bokeh.sampledata.olympics2014 import data
from bokeh.charts import Bar, output_file, show
import csv
import os
import numpy as np
import pandas as pd

CurrentPath = os.getcwd()
FilePath= (CurrentPath+'/DataFiles/GDD_Data.csv')
Hourly_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = "\t" ,skiprows=0)
Data = pd.DataFrame(Hourly_Data)
Data.replace('', np.nan, inplace = True)
Data = Data.dropna()
Index = Data.keys()
Date, MinTemp, MaxTemp, GDD = np.array(Data[Index[0]]),np.array(Data[Index[1]]), np.array(Data[Index[2]]), np.array(Data[Index[5]])
Data['group'] = Data['GDD'].map(lambda x:1 if x > 106 and x<=550 else 0)
Data['month'] = pd.DatetimeIndex(Data['date']).month

## Reference
## http://store.msuextension.org/publications/AgandNaturalResources/MT200103AG.pdf
## GDD For BARLEY, WHEAT AND CANARY_SEED
## The GDD of BARLEY 'Emergence':109-145,'Leaf_development':145-184,'Tillering':308-360,'Stem_elongation':489-555

p = Bar(Data,label='month', values='GDD',agg='median', group='group',
        title="GDD of Stem_elongation of Barley", legend='top_right')

output_file("bar.html")
show(p)
