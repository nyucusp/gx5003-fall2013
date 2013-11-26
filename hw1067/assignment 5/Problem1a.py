# -*- coding: utf-8 -*-
#Haozhe Wang
#Assignment 5
#Problem 1 A

import pandas as pd
import csv
import pylab
import numpy as np

stockfile = pd.read_csv('stocks.dat')#read the file with pandas call function
#print stockfile
apple_stock = stockfile[['month','apple']]


index = apple_stock.set_index('month')
#print index

right_timeseq = index.sort()

prefig = right_timeseq.plot(legend = True, style = "c*--")
#configure the plot
prefig.set_title('Is Apple still a buy?')
prefig.xaxis.grid(True, which="minor")
prefig.xaxis.grid(True, which="major")
prefig.set_ylabel('Price')
prefig.set_xlabel('Month')
prefig.annotate('Used Pandas and matplotlib to sort\n "month" as index, and configured\n other factors a little bit.', xy=(16,75))
plt.tight_layout()


prefig.figure.savefig('Apple Stock Pricetest.jpg',dpi = 300)

"""
tried my best to space the plot properly. Everything is labeled with legend in the right place.
Didn't change the default font size since it seems okay on the plot.
"""
