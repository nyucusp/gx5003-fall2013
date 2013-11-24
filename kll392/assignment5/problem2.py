import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import numpy as np
from collections import OrderedDict

'''
(a) I selected to do each day as a bin.  The dataset was so large that it made more sense to group by days, expecially because with the number of days included in the dataset it wouldn't have made much difference visually to go by half days, or hours, etc.

(b) Simply from looking at the histogram, I figure that assignment 3 was the most difficult because it had by far the most actions.  It looks like some people turned in assignments 3 and 4 late.  Assignments 1 and 2 required the least work.

(c) There is clearly a somewhat steady increase of work leading up to the due date of the assigment.  The number of people taking an action increases each day leading up to the due date, peaking on the due date.  This makes sense with general human nature.
'''

#I use this function to determine if a day is between 1-9.  If it is, I add a 0 to the beginning of the day so that it works in numerical order.  Like problem 1, I changed dates into integers so they would be easier to work with, so 10/09 became 1009. 
def isLessTen(day):
    date = int(day)
    if (date < 10):
        return True
    else:
        return False

#Read the data from the .dat file into a list of tuples called data:
data = []
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
    d = datetime.date(year, month, day)
    datadict[d] = 0
    datalist.append(d)

#Iteratively count how many submissions occurred on each day:
for x in range (8,13):
    for line in datalist:
        if (line.month == x):
            for y in range (0,32):
                if (line.day == y):
                    datadict[line] += 1

newdict = OrderedDict(sorted(datadict.items(), key = lambda t: t[0]))

dates = []
numSubmitted = []

#Change dates from 10/01 format into 1001 format:
for line in newdict:
    month = str(line.month)
    day = str(line.day)
    if (isLessTen(day) == True):
        day = '0'+day
    thisdate = month+day
    dates.append(int(thisdate))
    numSubmitted.append(newdict[line])

dateDict = {}
dateIndex = np.arange(0,len(dates))
i = 0
for line in dates:
    dateDict[i] = line
    i += 1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(dateIndex, numSubmitted)

#dueDates holds the corresponding integer for the various due dates.  Here I make the bar for each due date red so that it stands out on the histogram:
mergeFile = zip(dateIndex, numSubmitted)
dueDates = [8, 23, 34, 52, 66, 62]
for line in mergeFile:
    if (int(line[0]) in dueDates):
        ax.bar(line[0], line[1], color='red')

#Set fixed axis labels where assignments were due:
xAxis = plt.axes().xaxis
xAxis.set_major_locator(ticker.FixedLocator(dueDates))
for tl in xAxis.get_ticklabels():
    tl.set_fontsize(10)

#Set axis labels to due dates of assignments:
labels = [item.get_text() for item in ax.get_xticklabels()]
text = ['#1\n09-18', '#2\n10-04', '#3\n10-25', '#4\n11-27', '#5\n12-15', '#6\n12-11']
for i in range (0, 6):
    labels[i] = text[i]

axis = ax.xaxis
for tick in axis.get_ticklines():
    tick.set_color('black')

ax.set_xticklabels(labels)

fig.suptitle('Scientific Visualization Course Submissions, 2007', fontsize=16)
plt.ylabel('Number of actions', fontsize=14)

plt.show()
