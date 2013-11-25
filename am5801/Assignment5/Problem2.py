# Awais Malik
# Assignment 5
# Problem 2
# Annotations at the end of the code

from dateutil.parser import parse
import pandas as pd
from _collections import defaultdict

actions = open('actions-fall-2007.dat','r')
next(actions)

action_list = []
for line in actions:
    action_list.append(parse(line.rstrip()))
actions.close()

timeDict = defaultdict(int)

for line in action_list:
    timeDict[line.strftime('%m-%d')] += 1

timeHours = pd.DataFrame.from_dict(timeDict, orient='index')

timeHours.columns = ['TimeStamps']
timeHours = timeHours.sort()

time_list = []
for i in range(1,69):
    time_list.append(i)
    
timeHours['x_position']=time_list

ax = timeHours['TimeStamps'].sort_index().plot(kind='bar', grid='off', legend=False)

ax.text(0.5, 1.06, 'Histogram of Assignment Due Dates',
         horizontalalignment='center',
         fontsize=16,
         transform = ax.transAxes)
ax.set_ylabel('No. of Time Stamps')

ax.vlines(x = 9, ymin = 0, ymax = 14000,\
linestyles = 'dashed', colors='k', label='Assignments 0 and 1')
ax.annotate('Assigns 0 & 1', xy=(8,14010))

ax.vlines(x = 24, ymin = 0, ymax = 14000,\
linestyles = 'dashed', colors='k', label='Assignment 2')
ax.annotate('Assign 2', xy=(23,14010))

ax.vlines(x = 35, ymin = 0, ymax = 14000,\
linestyles = 'dashed', colors='k', label='Assignments 3')
ax.annotate('Assign 3', xy=(34,14010))

ax.vlines(x = 53, ymin = 0, ymax = 14000,\
linestyles = 'dashed', colors='k', label='Assignments 4')
ax.annotate('Assign 4', xy=(49,14010))

ax.vlines(x = 67, ymin = 0, ymax = 14000,\
linestyles = 'dashed', colors='k', label='Assignments 5')
ax.annotate('Assign 5', xy=(66,14010))

ax.vlines(x = 63, ymin = 0, ymax = 14000,\
linestyles = 'dashed', colors='k', label='Assignments 6')
ax.annotate('Assign 6', xy=(59,14010))

""" Annotations:
a) I selected the bin size equal to one day. The histogram took a reasonable
time to plot (~ 1 min), and the plot was visually effective.
b) Assignment 3 involved the most work based off this histogram.
Assignment 4, 5 and 6 were equally time consuming, while Assignment 0, 1 and 2
required the least amount of work (relatively speaking).
c) The amount of work rises significantly on days immediately preceding an
assignment due date. """