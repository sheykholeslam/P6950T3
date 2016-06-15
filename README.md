CMSC6950 - Group # 3 (Growing degree-day)
=========================================
This is an extended assignment for the course CMSC6950. Our group formation is given below:

1. Mohammad Hassan - mmh474@mun.ca
2. Ernest - esaw83@mun.ca
3. Mehrzad - smalmasi@mun.ca
4. Yin Zhang - yz2416@mun.ca
5. Rufai Raji - orr612@mun.ca
6. Lutfor Rahman - r97mlr@mun.ca
7. Mohammad Sheykholeslam - mhs137@mun.ca

Dependencies:
-------------
- <b>Python</b>
- <b>Python Packages:</b> numpy, pandas, scipy, argparse, math, matplotlib, bokeh, os, wget. 
- <b>Bash</b>
- <b>Bokeh library</b>

Requirements:
-------------
- <b>Platform :</b> Mac OS X, Ubuntu, Debian, Red Hat, Fedora.

Program Execute:
----------------

##### Clone GitHub Repository:

```bash
# Make a clone of the repository in a local directory
$ git clone https://github.com/sheykholeslam/P6950T3.git
```

##### Run:

```bash
# To call the Makefile and execute all.
$ make

# To removing all the downloaded data and complied files.
$ make clean

# To run the test case. If there is no reply, that means success.  
$ make test

# To generate files by file name (Ex. report.pdf). 
$ make report.pdf
```

Project Requirements and Tasks:
----------------
<b>Link :</b> [Click Here](https://github.com/sheykholeslam/P6950T3/blob/master/Project_Requirements.md)

Web-based Presentation:
----------------
<b>Link :</b> [Click Here](https://sheykholeslam.github.io/P6950T3/)


Contents:
----------
 
<table>
<th colspan="2" align=left>Base Files</th>
<tr><td>Makefile</td><td>Makefile for this project.</td></tr>
<tr><td>Project_Requirements.md</td><td>Requirement for this project given by Professor.</td></tr>
<tr><td>README.md</td><td>Instructions for source code usage.</td></tr>
<th colspan="2" align=left>Source Files</th>
<tr><td>calculate_GDD.py</td><td>Function to calculate GDD from a given data.</td></tr>
<tr><td>download_data.py</td><td>Download the historical weather data from web.</td></tr>
<tr><td>save_data_as_csv.py</td><td>Save the downloaded/modified data into CSV format.</td></tr>
<tr><td>extract_data_from_csv.py</td><td>Extract the data from downloaded CSV files.</td></tr>
<tr><td>gdd_plot.py</td><td>Plot the cumulative GDD for multiple cities.</td></tr>
<tr><td>min_max_plot.py</td><td>Min-Max temperature plot for different cities.</td></tr>
<tr><td>opTask1.py</td><td>Optional Task # 1.</td></tr>
<tr><td>opTask3.py</td><td>Optional Task # 3.</td></tr>
<tr><td>opTask4.py</td><td>Optional Task # 4.</td></tr>
<tr><td>opTask5.py</td><td>Optional Task # 5.</td></tr>
<tr><td>report.tex</td><td>LaTeX source file for the report.</td></tr>
<tr><td>gh-pages/index.html</td><td>Web based presentation source code.</td></tr>
<th colspan="2" align=left>Data Files</th>
<tr><td>report.pdf</td><td>Function to calculate GDD from a given data.</td></tr>
<tr><td>GDD_Data.csv</td><td>Downloaded CSV data file.</td></tr>
</table> 
