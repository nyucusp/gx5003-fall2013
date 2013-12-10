import matplotlib.pyplot as plt
from datetime import date
import numpy as np

data = open('stocks.dat','r') #open file

arr_mon = []
arr_app = []
app_micro  = []
for plot1 in data:   # Separating data values
    split_data = plot1.split(',')
    arr_mon.append(split_data[0])
    arr_app.append(split_data[1])
    arr_mic.append(split_data[2])

del arr_mon[0]   # Deleting initial values in all the arrays defined
del arr_app[0]
del arr_mic[0]

dates = []
for element in arr_mon:
    year = int(element.split('-')[0])
    month = int(element.split('-')[1])
    new_date = date(int(year),int(month),1)
    dates.append(new_date)

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.set_title("Apple and Microsoft Stocks")  # Setting the title

#Values being plotted for Microsoft data
ax0.plot(dates, arr_mic, 'go-', label='Microsoft')
ax0.set_xlabel('Date')
ax0.set_ylabel('Microsoft \'s Stock')
ax0.set_ylim(20,40)
ax0.yaxis.set_ticks(np.arange(20, 40, 5))
min_date = date(2005, 12, 1) # Limiting data for the minimum date
max_date = date(2008, 10, 1) # Limiting data for the maximum date
ax0.set_xlim(min_date, max_date)
ax0.grid(which = 'both', color = '0.90', linestyle = '-')
ax0.legend(loc='upper left')

# Values being plotted for Apple data
ax1.plot(dates, arr_app, 'o-', label='Apple')
ax1.set_xlabel('Date')
ax1.set_ylabel('Apple \'s Stock')
ax1.set_ylim(40,210)
ax1.yaxis.set_ticks(np.arange(40, 210, 40))
min_date = date(2005, 12, 1) # Limiting data for the minimum date
max_date = date(2008, 10, 1) # Limiting data for the maximum date
ax1.set_xlim(min_date, max_date)
ax1.grid(which = 'both', color = '0.90', linestyle = '-')
ax1.legend(loc='upper left')

plt.setp(ax0.get_xticklabels(), rotation=15)
plt.setp(ax1.get_xticklabels(), rotation=15)
plt.subplots_adjust(hspace=0.45)
plt.tight_layout()
plt.show()

# I plotted by juxtaposition the stock values of Apple & Microsoft over each other.
# This gives a better understanding to study by doing a comparitive analysis on the stock patterns of both the companies over time.
# But caution should be mantained as the scales of the Stock Values differ!

