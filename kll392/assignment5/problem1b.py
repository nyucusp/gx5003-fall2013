import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab

'''I used many of the same processes for this problem as I did for problem 1a.  The steps are briefly explained below, but much of it is very similar to 1a.  The only difference for this problem was that I called on ax.plot() twice, once for each dataset to be displayed.  This graph is very effective in showing directly the differences between Apple's and Microsoft's stocks, and paints a more accurate picture than the graphs produced in problem 1c. Looking at this graph, I can conclude that while Apple's stock is generally valued much higher than Microsoft's, it is also more volatile and so is likely a bit riskier.  It is clear from the plto that although it is valued lower, Microsoft's stock is impressively stable.
'''

#Instantiate lists to hold the values of month, apple and microsoft's stocks:
month = []
apple = []
microsoft = []

with open('stocks.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        month.append(row[0])
        apple.append(row[1])
        microsoft.append(row[2])
    
#Reverse all of the lists to be in correct chronological order:
month = month[::-1]
apple = apple[::-1]
microsoft = microsoft[::-1]

#As in problem 1a, I created a simple list of integers to use in place of the month and year data because the intervals are evenly spaced and a list of integers is much easier to work with:
newdates = list(xrange(33))

#Instantiate plot:
fig, ax = plt.subplots()

#Plot both microsoft and apple on the same figure by calling the same axes (ax):
ax.plot(newdates, apple, label='AAPL')
ax.plot(newdates, microsoft, label='MSFT')

#Specify a range for the x and y axes:
plt.xticks(np.arange(0, max(newdates) + 1, 4))
plt.yticks(np.arange(40, 240, 20))

#Format the x axis so that labels are rotated 30 degrees for easier reading:
xAxis = plt.axes().xaxis
for tl in xAxis.get_ticklabels():
    tl.set_rotation(30)

#Fetch the labels and set them to the previously created list of months and years:
labels = [item.get_text() for item in ax.get_xticklabels()]
for i in range(0, len(month)/4 + 1):
    labels[i] = month[i*4]
ax.set_xticklabels(labels)

#Title, label axes, legend:
fig.suptitle('Apple vs Microsoft Stocks', fontsize=20)
plt.xlabel('Month', fontsize = 16)
plt.ylabel('Stock Value', fontsize = 16)
legend = ax.legend(loc = 'upper left')

plt.grid(True)

plt.show()
