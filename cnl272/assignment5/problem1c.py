import matplotlib.pyplot as plt
from datetime import date
import matplotlib.ticker as ticker
import numpy as np

myfile = open('stocks.dat','r')

#split data in the origin file and append it into arrays of month and apple
month = []
apple = []
msft = []
for line in myfile:
    data = line.split(',')
    month.append(data[0])
    apple.append(data[1])
    msft.append(data[2])
del month[0]
del apple[0]
del msft[0]

#transform data in month as integer for plotting
datetimes = []
for times in month:
	years = int(times.split('-')[0])
	months = int(times.split('-')[1])
	date_time = date(int(years),int(months),1)
	datetimes.append(date_time)

fig, (ax1, ax2) = plt.subplots(nrows=2)
#label the axes of x and y, add the title for the both graphs
ax1.plot(datetimes, apple, 'o--', label='Apple')
ax1.set_title('Apple Stock Price, Jan 2006 - Sep 2008', fontsize=20)
ax1.set_xlabel('Month', fontsize = 16)
ax1.set_ylabel('US Dollars', fontsize=16)
ax2.set_xlabel('Month', fontsize = 16)
ax2.set_ylabel('US Dollars', fontsize=16)
ax2.set_title('Microsoft Stock Price, Jan 2006 - Sep 2008', fontsize=20)
ax2.plot(datetimes, msft, 'o--', label='Microsoft')

#place the proper time for x axis and proper range for y axis
ax1.set_ylim(0,210)
ax1.yaxis.set_ticks(np.arange(0, 210, 20))
date_start = date(2005, 12, 1)
date_end = date(2008, 10, 1)

#place label on the proper side and add gridlines to help reading easier
ax1.legend(loc = 'upper left')
ax1.grid(which = 'both', color = '0.85', linestyle = '-')

ax2.set_ylim(0,100)
ax2.yaxis.set_ticks(np.arange(0, 100, 10))
ax2.legend(loc = 'upper left')
ax2.grid(which = 'both', color = '0.85', linestyle = '-')

fig.autofmt_xdate()
plt.show()
