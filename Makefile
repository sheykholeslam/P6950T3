all : report.pdf

GDD_Data.csv : ./source/download_data.py ./source/calculate_GDD.py
	python3 ./source/download_data.py 2015 2015 10
	
GDD_Plot.png : ./source/extract_data_from_csv.py GDD_Data.csv
	python3 ./source/gdd_plot.py
	
min_max_plot.png : ./source/extract_data_from_csv.py GDD_Data.csv
	python3 ./source/min_max_plot.py
	
report.pdf : ./source/Report/report.tex GDD_Plot.png min_max_plot.png
	pdflatex ./source/Report/report.tex
	pdflatex ./source/Report/report.tex
	
clean : 
	rm -rf *.csv ./source/__pycache__ DataFiles
	rm -f report.log report.aux report.pdf report.toc