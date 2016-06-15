import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
from extract_data_from_csv import extract_data_from_csv

T_baseList=[10,11,12,13,14,15]

def checkGDD(values):
    gdd = []
    item = 0
    for i in values:
        if i >= 0:
            item += i
        gdd.append(item)
    return gdd

def gdd_Tbase(i):
    CurrentPath = os.getcwd()
    FilePath= (CurrentPath+'/DataFiles/GDD_Data_St_Johns.csv')
    Data, Date, MaxTemp, MinTemp = extract_data_from_csv(FilePath) 
    Data['GDD'+str(i)]=(Data['Max Temp (ÃÂ°C)']+Data['Min Temp (ÃÂ°C)'])/2-T_baseList[i]
    Data['GDD'+str(i)]=checkGDD(Data['GDD'+str(i)])
    gddt=Data['GDD'+str(i)]
    #print(gddt)
    gddt=np.array(gddt)
    return gddt

def Main():
    color=iter(cm.rainbow(np.linspace(0,1,len(T_baseList))))
    plt.subplot(1,1,1)
    X = np.linspace(1, 12, 365, endpoint=True)
    for i in range(len(T_baseList)):
        c=next(color)
        plt.plot(X, gdd_Tbase(i),c=c,label ='T_base = '+str(T_baseList[i]))
    plt.legend(loc='upper left')
    ax = plt.gca() 
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(8)
            label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

    ax.set_xlabel('Months', color='black', fontsize=14)
    ax.set_ylabel('Cumulative GDD on different T_bases', color='black', fontsize=14)
    plt.title("Accumulated Growing Degree Days in St.John's", color="black", fontsize=14)
    plt.savefig("./Plots/Op3.png")
    
if __name__ == '__main__':
    Main()