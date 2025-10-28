# import modules
import tkinter
from tkinter import filedialog
from tkinter import messagebox
import tkinter.simpledialog
import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# define variables
data_list = []
xticks_num = []
filename_list = []
var_list = ["data1","data2","data3","data4","data5","data6","data7","data8","data9","data10","data11","data12","data13",]
backcolor = "#000000"
labelcolor = "#FFFFFF"
gridcolor = "#1F1F1F"

#select csv files with filedialog
fle = list(filedialog.askopenfilenames(filetypes=[('csv file','.csv')]))
if len(fle) == 0:
    messagebox.showerror('Error', 'CSV file not selected, exit.')
    exit()
elif len(fle) > 13:
    messagebox.showerror('Error', 'too many CSV files please use less than 14, exit.')
    exit()

# aggregate all csv data
for i in range(len(fle)):
    xticks_num.append(i)
    filename_list.append(os.path.splitext(os.path.basename(fle[i]))[0])
    var_name = var_list[i]
    globals()[var_name] = pd.read_csv(fle[i],names=['Latency'])
    exec("{}['filename'] = '{}'".format(var_name,os.path.splitext(os.path.basename(fle[i]))[0]))
    exec("data_list.append({})".format(var_name))

# user input for GraphTitle
GraphTitle = tkinter.simpledialog.askstring("Enter Graph Title", "Enter Graph Title")
if isinstance(GraphTitle,str)==False:
    GraphTitle = ""

# user input for TestSetup
TestSetup = tkinter.simpledialog.askstring("Enter your setup", "Enter your setup(ex CPU,GPU,monitor,OS,etc)")
if isinstance(TestSetup,str)==False:
    TestSetup = ""

# user input for TestInfo
TestInfo = tkinter.simpledialog.askstring("Enter test info", "Enter additional test info")
if isinstance(TestInfo,str)==False:
    TestInfo = ""

# custom figure color,create figure
sb.set(rc={'axes.facecolor':backcolor, 'figure.facecolor':backcolor, 'grid.color': gridcolor})
height = 2.8+(6.2*len(fle))
fig, ax = plt.subplots(1, 1, figsize=(16, height))
n_top = (height-1.3)/(height)
n_bottom = 1/height
fig.subplots_adjust(top=n_top, bottom=n_bottom)

# create plot
for i in range(len(fle)):
    plot = sb.violinplot(data=data_list[i], x='Latency', y='filename', label=filename_list[i], inner='quart', cut=0, saturation=1, alpha=None, edgecolor=sb.color_palette("tab10")[i]+(1,), dodge=False, legend=False, split=True, color=sb.color_palette("tab10")[i]+(0.249,))

# custom figure title and ticks and label,spines
suptitle_y = (height-0.18)/height
if GraphTitle!="":
    fig.suptitle(GraphTitle,size=30,color=labelcolor,y=suptitle_y)
plt.xticks(color=labelcolor)
plt.yticks(color=labelcolor)
if TestSetup != "" and TestInfo != "":
    plt.title("test setup : "+TestSetup+"\ntestinfo : "+TestInfo,color=labelcolor,size=9,pad=20)
elif TestSetup == "" and TestInfo != "":
    plt.title("testinfo : "+TestInfo,color=labelcolor,size=15,pad=20)
elif TestSetup != "" and TestInfo == "":
    plt.title("test setup : "+TestSetup,color=labelcolor,size=15,pad=20)
for b in ['top', 'bottom', 'left', 'right']:
    ax.spines[b].set_linewidth(0)
ax.set(xlabel="input latency [ms]")
ax.xaxis.label.set_color(labelcolor)
ax.yaxis.label.set_color(backcolor)

# save figure as figure.png with high resolution
dir_path = os.path.dirname(os.path.realpath(__file__))
if os.path.isdir(dir_path+"\\outputs")==False:
    os.mkdir(dir_path+"\\outputs")
if GraphTitle=="":
    for i in range(1000):
        if os.path.isfile(dir_path+"\\outputs\\"+"violinplot_KDElike_inde_"+str(i).zfill(4)+".png")==False:
            plt.savefig(dir_path+"\\outputs\\"+"violinplot_KDElike_inde_"+str(i).zfill(4)+".png", dpi=120)
            break
else:
    for i in range(1000):
        if os.path.isfile(dir_path+"\\outputs\\"+GraphTitle+"_violinplot_KDElike_inde_"+str(i).zfill(4)+".png")==False:
            plt.savefig(dir_path+"\\outputs\\"+GraphTitle+"_violinplot_KDElike_inde_"+str(i).zfill(4)+".png", dpi=120)
            break