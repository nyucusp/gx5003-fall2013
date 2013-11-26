import pylab
import scipy
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.ticker as mticker 
from matplotlib import dates 
import datetime 
from scipy import stats
import dateutil.parser as dparser
from matplotlib import pyplot as PLT 

stocks_file = open('stocks.dat', 'rU')
stocks_lines = csv.reader(stocks_file)


list_dates_r = []
list_apple_r = []
list_microsoft_r = [] 

for x in stocks_lines:
	list_dates_r.append(x[0]) 
	list_apple_r.append(x[1])
	list_microsoft_r.append(x[2])

# Rid of first line 

list_dates_r = list_dates_r[1:]
list_apple_r = list_apple_r[1:]
list_microsoft_r = list_microsoft_r[1:] 


# Reverse 

list_dates = []
list_apple = []
list_microsoft = [] 

for x in reversed(list_dates_r):
	list_dates.append(dparser.parse(x, fuzzy=True))

for x in reversed(list_apple_r):
	list_apple.append(float(x))

for x in reversed(list_microsoft_r):
	list_microsoft.append(float(x))


#print list_dates
#print list_apple
#print list_microsoft

#plt.scatter(list_dates, list_apple)
#plt.show()


#dates = matplotlib.dates.date2num(list_dates)
#print dates 
#plot_date(list_dates, list_apple)

years = dates.YearLocator()
months = dates.MonthLocator()
yearsFmt = dates.DateFormatter('%Y' )
monthsFmt = dates.DateFormatter('%B' )
#autoFmt = dates.AutoDateFormatter()
### A ### 


fig, ax = plot.subplots()
line1 = ax.plot_date(list_dates, list_apple, 'o-', color = 'blue', alpha= 0.7, label='Apple Inc. (AAPL)')
#line2 = ax.plot_date(list_dates, list_microsoft, 'o-', color = 'orange', alpha= 0.7, label='Microsoft Corporation (MSFT)')

# format the ticks 
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
#ax.xaxis.set_minor_formatter(monthsFmt)


#lables 
fig.suptitle('Problem 1a', fontsize = 20)
plot.xlabel('Year', fontsize = 18)
plot.ylabel('Stock Quote', fontsize=16)
plot.legend(loc='upper left', prop={'size':14})
#plt.xlim((min(list_dates), max(list_dates))
plot.ylim((float(min(list_apple))-20), (float(max(list_apple))+20))
#print max(list_apple)
#print list_apple

#datemin = datetime.date(list_dates.min().year, 1, 1)
#datemax = datetime.date(list_dates.max().year+1,1,1)
#ax.set_xlim(datemin, datemax)


# grid
ax.grid(True)

fig.autofmt_xdate()

fig.savefig('Problem_1a.jpg')
plt.show()



### B ### 

fig, ax = plot.subplots()
line1 = ax.plot_date(list_dates, list_apple, 'o-', color = 'blue', alpha= 0.7, label='Apple Inc. (AAPL)')
line2 = ax.plot_date(list_dates, list_microsoft, 'o-', color = 'orange', alpha= 0.7, label='Microsoft Corporation (MSFT)')

# format the ticks 
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
#ax.xaxis.set_minor_formatter(monthsFmt)


#lables 
fig.suptitle('Problem 1b', fontsize = 20)
plot.xlabel('Year', fontsize = 18)
plot.ylabel('Stock Quote', fontsize=16)
plot.legend(loc='upper left', prop={'size':14})
#plt.xlim((min(list_dates), max(list_dates))
plot.ylim((float(min(list_microsoft))-20), (float(max(list_apple))+20))
plt.axhline(y=float(list_apple[1]), linestyle='-', color='blue')
plt.axhline(y=float(list_microsoft[1]), linestyle='-', color='orange')

#print max(list_apple)
#print list_apple

#datemin = datetime.date(list_dates.min().year, 1, 1)
#datemax = datetime.date(list_dates.max().year+1,1,1)
#ax.set_xlim(datemin, datemax)


# grid
ax.grid(True)

fig.autofmt_xdate()

fig.savefig('Problem_1b.png')
plt.show()



### C ### 

fig = PLT.figure() 
ax1 = fig.add_subplot(211)
ax1.plot_date(list_dates, list_apple, 'o-', color = 'blue', alpha= 0.7, label='Apple Inc. (AAPL)')
plt.axhline(y=float(list_apple[1]), linestyle='-', color='blue')
plot.legend(loc='upper left', prop={'size':14})


ax2 = fig.add_subplot(212)
ax2.plot_date(list_dates, list_microsoft, 'o-', color = 'orange', alpha= 0.7, label='Microsoft Corporation (MSFT)')


# format the ticks 
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_title('Apple')

ax2.xaxis.set_major_locator(years)
ax2.xaxis.set_major_formatter(yearsFmt)
ax2.xaxis.set_minor_locator(months)
ax2.set_title('Microsoft')

#ax.xaxis.set_minor_formatter(monthsFmt)

#lables 
#fig.suptitle('Problem 1c', fontsize = 20)
plot.xlabel('Year', fontsize = 18)
plot.ylabel('Stock Quote', fontsize=16)
plot.legend(loc='upper left', prop={'size':14})
#plt.xlim((min(list_dates), max(list_dates))
plot.ylim((float(min(list_apple))-20), (float(max(list_apple))+20))
plt.axhline(y=float(list_apple[1]), linestyle='-', color='blue')
#plt.axhline(y=float(list_microsoft[1]), linestyle='-', color='orange')

ax.grid(True)

fig.autofmt_xdate()

# format the ticks 
ax2.xaxis.set_major_locator(years)
ax2.xaxis.set_major_formatter(yearsFmt)
ax2.xaxis.set_minor_locator(months)
#ax.xaxis.set_minor_formatter(monthsFmt)

#lables 
fig.suptitle('Problem 1C', fontsize = 20)
plot.xlabel('Year', fontsize = 18)
plot.ylabel('Stock Quote', fontsize=16)
plot.legend(loc='upper left', prop={'size':14})
#plt.xlim((min(list_dates), max(list_dates))
plot.ylim((float(min(list_microsoft))-20), (float(min(list_microsoft))+20))
#plt.axhline(y=float(list_apple[1]), linestyle='-', color='blue')
plt.axhline(y=float(list_microsoft[1]), linestyle='-', color='orange')

ax.grid(True)

fig.autofmt_xdate()

fig.savefig('Problem_1c.png')
PLT.show 

plt.show()

stocks_file.close 


'''
Annotation 

a) The key is delivering the information clearly and effectively. 
I made sure that the ticks are not overlapped. Also the top and bottom of the graph are not touching the ceiling and bottom of the graph. 
I chose colors that distinguish the graph strongly from the background.

b) Clealy Apple is perceived as drastically valuable in the recent years. MS has been consistent in its value. 

c) I belive superposition is better in this case since I can clearly see the different valutions along the same axis. 



'''