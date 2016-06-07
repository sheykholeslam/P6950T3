from min_max_plot import min_max_plot
from gdd_plot import gdd_plot
from download_data import download_data
 
def Main():
	startYear = 2015
	endYear = 2015
	baseTemp=10
	stationId = [50089,51157,50430]
	cityName = ['St. John\'s', 'Montreal', 'Calgary']
	cityData = []
	for i in range(len(stationId)):
		data, minTemp, maxTemp = download_data(stationId[i], startYear, endYear, baseTemp)
		cityData.append(data['GDD'])
		min_max_plot(minTemp, maxTemp, cityName[i])
		
	gdd_plot(cityData[0], cityData[1], cityData[2], cityName[0], cityName[1], cityName[2])
	
if __name__ == '__main__':
	Main()