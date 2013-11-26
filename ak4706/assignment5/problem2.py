import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
import pandas as pd
from pandas import DataFrame
from matplotlib.dates import date2num, num2date
from _collections import defaultdict
from dateutil.parser import parse


df = pd.read_csv('actions-fall-2007.dat', parse_dates=True)
# index_col=0)
#print df

actions = open('actions-fall-2007.dat', 'r')
next(actions)

act = []
for line in actions:
	act.append(parse(line.rstrip()))
timeDict=defaultdict(int)

for line in act:
	timeDict[line.strftime('%m-%d')] += 1

#graph = pd.DataFrame((df), index=pd.date_range('09/15/2007', periods = 100))

timeHours=pd.DataFrame.from_dict(timeDict, orient='index')

timeHours.columns = ['timestamp']

ax=timeHours['timestamp'].sort_index().plot(kind='bar')

plt.xlabel('Date')
plt.xticks(fontsize=6)
ax.vlines( 9, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 1')
plt.text(6,14005, "Assign 0 & 1", fontsize=8)
ax.vlines( 24, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 2')
plt.text(23,14005, "Assign 2", fontsize=8)
ax.vlines( 35, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 3')
plt.text(32,14005, "Assign 3", fontsize=8)
ax.vlines( 53, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 4')
plt.text(50,14005, "Assign 4", fontsize=8)
ax.vlines( 67, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 5')
plt.text(66,14005, "Assign 5", fontsize=8)
ax.vlines( 63, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 6')
plt.text(60,14005, "Assign 6", fontsize=8)

plt.text(35, 14400, "Histogram of Frequency of Timestamps with Due Dates", horizontalalignment = 'center', fontsize=16)
plt.ylabel("Number of Timestamps")
plt.show()

#Annotations:
#a. It was only over a span of 3 months, so monthly wouldn't have shown
#	anything and hourly would've been way to much, so daily is a good
#	time scale to see whats going around each assignment due date
#b. The first and second assignments seemed to have little work, the 
#	third was definitely the most work, and then less and less for 4, 5
#	and 6.
#c. For the first assignment people were much more on top of it and there
#	was even less action on the day it was due than the day before.  For
#	the second assignment there was a little more activity on the day it
#	was due.  By the third assignment the timestamps on the day it was due
#	skyrocketed, and the fourth assignment was also high.  The 6th had less
#	the day it was due, but then the 5th went back to being more.

#before I realized exactly what we were supposed to be doing:
# count1 = 0
# for line in input:
# 	if line < '2007-09-18 12:00:00':
# 		count1=count1+1
# 		#print line
# print count1


# count2 = 0
# for line in input:
# 	if (line > '2007-09-18 12:00:00' and line < '2007-10-04 12:00:00'):
# 		count2=count2+1
# 		#print line
# print count2

# count3 = 0
# for line in input:
# 	if (line > '2007-10-04 12:00:00' and line < '2007-10-25 12:00:00'):
# 		count3=count3+1
# 		#print line
# print count3

# count4 = 0
# for line in input:
# 	if (line > '2007-10-25 12:00:00' and line < '2007-11-27 12:00:00'):
# 		count4=count4+1
# 		#print line
# print count4

# count5 = 0
# for line in input:
# 	if (line > '2007-11-27 12:00:00' and line < '2007-12-11 12:00:00'):
# 		count5=count5+1
# 		#print line
# print "assignment 6", count5

# count6 = 0
# for line in input:
# 	if (line > '2007-12-11 12:00:00' and line < '2007-12-15 12:00:00'):
# 		count6=count6+1
# 		#print line
# print "assignment 5", count6