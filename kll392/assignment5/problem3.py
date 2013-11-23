import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import operator

years = []
transistors = []
processors = []
data = {}

with open('microprocessors.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    i = 1
    for row in rows:
        processor = row[0]
        year = int(row[1])
        transistor = int(row[2])
        data[processor] = year, transistor
        years.append(year)
        transistors.append(transistor)

for item in data:
    print item, data[item]

simpleList = np.arange(0, 13)

fig = plt.figure()

#PLOT 1: YEAR

pByYear = []
sortByYear = sorted(data.iteritems(), key = operator.itemgetter(1))
for entry in sortByYear:
    pByYear.append(entry[0])
years.sort()

ax1 = fig.add_subplot(121)
ax1.plot(years, simpleList, 'o')
ax1.yaxis.grid()
plt.xlim([1960, 2010])
plt.yticks(np.arange(-1, 14, 1))

for label in ax1.yaxis.get_ticklabels():
    label.set_size('10')

labels = [item.get_text() for item in ax1.get_yticklabels()]
for i in range (0, 13):
    labels[i + 1] = pByYear[i]
ax1.set_yticklabels(labels)


#PLOT 2: TRANSISTORS

pByTrans = []
sortByTrans = sorted(data.iteritems(), key = operator.itemgetter(1))
for entry in sortByTrans:
    pByTrans.append(entry[0])
transistors.sort()

ax2 = fig.add_subplot(122)
ax2.plot(transistors, simpleList, 'o')
ax2.yaxis.grid()
ax2.set_xscale('log')
plt.yticks(np.arange(-1, 14, 1))

for label in ax2.yaxis.get_ticklabels():
    label.set_size('10')

labels = [item.get_text() for item in ax2.get_yticklabels()]
for i in range (0, 13):
    labels[i + 1] = pByTrans[i]
ax2.set_yticklabels(labels)



plt.show()
