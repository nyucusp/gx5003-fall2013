#!/usr/bin/env python

import numpy as np
import pylab as pl
import pandas as pd
from matplotlib import ticker
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
from random import shuffle
import csv
from sklearn.cross_validation import KFold

data1 = pd.read_csv('RTrees10fold.csv')
data2 = pd.read_csv('KNearest10fold.csv')
data3= pd.read_csv('Mlp10fold.csv')
data4 = pd.read_csv('Boost10fold.csv')

models=[1,2,3,4]
labels=['R Trees', 'K Nearest', 'MLP', 'Boost']
means=[data1.mean(0)[1],data2.mean(0)[1],data3.mean(0)[1],data4.mean(0)[1]]
stds=[data1.std(0)[1],data2.std(0)[1],data3.std(0)[1],data4.std(0)[1]]


plt.figure()
plt.errorbar(models,means,yerr=stds,label='Standard Deviation',color='g',linestyle='-.', linewidth=1.5)
#plt.plot(degrees,fts,label='Full model',color='r', linewidth=2.0)
plt.xlim(0,6)
#plt.ylim(9000,19000)
plt.xlabel('Models')
plt.ylabel('Percent Accuracy')
plt.xticks(models,labels)
plt.title('Letter Recognition Classification Methods')
plt.ylim(.7,1)
plt.grid()
plt.legend( loc='upper left' )
plt.savefig('Classification_Method_Comparison.png',dpi = 300)
