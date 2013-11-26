# -*- coding: utf-8 -*-
#Assignment 5
#Problem1 C
#Haozhe Wang

import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt


stockfile = pd.read_csv('stocks.dat', parse_dates = True)#read the file with pandas call function
#print stockfile
apple_stock = stockfile[['month','apple']]
microsoft_stock = stockfile[['month','microsoft']]


index1 = apple_stock.set_index('month')
index2 = microsoft_stock.set_index('month')


Sindex1 = index1.sort()
Sindex2 = index2.sort()
#print Sindex2


#plot apple in the subplot211
fog = plt.figure(figsize = (12,6), dpi = 300)
ax1 = plt.subplot(211)
plt.plot(Sindex1)
plt.annotate("USD75.51 in\n Jan 2006",xy=(24,84),fontsize = 10, color = "g")#annotate the baseline with font size 10 on top of the actual line in green 
plt.xticks(arange(35,0,-1),apple_stock.month[:35], rotation = 90, fontsize = 8)
ax1.set_autoscale_on(False)
plt.axhline(y = 75.51, color = "k")
plt.tight_layout()


#plot MSFT in subplot212
ax2 = plt.subplot(212)
plt.plot(Sindex2)
plt.annotate("USD27.06 in\n Jan 2006",xy=(28,28.5),fontsize = 10, color = "b")
plt.axhline(y = 27.06, color = "k")
plt.xticks(arange(0,35),microsoft_stock.month[:35
                                              ], rotation = 90, fontsize = 8)

fog.savefig('juxMandA.jpg',dpi = 300)

"""
I had problems cleaning up this chart:
I can't get the x-ticks to work right. It is obvious that I got either inversed x-ticks or fliped x-ticks(after trying to fix the inversed issue)
These co-existing problems  had taken too much of my time(like half a day, I try different approaches: \n plot the two at the same time with pandas by allowing subplot, then I wouldn't be able to tweak the details)
Please give this work some credit, I tried more than two  ways, and this one is so close to geting things done with matplotlib. Thank you.
"""

