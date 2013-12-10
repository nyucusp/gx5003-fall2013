import matplotlib.pyplot as plt
from datetime import date
import numpy as np

data = open('stocks.dat','r') #open file

mon = []
app = []
mic  = []
for line in data:
    split_data = line.split(',')
    mon.append(split_data[0])
    app.append(split_data[1])
    mic.append(split_data[2])

del mon[0]
del app[0]
del mic[0]

dates = []
for element in mon:
    yr = int(element.split('-')[0])
    mn = int(element.split('-')[1])
    new_date = date(int(yr),int(mn),1)
    dates.append(new_date)

fig, ax = plt.subplots()
ax.plot(dates, app, 'o-', label='Apple')
ax.plot(dates, mic, 'o-', label='Microsoft')
fig.autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Stock')
plt.title("Apple vs Microsoft")

#Limits
ax.set_ylim(0,200)
ax.yaxis.set_ticks(np.arange(0, 200, 20))
datemin = date(2005, 12, 1)#Limits of minimum date
datemax = date(2008, 10, 1)#Limits of maximum date
ax.set_xlim(datemin, datemax)
plt.grid(which = 'both', color = '0.90', linestyle = '-')

#Subtitle (Apple & Microsoft()
legend = ax.legend(loc='upper left')
frame  = legend.get_frame()
frame.set_facecolor('0.98')
for label in legend.get_texts():
    label.set_fontsize('medium')
for label in legend.get_lines():
    label.set_linewidth(1.0)  

plt.show()

#Didn't use pandas, instead I did it in matplotlib
# I removed the grids in a way that the graph seems better and reduced the scale of X and Y