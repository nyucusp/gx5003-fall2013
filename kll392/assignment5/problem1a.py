import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab
import matplotlib.ticker as ticker

#Initiate empty lists for entries of month and apple:
month = []
apple = []

with open('stocks.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        month.append(row[0])
        apple.append(row[1])

#Reverse month and apple arrays so that they read in chronological order:
month = month[::-1]
apple = apple[::-1]

#Because every entry in the list of stocks is equally spaced in time, I chose to create a list of simple integers that correspond to every month so that I do not have to deal with datetime objects:
intDates = list(xrange(len(apple)))

#Instantiate the figure:
fig, ax = plt.subplots()

#Plot the list of simple integers with apple stock values
ax.plot(intDates, apple, label='AAPL')

#Specify range for both x and y axes:
plt.xticks(np.arange(0, max(intDates) + 1, 4))
plt.yticks(np.arange(40, 240, 20))

#Formatting the x-axis: set rotation to 30 degrees for a more readable figure:
xAxis = plt.axes().xaxis
for tl in xAxis.get_ticklabels():
    tl.set_rotation(30)

#Fetch a list of the labels on the x axis.  Here I use my month list created earlier to cover the simple integer values with the correct month and year.  I chose to label every fourth tick as it seems to provide the most effective plot:
labels = [item.get_text() for item in ax.get_xticklabels()]
for i in range(0, max(intDates)/4 + 1):
    labels[i] = month[i*4]
ax.set_xticklabels(labels)

#Properly label the x and y axes, title the graph:
fig.suptitle('Apple Stock Quotes', fontsize=20)
plt.xlabel('Month', fontsize = 16)
plt.ylabel('Stock Value', fontsize = 16)

#Place a legend on the graph, which will display the value specified for 'label' in ax.plot():
legend = ax.legend(loc = 'upper left')

plt.grid(True)

#Finally, show the plot:
plt.show()
