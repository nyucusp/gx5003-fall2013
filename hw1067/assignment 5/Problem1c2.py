# -*- coding: utf-8 -*-
#just a trail 
#Haozhe Wang

import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt


stockfile = pd.read_csv('stocks.dat')#read the file with pandas call function
#print stockfile

index = stockfile.set_index('month')
#print index


right_timeseq = index.sort()

#fig = plt.figure(figsize=(8,5))
#fig, axes = plt.subplots(nrows=1, ncols=2)
fog = right_timeseq.plot(subplots = True,legend = True, style = "c^--")
#prefig1 = right_timeseq['apple'].plot(ax=axes[0,0]); plt.legend(loc='best')
#axes[0,0].set_title('Apple')
#configure the plot
#plt.xaxis.grid(True, which="minor")
#prefig.xaxis.grid(True, which="major")
plt.ylabel('Price')
plt.xlabel('Month')
#prefig.set_title('MSFT vs. AAPL')
#prefig.annotate('Used Pandas and matplotlib to sort\n "month" as index, and configured\n other factors a little bit.', xy=(16,75))
plt.tight_layout()
#plt.axhline(y = 27.06, color = "k")
#plt.axhline(y = 75.51, color = "k")

#plt.annotate("USD27.06 in\n Jan 2006",xy=(28,38),fontsize = 10, color = "g")#annotate the baseline with font size 10 on top of the actual line in green 
#plt.annotate("USD75.51 in\n Jan 2006",xy=(28,84),fontsize = 10, color = "b")


