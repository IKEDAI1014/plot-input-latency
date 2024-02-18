# import modules
import tkinter
from tkinter import filedialog
import tkinter.simpledialog
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# define variables
data_list = []
mergeddataset = []
filename_list = []
var_list = ["data1","data2","data3","data4","data5","data6","data7","data8","data9","data10","data11","data12","data13",]
backcolor = "#000000"
labelcolor = "#FFFFFF"
gridcolor = "#1F1F1F"
plotcolor = ["#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#BFBFBF","#7F7F7F","#7F0000","#7F7F00","#007F00","#7F007F","#007F7F"]

# select csv files with filedialog
fle = list(filedialog.askopenfilenames(filetypes=[('csv file','.csv')]))

# aggregate all csv data
for i in range(len(fle)):
    filename_list.append(os.path.basename(fle[i]))
    var_name = var_list[i]
    globals()[var_name] = pd.read_csv(fle[i],names=['Latency'])
    exec("data_list.append({})".format(var_name))

# user input for GraphTitle
GraphTitle = tkinter.simpledialog.askstring("Enter Graph Title", "Enter Graph Title")

# user input for TestSetup
TestSetup = tkinter.simpledialog.askstring("Enter your setup", "Enter your setup(ex CPU,GPU,monitor,OS,etc)")

# user input for TestInfo
TestInfo = tkinter.simpledialog.askstring("Enter test info", "Enter additional test info")

# custom figure color,create figure
sb.set(rc={'axes.facecolor':backcolor, 'figure.facecolor':backcolor, 'grid.color': gridcolor})
fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)

# create plot
for i in range(len(fle)):
    sb.kdeplot(data=data_list[i], x='Latency', label=filename_list[i])
plt.legend(labelcolor=labelcolor)

# custom figure title and ticks and label,spines
fig.suptitle(GraphTitle,y=0.98,size=30,color=labelcolor)
plt.xticks(color=labelcolor)
plt.yticks(color=backcolor)
ax.set_title("test setup : "+TestSetup+"\ntestinfo : "+TestInfo,color=labelcolor,size=9)
for b in ['top', 'bottom', 'left', 'right']:
    ax.spines[b].set_linewidth(0)
ax.set(ylabel="input latency [ms]")
ax.yaxis.label.set_color(backcolor)
ax.xaxis.label.set_color(labelcolor)

# save figure as figure.png with high resolution
dir_path = os.path.dirname(os.path.realpath(__file__))
plt.savefig(dir_path+"\\"+GraphTitle+"_kdeplot.png", dpi=200)