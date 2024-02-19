# import modules
import tkinter
from tkinter import filedialog
import tkinter.simpledialog
import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# define variables
data_list = []
mergeddataset = []
filename_list = []
var_list = ["data1","data2","data3","data4","data5","data6","data7","data8","data9","data10","data11","data12","data13",]
backcolor = "#000000"
labelcolor = "#FFFFFF"
gridcolor = "#1F1F1F"
plotcolor = ["#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#BFBFBF","#7F7F7F","#7F0000","#7F7F00","#007F00","#7F007F","#007F7F"]

#select csv files with filedialog
fle = list(filedialog.askopenfilenames(filetypes=[('csv file','.csv')]))

# aggregate all csv data
for i in range(len(fle)):
    var_name = var_list[i]
    globals()[var_name] = pd.read_csv(fle[i],names=['Latency'])
    exec("{}['testname'] = '{}'".format(var_name,os.path.splitext(os.path.basename(fle[i]))[0]))
    exec("data_list.append({})".format(var_name))
mergedataset = pd.concat(data_list)

# user input for GraphTitle
GraphTitle = tkinter.simpledialog.askstring("Enter Graph Title", "Enter Graph Title")

# user input for TestSetup
TestSetup = tkinter.simpledialog.askstring("Enter your setup", "Enter your setup(ex CPU,GPU,monitor,OS,etc)")

# user input for TestInfo
TestInfo = tkinter.simpledialog.askstring("Enter test info", "Enter additional test info")

# custom figure color,create figure
sb.set(rc={'axes.facecolor':backcolor, 'figure.facecolor':backcolor, 'grid.color': gridcolor})
fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(111)

# create plot
plot = sb.histplot(data=mergedataset, x='Latency', hue='testname', bins=20, element="step", legend=True)
plot.legend_.set_title('')
for text in plot.legend_.get_texts():
    text.set_color(labelcolor)

# custom figure title and ticks and label,spines
fig.suptitle(GraphTitle,y=0.98,size=30,color=labelcolor)
plt.xticks(color=labelcolor)
plt.yticks(color=backcolor)
ax.set_title("test setup : "+TestSetup+"\ntestinfo : "+TestInfo,color=labelcolor,size=9)
for b in ['top', 'bottom', 'left', 'right']:
    ax.spines[b].set_linewidth(0)
ax.set(xlabel="input latency [ms]")
ax.yaxis.label.set_color(backcolor)
ax.xaxis.label.set_color(labelcolor)

# save figure as figure.png with high resolution
dir_path = os.path.dirname(os.path.realpath(__file__))
plt.savefig(dir_path+"\\"+GraphTitle+"_histgraph_step.png", dpi=120)