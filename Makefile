All : Main.o
	
Main.o : ./source/min_max_plot.py ./source/gdd_plot.py ./source/checkGDD.py ./source/download_data.py ./source/Main.py 
	python3 ./source/Main.py
	
clear : 
	rm -rf *.csv ./source/__pycache__