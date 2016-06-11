all : main.o
	
main.o : ./source/min_max_plot.py ./source/gdd_plot.py ./source/checkGDD.py ./source/download_data.py ./source/main.py 
	python3 ./source/main.py
	
report.pdf : ./source/Report/report.tex
	pdflatex ./source/Report/report.tex
	pdflatex ./source/Report/report.tex
	
clean : 
	rm -rf *.csv ./source/__pycache__ DataFiles
	rm -f report.log report.aux report.pdf report.toc