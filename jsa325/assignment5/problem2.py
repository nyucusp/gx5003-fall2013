# Import packages                                                                                        

import matplotlib.pyplot as plt
import numpy as np
import scipy
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pylab
from datetime import timedelta
from datetime import datetime
import math

params = {'axes.labelsize': 12, 'text.fontsize': 12, 'legend.fontsize': 12, 'xtick.labelsize': 10, 'ytick.labelsize': 10, 'text.usetex': True}

pylab.rcParams.update(params)

actionsFile = open('/Users/JSAdams/Downloads/Hw1data/actions-fall-2007.dat', 'r')
r = mlab.csv2rec(actionsFile)
ts = r.timestamp

dt = timedelta(days=1)
t = min(ts).date()
endDate = max(ts).date()

setDate = []
while t < endDate:
    setDate.append(t)
    t += dt
setDate = np.array(setDate)

s = len(ts)
dist = dict([(i,0) for i in setDate])
b = dict([(1,2),(3,4)])

for i in ts:
    dist[i.date()]+=1
for d in dist:
    dist[d] = dist[d]
actions = np.array(dist.values())

fig, ax = plt.subplots()

N = len(setDate)
ind = np.arange(N)

def dateFormat(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return setDate[thisind].strftime('%b %d')

ax.bar(ind-0.5, actions, width=1.0, alpha=0.5)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(dateFormat))
fig.autofmt_xdate()

ax.set_xlim(ind[0]-5, ind[-1]+5)

strDue = ['2007-09-18 12:00:00','2007-10-04 12:00:00','2007-10-25 12:00:00','2007-11-27 12:00:00','2007-12-15 12:00:00','2007-12-11 12:00:00']
from dateutil.parser import parse
datesDue = np.array([parse(i, fuzzy=True) for i in strDue])

posDue = []
for j in datesDue:
    for i in ind:
        if setDate[i] == j.date():
            posDue.append(i)

ylim = ax.get_ylim()

count = 0

for d in posDue:
    ax.plot([d,d],ylim,'--',color='red',alpha=0.5)
    xyt = (d-10,10500+1500*math.sin(math.pi*count*0.5))
    xy = (d,8000)
    count += 1

ax.set_xlabel('Date')
ax.set_ylabel('Actions')
fig.set_size_inches(9.60,4.80)
figname = 'Problem2.png'
plt.savefig(figname)
plt.show()
plt.close()
