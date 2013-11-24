#Aliya Merali
#Urban Informatics
#Assignment 5
#Problem 1c

import matplotlib.pyplot as plt
from datetime import date
import numpy as np

data = open('stocks.dat','r')

month = []
apple = []
msft  = []
for line in data:
    split_data = line.split(',')
    month.append(split_data[0])
    apple.append(split_data[1])
    msft.append(split_data[2])
del month[0]
del apple[0]
del msft[0]

dates = []
for element in month:
    yr = int(element.split('-')[0])
    mn = int(element.split('-')[1])
    new_date = date(int(yr),int(mn),1)
    dates.append(new_date)

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.set_title("Apple &  Microsoft Stock Quotes at the Start of Each Month")
#fig.autofmt_xdate()
#plt.xticks(rotation=30)

ax0.plot(dates, apple, 'o-', label='Apple')
#plt.xticks(rotation=30)
ax0.set_xlabel('Date')
ax0.set_ylabel('Stock Quote')
ax0.set_ylim(40,210)
ax0.yaxis.set_ticks(np.arange(40, 210, 40))
datemin = date(2005, 12, 1)
datemax = date(2008, 10, 1)
ax0.set_xlim(datemin, datemax)
ax0.grid(which = 'both', color = '0.75', linestyle = '-')

ax1.plot(dates, msft, 'go-', label='Microsoft')
#plt.xticks(rotation=30)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Quote')
ax1.set_ylim(20,40)
ax1.yaxis.set_ticks(np.arange(20, 40, 5))
datemin = date(2005, 12, 1)
datemax = date(2008, 10, 1)
ax1.set_xlim(datemin, datemax)
ax1.grid(which = 'both', color = '0.75', linestyle = '-')

plt.subplots_adjust(hspace=0.5)
#plt.xticks(rotation=30)

# Now add the legends
legend = ax0.legend(loc='upper left')
legend2 = ax1.legend(loc='upper left')

plt.show()


#_____________________Annotation
