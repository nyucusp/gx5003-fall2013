import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

myfile = pd.read_csv('stocks.dat', nrows=34, parse_dates=['month'])
pd.set_option('display.mpl_style', 'default')

pd.set_option('display.line_width', 4000)
pd.set_option('display.max_columns', 100)
#figsize(15, 6)
stockPlot = myfile[['month', 'apple', 'microsoft']]


#print myfile
#print applePlot
index = stockPlot.set_index('month')
#sort by month
sortedIndex = index.sort()
#create dict to grab first elements
# stockDict = {}
#start time is first key
beginning = datetime.strptime('2006 01 01', '%Y %m %d')
appleBase = sortedIndex.get_value(beginning, "apple")
microBase = sortedIndex.get_value(beginning, "microsoft")
# for items in sortedIndex.iterkv():
#     for prices in items[1]:
#         prices = prices - appleBase
# map to adjust to baseline,


fig = sortedIndex.plot(style = ['bo--', 'ro-.'], title = "Historical Stock Price of Apple and Microsoft")
plt.axhline(linewidth=2, color='black')
plt.ylabel("Price ($)")
plt.xlabel("Month")
plt.annotate('I used blue circles to clearly \nindicate actual data points', xy = ("2007-04-01",100.00), xytext = ("2007-02-01",40.00), arrowprops=dict(facecolor='black', shrink =.05))
x = 0
def f(x):
    x = x - appleBase
    return x
#sortedIndex.apply(f(x), axis=1)

plt.axis(['2005-12-25', '2008-10-10', -20, 210])
#print sortedIndex

#applePlot.set_index('month').sort_index().resample('H', how = len).plot()
fig.figure.savefig('Problem1b.png', dpi = 200)
