# Import packages                                                                                        

import matplotlib.pyplot as plt
import numpy as np
import scipy
import pandas as pd
import matplotlib.mlab as mlab
from  matplotlib.ticker import MultipleLocator
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter, date2num, num2date
import pylab
from datetime import timedelta
from datetime import datetime
import math

params = {'axes.labelsize': 12, 'text.fontsize': 12, 'legend.fontsize': 12, 'xtick.labelsize': 10, 'ytick.labelsize': 10, 'text.usetex': True}

pylab.rcParams.update(params)

actionsFile = pd.read_table('/Users/JSAdams/Downloads/Hw1data/actions-fall-2007.dat', sep = ',')
actionsFile['timestamp'] = pd.to_datetime(actionsFile['timestamp'])
actionsFile['timestamp'] = date2num(actionsFile['timestamp'])

fig, ax = plt.subplots()

ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('%B'))
ax.yaxis.set_major_locator(MultipleLocator(2500))

# Set limits
xmin = pd.to_datetime('2007-09-02')
xmax = pd.to_datetime('2007-12-20')
ax.set_xlim(xmin, xmax)
ax.set_ylim(1, 16000)

ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

h_lines = [5000, 10000, 15000]
ax.hlines(h_lines, xmin, xmax, color='0.85', zorder=1, linestyle=':')

datesDue = ['2007-09-18 12:00:00', '2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-15 12:00:00', '2007-12-11 12:00:00']
datesDue = pd.to_datetime(datesDue)
datesDue = date2num(datesDue)
ax.vlines(datesDue, 0, 16000, color='0.35', zorder=10, linestyle='--', linewidth=1)

labels = ["Assignment " + str(x) for x in range (0, 7)]
labels[0] = labels[0] + ",\nAssignment 1"
counter = 0
for date in datesDue:
    if counter != 1 and counter != 5:
        ax.text(date-1, 15500, labels[counter] + "\ndue", ha='right', va='top', multialignment='right', color='0.35', fontsize=10)
    counter += 1
ax.text(datesDue[5]+1, 15500, labels[5] + "\ndue", ha='left', va='top', color='0.35', fontsize=10)

base = str(num2date(actionsFile['timestamp'].min()))
noon = ' 12:00:00+00:00'
base = base.split(' ')[0] + noon
base = date2num(pd.to_datetime(base))
binList = [ base + i for i in range(0,99) ]

plt.hist(actionsFile['timestamp'], binList, histtype='stepfilled', color='green', zorder=2, ec='none')

t = ax.set_title('Actions, 2007.')
t.set_y(1.03)
ax.set_ylabel('Number of Actions')
ax.set_xlabel('Due Dates')
plt.subplots_adjust(left=.11, top=.9, right=.95, bottom=.13)
plt.savefig('Problem 2.png')
plt.show()
plt.close()

"""
I chose bins for 24 hour periods from noon to noon since the due dates were
all at noon.

Assignments 3, 4, and 5 required more actions that assignments 1, 3, and 6.
This could indicate that the former were more difficult than the latter.

The number of actions is greatest on both sides of the deadline. For assign-
ments 1, 4, 5, 6, the greatest number of actions were committed in the 24 hours
before the due date; for assignments 2 and 3 the greatest number of actions
were committed in the 24 hours after the due date.

"""
