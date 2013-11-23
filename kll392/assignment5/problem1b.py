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

fig, ax = plt.subplots()
fig.canvas.draw()

ax.plot(newdates, apple, label='AAPL')
ax.plot(newdates, microsoft, label='MSFT')

plt.xticks(np.arange(0, max(newdates)+3, 1))
plt.yticks(np.arange(40, 240, 20))

xaxis = []
for i in range(0, len(month)):
    if (i%7 == 0):
        xaxis.append(month[i])

labels = [item.get_text() for item in ax.get_xticklabels()]
for i in range(1, len(month)):
    if (i%5 == 0):
        labels[i] = month[i]

ax.set_xticklabels(labels)

fig.suptitle('Apple vs Microsoft Stocks', fontsize=20)
plt.xlabel('Month', fontsize = 16)
plt.ylabel('Stock Value', fontsize = 16)

legend = ax.legend(loc = 'upper left')

plt.grid(True)

plt.show()
