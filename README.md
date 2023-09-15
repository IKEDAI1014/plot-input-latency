# plot-input-latency
 Script to graph input latency data

## Contents
- [violinplot.py](violinplot.py) -> Script to graph input latency data with violinplot  
![preview_violinplot](preview_violinplot.png)
- [histgraph_step.py](histgraph_step.py) -> Script to graph input latency data with histgraph in step mode  
![preview_step](preview_histgraph_step.png)
- [histgraph_poly.py](histgraph_poly.py) -> Script to graph input latency data with histgraph in poly mode  
![preview_poly](preview_histgraph_poly.png)

## requisite
- csv file containing data on input latency with no headers and units, separated by line feeds
- python3.8+
- pandas module
- seaborn module
- tkinter module
- matplotlib module
- os module

## Usage
1. install python 3.8+.
2. Install the module written above using `pip install ***`.
3. run plot.py and select csv files.
4. Enter GraphTitle and TestSetup,TestInfo.(ex "RawInput ON vs OFF" and "10900KF, 4000MHz16-17-17-35, 2080Ti" , "1000Try Each, DX12".
5. plot.png is in the same folder as plot.py.