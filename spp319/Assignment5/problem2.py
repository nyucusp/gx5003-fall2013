import matplotlib.pyplot as plt
import pylab as P
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

pd.set_option('display.mpl_style', 'default')

# Display all the columns instead of a summary
pd.set_option('display.line_width', 4000)
pd.set_option('display.max_columns', 100)

orig_data = pd.read_csv('actions-fall-2007.dat',nrows=132132 , parse_dates=['timestamp'])
entries = orig_data[['timestamp']]
entries = entries.sort()
#dataframe which will hold the dates of actions and the number of actions on that date
df = {}
#The end of the first time period on actions. This will be used to separate the bins.
endDay = datetime.strptime('2007-09-16 11:59:00', '%Y-%m-%d %X')
actionCounter = 0

fig, ax = plt.subplots()

binDates = []
data = []
bins = []
allDates = []

for row in entries['timestamp']:
    if endDay > row:
        actionCounter += 1
        df[endDay] = actionCounter
    else:
        allDates.append(endDay)

        while (row + timedelta(hours = 24)) < (endDay + timedelta(hours = 24)):
            print "is true"
            endDay = endDay + timedelta(hours = 24)

        actionCounter = 1
        endDay = endDay + timedelta(hours = 24)
        df[endDay] = actionCounter

#To inspect all keys and values in the dictionary/dataframe
counter = 0
for item in df:
    data.append(item)
    data.append(df.get(item))
    binDates.append(item)
    bins.append(data[counter])
    counter += 1

#print len(df) 94 entries in dataframe (bins)

X = np.arange(len(df))
P.bar(X, df.values(), align='center', width=0.5)
P.xticks(X, df.keys())
ymax = max(df.values()) + 1
P.ylim(0, ymax)
P.show()

#Plot duedates vertical lines
assignments = ['2007-09-18 12:00:00', '2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-15 12:00:00', '2007-12-11 12:00:00']
assignments = pd.to_datetime(assignments)
# assignments = date2num(assignments)
P.vlines(assignments, 0, 16000, color='0.35', zorder=10, linestyle='--', linewidth=1)

plt.savefig('Problem2.png', dpi=300)
