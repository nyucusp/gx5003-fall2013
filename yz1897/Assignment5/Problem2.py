# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:38:20 2013

@author: yilong
"""

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

params = {'axes.labelsize': 12,
          'text.fontsize': 12,
          'legend.fontsize': 12,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'text.usetex': True}

pylab.rcParams.update(params)

#path='C:/works/Dropbox/learning/CUSP Program/4 Principle of Urban Informatics/Assignment 5/'
path=''
stockfile=path+'actions-fall-2007.dat'
r = mlab.csv2rec(stockfile)
ts=r.timestamp

dt=timedelta(days=1)

t=min(ts).date()
enddate=max(ts).date()
dateset=[]
while t<=enddate :
    dateset.append(t)
    t+=dt
dateset=np.array(dateset)

s=len(ts);dist=dict([(i,0) for i in dateset])
b=dict([(1,2),(3,4)])
for i in ts:
    dist[i.date()]+=1
for d in dist:
    dist[d]=dist[d]#/float(s)
frequence=np.array(dist.values())

fig, ax = plt.subplots()
#dateset=dateset-dt/2
#print dateset[0]

# next we'll write a custom formatter
N = len(dateset)
ind = np.arange(N)  # the evenly spaced plot indices

def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return dateset[thisind].strftime('%b %d')

#plot the bars, the bar center is the middle of the day
ax.bar(ind-0.5, frequence,width=1.0,alpha=0.5)

ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()

#extend the range of x axis to make it viewable
ax.set_xlim(ind[0]-5,ind[-1]+5)


duedatesstr=['2007-09-18 12:00:00','2007-10-04 12:00:00','2007-10-25 12:00:00',\
          '2007-11-27 12:00:00','2007-12-15 12:00:00','2007-12-11 12:00:00']
#turn the due date string into datetime format
from dateutil.parser import parse
duedates=np.array([parse(i,fuzzy=True) for i in duedatesstr])

#make the annotation text
note=['Assignment '+str(i+1)+'\nDue:\ '+duedates[i].strftime('%b %d') for i in range(len(duedates))]

#the due date is write at center of the day
duepositions=[]
for j in duedates:
    for i in ind:
        if dateset[i]==j.date():
            duepositions.append(i)

ylim=ax.get_ylim()

count=0

for d in duepositions:
    ax.plot([d,d],ylim,'--',color='red',alpha=0.5)
    #change the position of the annotation
    xyt=(d-10,10500+1500*math.sin(math.pi*count*0.5))
    xy=(d,8000)
    ax.annotate(note[count],xy=xy,xycoords='data',xytext=xyt,textcoords='data',arrowprops=dict(arrowstyle='->',connectionstyle='arc,angleA=0,armA=30,rad=10'))
    count+=1



ax.set_xlabel('Date')
ax.set_ylabel('Frequence')
fig.set_size_inches(9.60,4.80)
fig.set_dpi('200')


figname=path+'Problem 2.png'

#plt.show()
plt.savefig(figname,dpi=1200)
plt.close()

'''
===========Answers=========
1. Bin of the histogram

I selected the day as the Bin of the histogram, my principle of choosing the bin is 
--keep as much information as possible
--keep the graph I draw recognizable

Given that the total time span of the data is 99 days, I think a day will be better to be a unit of the graph.

2. Hypothesis about the amount of work

I assume that the amount of work can be reflected by the number of the actions.

3. Patterns

One noticeable pattern is that the action number increase when the time is close to the due date.

 

'''