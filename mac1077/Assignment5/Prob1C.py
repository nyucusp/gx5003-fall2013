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

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.set_title("Apple and Microsoft Stocks")

#plot for Microsoft
ax0.plot(dates, mic, 'go-', label='Microsoft')
ax0.set_xlabel('Date')
ax0.set_ylabel('Microsoft \'s Stock')
ax0.set_ylim(20,40)
ax0.yaxis.set_ticks(np.arange(20, 40, 5))
datemin = date(2005, 12, 1)#Limits of minimum date
datemax = date(2008, 10, 1)#Limits of maximum date
ax0.set_xlim(datemin, datemax)
ax0.grid(which = 'both', color = '0.90', linestyle = '-')
ax0.legend(loc='upper left')

#plot for Apple
ax1.plot(dates, app, 'o-', label='Apple')
ax1.set_xlabel('Date')
ax1.set_ylabel('Apple \'s Stock')
ax1.set_ylim(40,210)
ax1.yaxis.set_ticks(np.arange(40, 210, 40))
datemin = date(2005, 12, 1)#Limits of minimum date
datemax = date(2008, 10, 1)#Limits of maximum date
ax1.set_xlim(datemin, datemax)
ax1.grid(which = 'both', color = '0.90', linestyle = '-')
ax1.legend(loc='upper left')

plt.setp(ax0.get_xticklabels(), rotation=15)
plt.setp(ax1.get_xticklabels(), rotation=15)
plt.subplots_adjust(hspace=0.45)
plt.tight_layout()
plt.show()

#juxtaposition technique is better in this kind of comparisons, it makes it easier
# to read
