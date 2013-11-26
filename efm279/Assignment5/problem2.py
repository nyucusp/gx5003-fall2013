from matplotlib import pyplot
from matplotlib.dates import date2num
import numpy as np
import csv
import time
x1 = []
x2 = []
y1 = []
y2 = []
xcount=[]
labels=[]
counter=0
pattern = '%Y-%m-%d %H:%M:%S'
pyplot.figure(figsize=(18, 18))

## Change time to epoch time for the sake of simplicity

with open('actions-fall-2007.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    spamreader.next() 
    for row in spamreader:
            x2.append(row[0])
            x1.append(int(time.mktime(time.strptime(row[0], pattern))))
            counter=counter+1

xv = np.array(x1)

#a Bins are defined for 12 hours for visual considerations, daily bins created too broad observations and can be misleading considering the deadlines are at 12:00pm
#b Assignment 3 has the highest number of actions, it is also interesting a big portion of the homework submissions are made after the deadline has passed. Assignment 6,4,5 respectively has the next high number of actions.
#  Assignment 1 has the least number of actions.

#c Number of actions increase close to deadlines. For Assignment 2,3 and 4 more number of actions are observed right after the deadline. For the others more number of actions are observed right before the deadline.

pyplot.hist(x1, bins=range(min(x1),max(x1),43200), facecolor='red', alpha=0.75)

for timex in range(min(x1),max(x1),100000):
        labels.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timex)))[5:-9])


pyplot.xticks(range(min(x1),max(x1),100000), labels, rotation='vertical')
pyplot.ylim(0,12500)
pyplot.ylabel('Number of actions')
pyplot.xlabel('Date')
pyplot.title('Assignment Submission Records')

deadlines=['2007-09-18 12:00:00','2007-10-04 12:00:00','2007-10-25 12:00:00','2007-11-27 12:00:00','2007-12-15 12:00:00','2007-12-11 12:00:00']
fabio=1
for nivan in deadlines:
        pyplot.axvline(x=int(time.mktime(time.strptime(nivan, pattern))),ls='--',color='green', linewidth=2)
        pyplot.text(int(time.mktime(time.strptime(nivan, pattern)))-80000,12000,'Assignment '+str(fabio)+' Deadline', rotation=90)
        fabio=fabio+1
pyplot.show()


