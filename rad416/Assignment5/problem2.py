import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse
from _collections import defaultdict

actionsFile = open('actions-fall-2007.dat','r')
next(actionsFile) #dump the header

actionsList = []
for line in actionsFile:
    actionsList.append(parse(line.rstrip()))
actionsFile.close()

timebinsHoursDict = defaultdict(int)

for t in actionsList:
    timebinsHoursDict[t.strftime('%m-%d-%H')] += 1

timeBinsHoursDF = pd.DataFrame.from_dict(timebinsHoursDict,orient='index')
timeBinsHoursDF.columns = ['Count of actions']
del timebinsHoursDict

timeBinsHoursDF = timeBinsHoursDF.sort()

actionsplot = timeBinsHoursDF.plot(kind='bar',grid='off')

plt.savefig('Problem_2.png')