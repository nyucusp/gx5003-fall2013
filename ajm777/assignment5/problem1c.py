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

ax0.plot(dates, apple, 'o-', label='Apple')
ax0.set_xlabel('Date')
ax0.set_ylabel('Stock Quote')
ax0.set_ylim(40,210)
ax0.yaxis.set_ticks(np.arange(40, 210, 40))
datemin = date(2005, 12, 1)
datemax = date(2008, 10, 1)
ax0.set_xlim(datemin, datemax)
ax0.grid(which = 'both', color = '0.75', linestyle = '-')
ax0.legend(loc='upper left')

ax1.plot(dates, msft, 'go-', label='Microsoft')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Quote')
ax1.set_ylim(20,40)
ax1.yaxis.set_ticks(np.arange(20, 40, 5))
datemin = date(2005, 12, 1)
datemax = date(2008, 10, 1)
ax1.set_xlim(datemin, datemax)
ax1.grid(which = 'both', color = '0.75', linestyle = '-')
ax1.legend(loc='upper left')

plt.setp(ax0.get_xticklabels(), rotation=15)
plt.setp(ax1.get_xticklabels(), rotation=15)
plt.subplots_adjust(hspace=0.45)
plt.tight_layout()
plt.show()

#_____________________Annotation
"""
In this plot, we can see the fluctuations in the stock of Apple and 
Microsoft very clearly. Because Microsoft's peaks and drops are 
smaller than Apple's (rising ~7 points from September to October 2007 
vs. Apple's rise of ~35 points in that same time period), it is 
difficult to see them when plotted on the same graph. Here, however, 
you can clearly see the trends followed by both stocks and the rises 
and falls in each one specifically. Which format makes more sense 
depends on your intention for the graph. If the goal is to compare the 
value of the two stocks, than they should be plotted on the same graph. 
If the goal is to compare the patterns and fluctuations of the two
stocks, then this represnetation (on two graphs) makes the most sense. 
"""
