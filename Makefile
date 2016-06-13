# Source folder path from root directory
s = ./source/
r = ./source/Report/
d = ./DataFiles/
p = ./Plots/

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
	
$(p)GDD_Plot.png : $(s)extract_data_from_csv.py $(s)gdd_plot.py $(d)GDD_Data_St.Johns.csv $(d)GDD_Data_Montreal.csv $(d)GDD_Data_Calgary.csv
	mkdir -p Plots
	python3 $(s)gdd_plot.py $(stationId) $(cityName) $(gColor)
	
$(p)min_max_plot_St.Johns.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_St.Johns.csv
	mkdir -p Plots
	python3 $(s)min_max_plot.py $(stationId) $(cityName)
	
$(p)min_max_plot_Montreal.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_Montreal.csv
	mkdir -p Plots
	python3 $(s)min_max_plot.py $(stationId) $(cityName)

$(p)min_max_plot_Calgary.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_Calgary.csv
	mkdir -p Plots
	python3 $(s)min_max_plot.py $(stationId) $(cityName)

$(p)Op1_St.Johns.html : $(s)extract_data_from_csv.py $(s)opTask1.py $(d)GDD_Data_St.Johns.csv
	mkdir -p Plots
	python3 $(s)opTask1.py $(stationId) $(cityName)
	
$(p)Op1_Montreal.html : $(s)extract_data_from_csv.py $(s)opTask1.py $(d)GDD_Data_Montreal.csv
	mkdir -p Plots
	python3 $(s)opTask1.py $(stationId) $(cityName)
	
$(p)Op1_Calgary.html : $(s)extract_data_from_csv.py $(s)opTask1.py $(d)GDD_Data_Calgary.csv
	mkdir -p Plots
	python3 $(s)opTask1.py $(stationId) $(cityName)

$(p)Op4.html : $(s)extract_data_from_csv.py $(s)opTask4.py $(d)GDD_Data_Calgary.csv $(d)GDD_Data_Montreal.csv $(d)GDD_Data_St.Johns.csv
	mkdir -p Plots
	python3 $(s)opTask4.py $(stationId) $(cityName)
	
report.pdf : $(r)report.tex $(p)GDD_Plot.png $(p)min_max_plot_St.Johns.png $(p)min_max_plot_Montreal.png $(p)min_max_plot_Calgary.png $(p)Op1_St.Johns.html $(p)Op1_Montreal.html $(p)Op1_Calgary.html $(p)Op4.html
	pdflatex $(r)report.tex
	pdflatex $(r)report.tex
	
clean : 
	rm -rf *.csv $(s)__pycache__ DataFiles Plots
	rm -f report.log report.aux report.pdf report.toc

help:
	@echo "Please make sure you have installed pdflatex program.
	@echo "# Calling the Makefile"
	@echo "$ make"
	@echo "# Clean the complied and data files"
	@echo "#$ make clean"
	@echo "# Calling by file name"
	@echo "#$ make report.pdf"
