#Aliya Merali
#Urban Informatics
#Assignment 5
#Problem 1b

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

fig, ax = plt.subplots()
ax.plot(dates, apple, 'o-', label='Apple')
ax.plot(dates, msft, 'o-', label='Microsoft')

fig.autofmt_xdate()
#Added the appropriate labels below for easy interpretation
plt.xlabel('Date')
plt.ylabel('Stock Quote')
plt.title("Apple v. Microsoft Stock Quotes at the Start of Each Month")
#Adjusted the x&y limits so plot had top & side buffers
ax.set_ylim(0,210)
ax.yaxis.set_ticks(np.arange(0, 210, 20))
datemin = date(2005, 12, 1)
datemax = date(2008, 10, 1)
ax.set_xlim(datemin, datemax)
plt.grid(which = 'both', color = '0.75', linestyle = '-')#Added light gridlines to make reading easier

# Now add the legend
legend = ax.legend(loc='upper left')
frame  = legend.get_frame()
frame.set_facecolor('0.98')
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

plt.show()

#_______________Conclusions drawn from this plot
"""
From this plot, you can directly compare the Stock Quotes of Apple and Microsoft. It is 
helpful to have them on the same graph because you can see both the changes in the quote 
value as well as the value relative to one another. Clearly, the Stock Quote for Apple 
is higher than that for Microsoft throughout, but you can also detect the same trends 
among both companies. Both values dip in May 2006, although Apple more extreme than 
Microsoft, and both rise in November of 2006. This matching trend continues with both 
rising and dipping in October and November of 2007, and dropping in February of 2008. 
Microsoft's Stock Quote is much more stable with less extreme peaks and dips, but both 
follow a similar pattern which likely reflects the trends of the market as a whole. 
"""
