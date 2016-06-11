all : Main.o
	
Main.o : ./source/min_max_plot.py ./source/gdd_plot.py ./source/checkGDD.py ./source/download_data.py ./source/Main.py 
	python3 ./source/Main.py
	
Report.pdf : ./source/Report/Report.tex
	pdflatex ./source/Report/Report.tex
	pdflatex ./source/Report/Report.tex
	#bibtex report
	pdflatex ./source/Report/Report.tex
	
clean : 
	rm -rf *.csv ./source/__pycache__ DataFiles
	rm -f Report.log Report.aux Report.pdf