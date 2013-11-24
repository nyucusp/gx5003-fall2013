import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num
import pandas as pd


stocks = pd.read_csv('stocks.dat', index_col = 'month', parse_dates = True)
apple_plot = stocks.plot(style = 'o-')
apple_plot.set_xlabel(' ')
apple_plot.set_ylabel('stock price')
plt.legend(loc = 'best')
apple_plot.set_title('Apple and Microsoft Stock Prices, 2006-2008')
plt.show()


"""
Microsoft's stock prices are much lower than Apple's, and also fluctuated much less. 
While Apple's price rose dramatically toward the end of 2007 and then fell sharply, 
Microsoft's price change was very small.
"""