s = ./source/

startYear = 2015
endYear = 2015
baseTemp = 10

all : report.pdf

GDD_Data.csv : $(s)download_data.py $(s)calculate_GDD.py
	python3 $(s)download_data.py $(startYear) $(endYear) $(baseTemp)
	
GDD_Plot.png : $(s)extract_data_from_csv.py $(s)gdd_plot.py GDD_Data.csv
	python3 $(s)gdd_plot.py
	
min_max_plot.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py GDD_Data.csv
	python3 $(s)min_max_plot.py
	
report.pdf : $(s)Report/report.tex GDD_Plot.png min_max_plot.png
	pdflatex $(s)Report/report.tex
	pdflatex $(s)Report/report.tex
	
clean : 
	rm -rf *.csv $(s)__pycache__ DataFiles
	rm -f report.log report.aux report.pdf report.toc