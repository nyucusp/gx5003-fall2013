# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:12:52 2013

@author: yilong
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
import os,sys
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pylab
from datetime import timedelta
from datetime import datetime
import math
from numpy import polyfit, polyval

def Computlinearpara(x,y,ran='no'):
    '''returns the linear parameter of two arrays, y=a+bx r is the 
    linear-correlation '''
    n=len(x)
    if ran!="no":
        xraw=x;yraw=y
        for i in range(0,n):
            if xraw[i]>=ran[0] and xraw[i]<=ran[1]:
                x.append(xraw[i])
                y.append(yraw[i])
        n=len(x)
    xa=float(sum(x))/float(n)
    ya=float(sum(y))/float(n)
    lxy=0.0;lxx=0.0;lyy=0.0
    for i in range(0,n):
        lxx+=x[i]*x[i]
        lxy+=x[i]*y[i]
        lyy+=y[i]*y[i]
    lxy-=n*xa*ya
    lxx-=n*xa*xa
    lyy-=n*ya*ya
    b=lxy/lxx
    a=ya-xa*b
    r=lxy/(sqrt(lxx)*sqrt(lyy))
    return a,b,r


params = {'axes.labelsize': 12,
          'text.fontsize': 12,
          'legend.fontsize': 12,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'text.usetex': True}

pylab.rcParams.update(params)

#path='C:/works/Dropbox/learning/CUSP Program/4 Principle of Urban Informatics/Assignment 5/'
path=''
stockfile=path+'genes.dat'
r = mlab.csv2rec(stockfile)


#========Problem 4a====================

plt.subplot(221)
plt.plot(r.a, r.b,'or',alpha=0.5)
plt.xlabel('Gene A')
plt.ylabel('Gene B')


plt.subplot(222)

plt.plot(r.a, r.c,'ob',alpha=0.5)
plt.xlabel('Gene A')
plt.ylabel('Gene C')
plt.subplot(223)

plt.plot(r.a, r.d,'og',alpha=0.5)
plt.xlabel('Gene A')
plt.ylabel('Gene D')

plt.subplots_adjust(left=0.1,right=0.95,top=0.95,wspace=0.25,hspace=0.25)
plt.savefig('Problem 4a.png')

#plt.show()
plt.close()


'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
    I adjusted the distance of the subplots and the marginal width.
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    No overlapping default setting
'''

#========Problem 4b===============
#linear best fitting between A,C

a,b,c=Computlinearpara(r.a,r.c)

plt.plot(r.a, r.c,'o',alpha=0.5,label='Data')
fity=a+b*r.a

plt.plot(r.a, fity,'-',alpha=0.5,label='Linear Fit')
plt.xlabel('Gene A')
plt.ylabel('Gene C')
plt.legend(loc=2)

plt.show()
plt.savefig('Problem 4b.png')

plt.close()
'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
   Default setting
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    No overlapping default setting
'''

#========Problem 4c===============
#linear best fitting between A,D


plt.plot(r.a, r.d,'o',alpha=0.5,label='Data')


coeffs = polyfit(r.a, r.d, 3)
newx = sorted(r.a)
fity= polyval(coeffs, newx)


plt.plot(newx, fity,'-',alpha=0.5,label='Cubic Fit')
plt.xlabel('Gene A')
plt.ylabel('Gene D')
plt.legend(loc='best')

plt.savefig('Problem 4c.png')

plt.close()




'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
   Default setting
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    No overlapping default setting
'''

#========Problem 4d===============
#linear best fitting between A,B




plt.plot(r.a, r.b,'o',alpha=0.5,label='Data')




coeffs = polyfit(r.a, r.b, 5)
fity= polyval(coeffs, newx)


plt.plot(newx, fity,'-',alpha=0.5,label='Poly Fit')
plt.xlabel('Gene A')
plt.ylabel('Gene B')
plt.legend(loc='best')

plt.savefig('Problem 4d.png')

plt.close()





'''
Visualization Principles
1. Make data stand out
    Default setting
2. Visual prominence
    I adjucted all the fontsizes of the stickes, labels and legends, to ensure the simbles and texts in the image eazy to recognize even when people are reading a smaller version
3. Scale lines and the data rectangle
   Default setting
4. Reference lines, labels, notes, and keys
    Default setting
5. Superposed data sets
    No overlapping default setting
'''
