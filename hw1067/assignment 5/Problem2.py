# -*- coding: utf-8 -*-
#Haozhe Wang
#Assignment 5
#Problem 2
# <nbformat>3.0</nbformat>

# <codecell>

#cd documents/python learning/hw1data

# <codecell>

import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as date
from matplotlib.dates import date2num, MonthLocator, DateFormatter

# <codecell>

action = []
actions = open('actions-fall-2007.dat','r')
next(actions)
for i in actions:
    action.append(i)
#del action[0]

# <codecell>

daytime = []
for j in action:
    a = dt.datetime.strptime(j.strip(),'%Y-%m-%d %H:%M:%S')
    b = date.date2num(a)
    daytime.append(b)
# Find the number of bins
a = max(daytime)-min(daytime)
binnum = int(a)+1

# <codecell>

begin = date.date2num(dt.datetime.strptime('2007-09-10 12:00:00','%Y-%m-%d %H:%M:%S'))
final = date.date2num(dt.datetime.strptime('2007-12-18 12:00:00','%Y-%m-%d %H:%M:%S'))
plt.hist(daytime, bins = binnum, color = 'c', range = (begin ,final ))
#plt.figure()
plt.gca().xaxis.set_major_locator(MonthLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter('%B'))
plt.ylabel('Number of Actions')
plt.title('HW submission Activity by 24hr period')

# <codecell>

deadlines = ['2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-11 12:00:00','2007-12-15 12:00:00']
deadtime = []
for k in deadlines:
    deadtime.append(dt.datetime.strptime(k, "%Y-%m-%d %H:%M:%S"))
    labels = ['Due Zero and One', 'Due Two', 'Due Three', 'Due Four', 'Due Six', 'Due Five']
    loc= ('best')
for l in range(0, 6):
    plt.text(deadtime[l],10000 + 1000*l,labels[l],rotation=0, size='small')
plt.vlines(date2num(deadtime), 0, 16000, color = 'b',linestyle = 'dashed' )
plt.savefig("Problem 2.png",dpi = 300)

# <codecell>

# (a)The bins are set as 24hr peroid beginning at 00:00 and ends at 24:00(12:00:00 in this dat file records).
# (b)HW3 and HW5 had the most work load that students had to finish in very short time. They also needed more time because most of the submission happened after due.
# (c) most submissions were made the day before and after the due(plus or munis 24hrs from due time); close to final week(HW5), more people tried to submit before the due.