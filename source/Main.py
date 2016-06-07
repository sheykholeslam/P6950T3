from min_max_plot import min_max_plot
from gdd_plot import gdd_plot
from download_data import download_data
 
def Main():
	start=2015
	end=2015
	baseTemp=10
	smonth=12

	stationid=50089
	cityName1 = 'St. John\'s'
	dataA, A1, B1 = download_data(stationid, start, end, baseTemp, smonth)
	stationid=51157
	cityName2 = 'Montreal'
	dataB, A2, B2 = download_data(stationid, start, end, baseTemp, smonth)
	stationid=50430
	cityName3 = 'Calgary'
	dataC, A3, B3 = download_data(stationid, start, end, baseTemp, smonth)

	min_max_plot(A1, B1, cityName1)
	min_max_plot(A2, B2, cityName2)
	min_max_plot(A3, B3, cityName3)

	gdd_plot(dataA['GDD'], dataB['GDD'], dataC['GDD'], cityName1, cityName2, cityName3)
	
if __name__ == '__main__':
	Main()