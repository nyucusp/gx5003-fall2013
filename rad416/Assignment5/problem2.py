import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse
from _collections import defaultdict

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

actionsFile = open('actions-fall-2007.dat','r')
next(actionsFile) #dump the header

timebinsHalfDaysDict = defaultdict(int)
for line in actionsFile:
    date = parse(line.rstrip())
    hour = date.hour
    if hour < 12:
        keyString = date.strftime('%m-%d') + " 0:00-11:59"
    else:
        keyString = date.strftime('%m-%d') + " 12:00-24:00"
    timebinsHalfDaysDict[keyString] += 1
actionsFile.close()

timeBinsHalfDaysDF = pd.DataFrame.from_dict(timebinsHalfDaysDict,orient='index')
timeBinsHalfDaysDF.columns = ['Count of actions']

timeBinsHalfDaysDF = timeBinsHalfDaysDF.sort()

n=10
ax = timeBinsHalfDaysDF[['Count of actions']].plot(kind='bar')
ticks = ax.xaxis.get_ticklocs()
ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
ax.xaxis.set_ticks(ticks[::n])
ax.xaxis.set_ticklabels(ticklabels[::n])
plt.axvline(x=14,ymin=0,ymax=12000,color='black')
plt.text(11,11500,"Assignment 0 and 1 Due",rotation=90)
plt.axvline(x=42,ymin=0,ymax=12000,color='black')
plt.text(39,11500,"Assignment 2 Due",rotation=90)
plt.axvline(x=59,ymin=0,ymax=12000,color='black')
plt.text(56,11500,"Assignment 3 Due",rotation=90)
plt.axvline(x=89,ymin=0,ymax=12000,color='black')
plt.text(86,11500,"Assignment 4 Due",rotation=90)
plt.axvline(x=115,ymin=0,ymax=12000,color='black')
plt.text(112,11500,"Assignment 5 Due",rotation=90)
plt.axvline(x=107,ymin=0,ymax=12000,color='black')
plt.text(103,11500,"Assignment 6 Due",rotation=90)
plt.legend().set_visible(False)

plt.savefig('Problem_2.png')