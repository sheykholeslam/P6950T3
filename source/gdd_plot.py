import numpy as np
import matplotlib.pyplot as plt
from extract_data_from_csv import extract_data_from_csv

def gdd_plot(gdd1, gdd2, gdd3, cityName1, cityName2, cityName3):
    plt.subplot(1,1,1)
    X = np.linspace(1, 12, 365, endpoint=True)
    plt.plot(X, gdd1, color="blue", label = cityName1)
    plt.plot(X, gdd2, color="red", label = cityName2)
    plt.plot(X, gdd3, color="green", label = cityName3)
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
    ax.set_ylabel('Cumulative GDD (>10°C)', color='black', fontsize=14)
    plt.title('Accumulated Growing Degree Days', color="black", fontsize=14)
    return plt
    
def Main():
    stationId = [50089,51157,50430]
    cityName = ['St.John\'s', 'Montreal', 'Calgary']
    cityData = []
    for i in range(len(stationId)):
        Data, Date, minTemp, maxTemp = extract_data_from_csv(cityName[i])
        cityData.append(Data['GDD'])
    
    gdd_plt = gdd_plot(cityData[0], cityData[1], cityData[2], cityName[0], cityName[1], cityName[2])
    gdd_plt.savefig("./DataFiles/GDD_Plot.png")

if __name__ == '__main__':
    Main()