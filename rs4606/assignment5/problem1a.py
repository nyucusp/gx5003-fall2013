import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num
import pandas as pd


stocks = pd.read_csv('stocks.dat', index_col = 'month', parse_dates = True)
apple_plot = stocks.plot(y='apple', style = 'o-', label='Apple')
apple_plot.set_xlabel(' ')
apple_plot.set_ylabel('stock price')
plt.legend(loc = 'best')
apple_plot.set_title('Apple Stock Prices, 2006-2008')
plt.show()


"""
To make this a clear plot I kept the following ideas in mind:
-not to have too many labels on either axis
-to have the data clear and visible (blue dots, not too many)
-to have a lot of white space
-to have the background be white.
"""