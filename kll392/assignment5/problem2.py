import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import numpy as np
from collections import OrderedDict

data = []

def isLessTen(day):
    date = int(day)
    if (date < 10):
        return True
    else:
        return False

with open('actions-fall-2007.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        data.append(row)

datadict = {}
datalist = []

for row in data:
    entry = str(row)
    year = int(entry[2:6])
    month = int(entry[7:9])
    day = int(entry[10:12])
    hour = int(entry[13:15])
    minute = int(entry[16:18])
    second = int(entry[19:21])
    d = datetime.date(year, month, day)
    datadict[d] = 0
    datalist.append(d)

for x in range (8,13):
    for line in datalist:
        if (line.month == x):
            for y in range (0,32):
                if (line.day == y):
                    datadict[line] += 1

newdict = OrderedDict(sorted(datadict.items(), key = lambda t: t[0]))

dates = []
numSubmitted = []

for line in newdict:
    month = str(line.month)
    day = str(line.day)
    if (isLessTen(day) == True):
        day = '0'+day
    thisdate = month+day
    dates.append(int(thisdate))
    numSubmitted.append(newdict[line])

dateDict = {}
dateIndex = np.arange(0,68)
i = 0
for line in dates:
    dateDict[i] = line
    i += 1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(dateIndex, numSubmitted)

#for line in dateDict:
#    print line, dateDict[line]
 


'''
labels = []
for line in labelLocs:
    for entry in dateDict:
        if (dateDict[entry] == line):
            labels.append(entry)

for line in labels:
    print line
'''

xAxis = plt.axes().xaxis
xAxis.set_major_locator(ticker.FixedLocator([8, 23, 34, 52, 66, 62]))
for tl in xAxis.get_ticklabels():
    tl.set_fontsize(10)
    tl.set_rotation(30)

#labels = [item.get_text() for item in ax.get_xticklabels()]
#labels = [8, 23, 34, 52, 66, 62]

#ax.set_xticklabels(labels)


'''
locations: asignment 0: 9-18
assignment 1: 9-18
assignment 2: 10-04
assignment 3: 10-25
assignment 4: 11-27
assignment 5: 12-15
assignment 6: 12-11
'''


plt.show()
