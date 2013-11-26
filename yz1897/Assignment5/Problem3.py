# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:42:26 2013

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
          'xtick.labelsize': 7,
          'ytick.labelsize': 5,          
          'text.usetex': True}

pylab.rcParams.update(params)

#path='C:/works/Dropbox/learning/CUSP Program/4 Principle of Urban Informatics/Assignment 5/'
path=''
stockfile=path+'microprocessors.dat'
r = mlab.csv2rec(stockfile)

name=r.processor
y=r.year_of_introduction
s=r.transistors

#sort by year
sorting=[(y[i],name[i],s[i]) for i in range(len(name))]
sorting.sort()
y=np.array([i[0] for i in sorting])
name=np.array([i[1] for i in sorting])
s=np.array([i[2] for i in sorting])
rank=np.arange(len(y))


fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)


fig.set_dpi(600)
fig.set_size_inches(7.20,3.60)
fig.subplots_adjust(left=0.18, bottom=None, right=0.95, top=None, wspace=0.08, hspace=None)
ax1.plot(y, rank, 'o',color='red',label='Year')#plot apple stock


#set the x and y labels
ax1.set_xlabel('Year')
ax1.set_ylabel('Processor')


#set x ticks
ax1.set_ylim(-0.5,12.5)
ax1.set_yticks(rank)
ax1.set_yticklabels(name)

#set the layout of the figure object
fig.autofmt_xdate()


#set the location of  legend as top left
ax1.legend(loc=2)

#plot the microsoft stock
ax2.plot(s, rank, 'o',color='blue',label='Transistors')

#eye guiding line for 0

ax2.set_xlabel('Transistors')
ax2.set_xscale('log')

figname=path+'Problem 3.png'

plt.legend(loc=2)
plt.savefig(figname,dpi=1200)
plt.close()
'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
    I changed the range of y axis, so as to make the baselines in two graph in the same hight, this will make the viewers easize to comparison, also, I adjusted the vertical space between 
    two subplot.
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    Default setting
'''
