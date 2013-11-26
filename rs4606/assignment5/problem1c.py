import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num
import pandas as pd


stocks = pd.read_csv('stocks.dat', index_col = 'month', parse_dates = True)

apple_plot, microsoft_plot = stocks.plot(subplots = True, style = 'o-')
apple_plot.set_xlabel(' ')
apple_plot.set_ylabel('stock price')
plt.legend(loc = 'best')
apple_plot.set_title('Stock Prices, 2006-2008')



microsoft_plot.set_xlabel(' ')
microsoft_plot.set_ylabel('stock price')
plt.legend(loc = 'best')

plt.show()


"""
Superposition is better for this data (as in problem1b.py) rather than juxtaposition
(which we are doing here).  Although juxtaposition makes some of the behavior of Microsoft
stock more apparent (since we are using a different scale on the y-axis), and thereby
shows a similarity in qualitative behavior between Apple and Microsoft stocks (i.e. the 
graphs are shaped similarly), it doesn't make it obvious that Microsoft's stock price was
much lower than Apples, and that it fluctuated very little relative to the amount of 
Apple's fluctuation.
"""