import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import operator

#Read the data into a list of years and transistors, and a dictionary whose key is the type of processor and data entries are year and number of transistors:
years = []
transistors = []
data = {}

with open('microprocessors.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        processor = row[0]
        year = int(row[1])
        transistor = int(row[2])
        data[processor] = year, transistor
        years.append(year)
        transistors.append(transistor)

#Again, I create a list of integers corresponding to the number of data entries to be plotted
simpleList = np.arange(0, len(years))


fig = plt.figure()


#PLOT 1: YEAR

#pByYear will hold a list of processor names as sorted chronologically by year.  I sort the list of years separately, which I can then plot against my list of integers. Then, I label the data with the sorted list of processors.  This is a similar process I have gone through with the previous problems. I follow the same process for the second sub-plot.
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
plt.xlabel('Year')

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

#Label the y axis on the right size of the graph instead of the left for a figure that is easier to read
for tick in ax2.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = True

for label in ax2.yaxis.get_ticklabels():
    label.set_size('10')
plt.xlabel('Number of Transistors')

labels = [item.get_text() for item in ax2.get_yticklabels()]
for i in range (0, 13):
    labels[i + 1] = pByTrans[i]
ax2.set_yticklabels(labels)

plt.suptitle('Evolution of Microprocessors', size=16)

plt.show()
