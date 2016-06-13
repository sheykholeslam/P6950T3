# Source folder path from root directory
s = ./source/
r = ./source/Report/
d = ./DataFiles/

# Input variables and their values
startYear = 2015
endYear = 2015
baseTemp = 10
# Provide list of Station ID and City Name here for GDD Calculation
stationId = -st 50089 51157 50430
cityName = -ct 'St.Johns' 'Montreal' 'Calgary'
# Define the seperate plot line color for each city. 
gColor = -gc 'blue' 'red' 'green'


all : report.pdf

$(d)GDD_Data_St.Johns.csv : $(s)download_data.py $(s)calculate_GDD.py
	python3 $(s)download_data.py $(startYear) $(endYear) $(stationId) $(cityName) 
	python3 $(s)calculate_GDD.py $(baseTemp) $(stationId) $(cityName)
	
$(d)GDD_Data_Montreal.csv : $(s)download_data.py $(s)calculate_GDD.py
	python3 $(s)download_data.py $(startYear) $(endYear) $(stationId) $(cityName)
	python3 $(s)calculate_GDD.py $(baseTemp) $(stationId) $(cityName)	

$(d)GDD_Data_Calgary.csv : $(s)download_data.py $(s)calculate_GDD.py
	python3 $(s)download_data.py $(startYear) $(endYear) $(stationId) $(cityName) 
	python3 $(s)calculate_GDD.py $(baseTemp) $(stationId) $(cityName)
	
$(d)GDD_Plot.png : $(s)extract_data_from_csv.py $(s)gdd_plot.py $(d)GDD_Data_St.Johns.csv $(d)GDD_Data_Montreal.csv $(d)GDD_Data_Calgary.csv
	python3 $(s)gdd_plot.py $(stationId) $(cityName) $(gColor)
	
$(d)min_max_plot_St.Johns.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_St.Johns.csv
	python3 $(s)min_max_plot.py $(stationId) $(cityName)
	
$(d)min_max_plot_Montreal.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_Montreal.csv
	python3 $(s)min_max_plot.py $(stationId) $(cityName)

$(d)min_max_plot_Calgary.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_Calgary.csv
	python3 $(s)min_max_plot.py $(stationId) $(cityName)

$(d)Op1.html : $(s)extract_data_from_csv.py $(s)optionaltask_1.py $(d)GDD_Data_St.Johns.csv $(d)GDD_Data_Montreal.csv $(d)GDD_Data_Calgary.csv
	python3 $(s)optionaltask_1.py
	
report.pdf : $(r)report.tex $(d)GDD_Plot.png $(d)min_max_plot_St.Johns.png $(d)min_max_plot_Montreal.png $(d)min_max_plot_Calgary.png $(d)Op1.html
	pdflatex $(r)report.tex
	pdflatex $(r)report.tex
	
clean : 
	rm -rf *.csv $(s)__pycache__ DataFiles
	rm -f report.log report.aux report.pdf report.toc

help:
	@echo "Please make sure you have installed pdflatex program.
	@echo "# Calling the Makefile"
	@echo "$ make"
	@echo "# Clean the complied and data files"
	@echo "#$ make clean"
	@echo "# Calling by file name"
	@echo "#$ make report.pdf"
