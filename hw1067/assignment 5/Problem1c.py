# -*- coding: utf-8 -*-
# Haozhe Wang
#Assignment 5
# Problem 1c

import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt
import numpy
from matplotlib.dates import date2num
import datetime

# <codecell>

stockfile = pd.read_csv('stocks.dat', parse_dates = True, index_col = 'month')#read the file with pandas call function

apple_ax,microsoft_ax = stockfile.plot(subplots = True, style = 'co--')
#Apple subplot
apple_ax.set_xlabel(' ')
apple_ax.set_ylabel('Stock Price')
apple_ax.legend(loc = 'best')
apple_ax.axhline(y = 75.51, color ="k")# to see changes made since fisrt month
#apple_ax.annotate("Price at USD75.51",xy = (2,22))
apple_ax.set_title('AAPL vs. MSFT Stock Prices 2006-2008')

#Microsoft subplot
microsoft_ax.set_xlabel('Month')
microsoft_ax.set_ylabel('Stock Price')
plt.axhline(y = 27.06, color ="k")
plt.legend(loc = 'best')
plt.tight_layout()

plt.show()


"""
the only difference between this plot and the plot in 1b is we can see the fluctuation better, especially for Microsoft. The stock offers sweet \n divident; therefore, the longterm price change is very minimal. The juxatposition plot gives plots like Microsoft more room to show the real change. 
Normally, I would put secondary y axis on, but, since the two do not vary much (less than a factor of 10 here, I would say), I would still them in the same scale.
As can be seen in ths plot, Microsoft went down around May 2006 and went back up in Nov 2007, which is hard to indentify in the superposition plot.
"""