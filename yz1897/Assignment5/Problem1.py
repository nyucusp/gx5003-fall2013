# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:40:29 2013

@author: yilong
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pylab

params = {'axes.labelsize': 12,
          'text.fontsize': 12,
          'legend.fontsize': 12,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'text.usetex': True}

pylab.rcParams.update(params)


#read the data
path=''
stockfile=path+'stocks.dat'
r = mlab.csv2rec(stockfile)
r.sort()

#question a

fig, ax = plt.subplots()
ax.plot(r.month, r.apple, 'o-')
fig.autofmt_xdate()
plt.xlabel('Time')
plt.ylabel('Apple\'s Stock')
figname=path+'Problem 1a.png'
plt.savefig(figname,dpi=1200)
plt.close()
'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
    Default setting.
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    Default setting
'''


#question b
fig,ax = plt.subplots()
stocka=r.apple-r.apple[0]
stockm=r.microsoft-r.microsoft[0]
ax.plot(r.month, stocka, 'o-',label='Apple',alpha=0.5)
ax.plot(r.month, stockm, 'o-',label='Microsoft',alpha=0.5)
fig.autofmt_xdate()
plt.xlabel('Time')
plt.ylabel('Relative Price')
figname=path+'Problem 1b.png'
plt.legend(loc=0)
plt.savefig(figname,dpi=1200)
plt.close()
'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
    Default setting.
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    I used the transparancy setting to make superposed viewable.
'''


#question c

stocka=r.apple-r.apple[0]
stockm=r.microsoft-r.microsoft[0]

fig, (ax1,ax2) = plt.subplots(1,2,sharey=False)

#set the layout of the figure object
fig.autofmt_xdate()
fig.set_dpi(1200)
fig.set_size_inches(9.60,3.60)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.08, hspace=None)
ax1.plot(r.month, stocka, 'o-',color='red',label='Apple')#plot apple stock

#eye guiding line for 0
ax1.plot([r.month[0],r.month[-1]],[0,0],'--',color='green')

#set the x and y labels
ax1.set_xlabel('Time')
ax1.set_ylabel('Relative Price')

#adjust the y axis area so that the two fig are matched at y=0
ax1.set_ylim(-50,150)

#set the location of  legend as top left
ax1.legend(loc=2)

#plot the microsoft stock
ax2.plot(r.month, stockm, 'o-',color='blue',label='Microsoft')

#eye guiding line for 0
ax2.plot([r.month[0],r.month[-1]],[0,0],'--',color='green')

ax2.set_xlabel('Time')
ax2.set_ylim(-10,30)


figname=path+'Problem 1c.png'

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
    two subplot. On the other hand, the size of the merged graph is adject in to a 16:6 rectangle (which is 16:9 as default.)
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    I used the transparancy setting to make superposed viewable.
'''

#plt.show()