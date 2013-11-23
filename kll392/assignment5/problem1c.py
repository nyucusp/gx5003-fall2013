import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab

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
    
month = month[::-1]
apple = apple[::-1]
microsoft = microsoft[::-1]

newdates = list(xrange(33))

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(newdates, apple, 'r', label='AAPL')
plt.xticks(np.arange(0, max(newdates)+3, 1))
plt.yticks(np.arange(40, 240, 20))

xaxis = []
for i in range(0, len(month)):
    if (i%7 == 0):
        xaxis.append(month[i])

labels = [item.get_text() for item in ax1.get_xticklabels()]
for i in range(1, len(month)):
    if (i%5 == 0):
        labels[i] = month[i]

ax1.set_xticklabels(labels)
plt.ylabel('Stock Value', fontsize = 16)
legend = ax1.legend(loc = 'upper left')


ax2 = fig.add_subplot(212)
ax2.plot(newdates, microsoft, label='MSFT')
plt.xticks(np.arange(0, max(newdates)+3, 1))
plt.yticks(np.arange(20, 100, 20))

labels = [item.get_text() for item in ax2.get_xticklabels()]
for i in range(1, len(month)):
    if (i%5 ==0):
        labels[i] = month[i]

ax2.set_xticklabels(labels)
plt.xlabel('Month', fontsize = 16)
plt.ylabel('Stock Value', fontsize = 16)
legend = ax2.legend(loc = 'upper left')

fig.suptitle('Apple vs Microsoft Stock Value', fontsize=18)

ax1.grid(True)
ax2.grid(True)

plt.show()

