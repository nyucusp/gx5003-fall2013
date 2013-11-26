import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse
from _collections import defaultdict

actionsFile = open('actions-fall-2007.dat','r')
next(actionsFile) #dump the header

timebinsDaysDict = defaultdict(int)

for line in actionsFile:
    date = parse(line.rstrip())
    timebinsDaysDict[date.strftime('%m-%d')] += 1
actionsFile.close()

timeBinsDaysDF = pd.DataFrame.from_dict(timebinsDaysDict,orient='index')
timeBinsDaysDF.columns = ['Count of actions']

timeBinsDaysDF = timeBinsDaysDF.sort()

n=5

ax = timeBinsDaysDF.plot(kind='bar')
ticks = ax.xaxis.get_ticklocs()
ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
ax.xaxis.set_ticks(ticks[::n])
ax.xaxis.set_ticklabels(ticklabels[::n])

plt.savefig('Problem_2.png')