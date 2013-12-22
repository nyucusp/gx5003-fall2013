import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

actionsFile = open('actions-fall-2007.dat', 'r')
actionsFile.readline()
dateTimeList = []
for line in actionsFile:
    thisDateTime = time.strptime(line, "%Y-%m-%d %H:%M:%S\n")
    dateTimeList.append(thisDateTime)

hist, edges = np.histogram(dateTimeList, 4)

print hist, edges

plt.hist(dateTimeList)

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.bar(edges[:-1], hist / width, width=width)
ax.set_xlim(bin_edges[0], num_now())
ax.set_ylabel('Events [1/day]')
if title:
    ax.set_title(title)
 
    # set x-ticks in date
    # see: http://matplotlib.sourceforge.net/examples/api/date_demo.html
ax.xaxis.set_major_locator(YearLocator())
ax.xaxis.set_major_formatter(DateFormatter('%Y'))
ax.xaxis.set_minor_locator(MonthLocator())
    # format the coords message box
ax.format_xdata = DateFormatter('%Y-%m-%d')
ax.grid(True)
 
fig.autofmt_xdate()
