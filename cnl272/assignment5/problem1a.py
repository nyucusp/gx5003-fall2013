import matplotlib.pyplot as plt
from datetime import date
import matplotlib.ticker as ticker

myfile = open('stocks.dat','r')

#split the data in the file and append it into arrays of month and apple
month = []
apple = []
for line in myfile:
    data = line.split(',')
    month.append(data[0])
    apple.append(data[1])
del month[0]
del apple[0]

#transform data in month as integer for plotting
datetimes = []
for times in month:
	years = int(times.split('-')[0])
	months = int(times.split('-')[1])
	date_time = date(int(years),int(months),1)
	datetimes.append(date_time)

fig, ax = plt.subplots()
ax.plot(datetimes, apple, 'o--', label='Apple')
fig.autofmt_xdate()
#label the axes of x and y, add the title for the graph
plt.xlabel('Month', fontsize = 16)
plt.title("Apple Stock Price, Jan 2006 - Sep 2008", fontsize=20)
plt.ylabel("US Dollars", fontsize=16)
#place the proper time for x axis
ax.set_ylim(40,210)
date_start = date(2005, 12, 1)
date_end = date(2008, 10, 1)
#add gridlines
plt.grid(which = 'both', color = '0.85', linestyle = '-')
#place label on the proper side
plt.legend(loc = 'upper left')

plt.show()