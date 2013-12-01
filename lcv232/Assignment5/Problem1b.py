import matplotlib.pyplot as plt
from datetime import date
import numpy as np

data = open('stocks.dat','r') #open file

arr_mon = []
arr_app = []
arr_micro  = []
for plot1 in data:      # Separating data values
    split_data = plot1.split(',')
    arr_mon.append(split_data[0])
    arr_app.append(split_data[1])
    arr_micro.append(split_data[2])

del arr_mon[0]  # Deleting initial values in all the arrays defined
del arr_app[0]
del arr_micro[0]

dates = []
for value1 in arr_mon:
    year = int(value1.split('-')[0])
    month = int(value1.split('-')[1])
    new_date = date(int(year),int(month),1)
    dates.append(new_date)

fig, ax = plt.subplots()  # Labelling the plot
ax.plot(dates, arr_app, 'o-', label='Apple')
ax.plot(dates, arr_micro, 'o-', label='Microsoft')
fig.autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Stock')
plt.title("Apple vs Microsoft")

# Setting the limits & display stuff in the plot
ax.set_ylim(0,200)
ax.yaxis.set_ticks(np.arange(0, 200, 20))
min_date = date(2005, 12, 1) # Limiting data for the minimum date
max_date = date(2008, 10, 1) # Limiting data for the maximum date
ax.set_xlim(min_date, max_date)
plt.grid(which = 'both', color = '0.90', linestyle = '-')

# Setting the label features
legend = ax.legend(loc='upper left')
frame  = legend.get_frame()
frame.set_facecolor('0.98')
for label in legend.get_texts():
    label.set_fontsize('medium')
for label in legend.get_lines():
    label.set_linewidth(1.0)  

plt.show()

# I have used Matplotlib to do the plotting.
# Have not used much of gridlines as they add confusion to the graph.
# I removed the grids in a way that the graph seems better interms of the scale of X and Y axis.
# The color used to display the plotting is Blue for Apple & Green for Microsoft, as the colors are subtle to the eye. 