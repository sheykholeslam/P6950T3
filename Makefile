s = ./source/

# Input variables and their values
startYear = 2015
endYear = 2015
baseTemp = 10
stationId = -st 50089 51157 50430
cityName = -ct 'St.Johns' 'Montreal' 'Calgary'
gColor = -gc 'blue' 'red' 'green'

all : report.pdf

GDD_Data.csv : $(s)download_data.py $(s)calculate_GDD.py
	python3 $(s)download_data.py $(startYear) $(endYear) $(baseTemp) $(stationId) $(cityName) 
	
GDD_Plot.png : $(s)extract_data_from_csv.py $(s)gdd_plot.py GDD_Data.csv
	python3 $(s)gdd_plot.py $(stationId) $(cityName) $(gColor)
	
min_max_plot.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py GDD_Data.csv
	python3 $(s)min_max_plot.py $(stationId) $(cityName)
	
report.pdf : $(s)Report/report.tex min_max_plot.png GDD_Plot.png
	pdflatex $(s)Report/report.tex
	pdflatex $(s)Report/report.tex
	
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
