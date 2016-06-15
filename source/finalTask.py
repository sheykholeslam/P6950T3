from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json
from bokeh.sampledata.olympics2014 import data
from bokeh.charts import Bar, output_file, show
import csv
import os
import numpy as np
import pandas as pd

## Reference
## http://store.msuextension.org/publications/AgandNaturalResources/MT200103AG.pdf
## GDD For BARLEY,
## The GDD of BARLEY 'Emergence':109-145,'Leaf_development':146-184,'Tillering':185-360,'Stem_elongation':489-555

def getGroup(GDD):
    group = []
    for i in GDD:
        if( i >= 109 and i <= 145):
            group.append('Emergence')
        elif ( i >= 146 and i <= 184):
            group.append('Leaf_development')
        elif ( i >= 185 and i <= 360):
            group.append('Tillering')
        elif ( i >= 361 and i <= 555):
            group.append('Stem_elongation')
        elif ( i >= 556 and i <= 936):
            group.append('Anthesis')
        elif ( i >= 937 and i <= 1145):
            group.append('Seed_fill')
        elif ( i >= 1146 and i <= 1438):
            group.append('Dough_stage')
        elif ( i >= 1439 and i <= 1522):
            group.append('Maturity_complete')
        else:
            group.append('No Growth')

    return group

CurrentPath = os.getcwd()
FilePath= (CurrentPath+'/DataFiles/GDD_Data.csv')
Hourly_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = "\t" ,skiprows=0)
Data = pd.DataFrame(Hourly_Data)
Data.replace('', np.nan, inplace = True)
Data = Data.dropna()
Index = Data.keys()
Date, MinTemp, MaxTemp, GDD = np.array(Data[Index[0]]),np.array(Data[Index[1]]), np.array(Data[Index[2]]), np.array(Data[Index[5]])
Data['group'] = getGroup(Data[Index[5]])
Data['month'] = pd.DatetimeIndex(Data['date']).month


p = Bar(Data,label='month', values='GDD',agg='median', group='group',
        title="GDD of Barley In Bar", legend='top_left')

output_file("GDDVisualization.html")
show(p)
