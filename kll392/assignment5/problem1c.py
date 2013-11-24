import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab

'''For this kind of data, superposition makes more sense than juxtaposition.  As you can see from my plots, expressing the data on different figures can be misleading because it is possible to use different scales, which in this case makes it appear as though Microsoft's stock is valued more closely to Apple's than it is in reality.
'''

#As with the previous two problems, I instantiate lists of months, microsoft and apple's stocks and read the values in from the data file.  In order to put the lists in proper chronological order, I reverse all of them.
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

#I used the same method as previously where I assign each month a simple integer for ease of plotting.
newdates = list(xrange(33))

#Instead of creating the fig, ax objects at the same time, I first call fig = plt.figure().  Then, in order to make 2 sub plots I specify ax1 and ax2, and pass three integers that specify how many rows and columns I will have, and where these axes should be located.  The rest of the code is the same as problems 1a and 1b:
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(newdates, apple, 'r', label='AAPL')
plt.xticks(np.arange(0, max(newdates)+1, 4))
plt.yticks(np.arange(40, 240, 20))

labels = [item.get_text() for item in ax1.get_xticklabels()]
for i in range(0, len(month)/4 + 1):
    labels[i] = month[i*4]
ax1.set_xticklabels(labels)

plt.ylabel('Stock Value', fontsize = 16)
legend = ax1.legend(loc = 'upper left')


ax2 = fig.add_subplot(212)
ax2.plot(newdates, microsoft, label='MSFT')
plt.xticks(np.arange(0, max(newdates)+1, 4))
plt.yticks(np.arange(20, 100, 20))

labels = [item.get_text() for item in ax2.get_xticklabels()]
for i in range(0, len(month)/4 + 1):
    labels[i] = month[i*4]
ax2.set_xticklabels(labels)

plt.xlabel('Month', fontsize = 16)
plt.ylabel('Stock Value', fontsize = 16)
legend = ax2.legend(loc = 'upper left')

fig.suptitle('Apple vs Microsoft Stock Value', fontsize=18)

ax1.grid(True)
ax2.grid(True)

plt.show()

