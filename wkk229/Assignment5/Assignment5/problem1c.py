import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

myfile = pd.read_csv('stocks.dat', nrows=34, parse_dates=['month'])
pd.set_option('display.mpl_style', 'default')
#figsize(15, 6)
pd.set_option('display.line_width', 4000)
pd.set_option('display.max_columns', 100)

stockPlotA = myfile[['month', 'apple']]
stockPlotM = myfile[['month', 'microsoft']]

#print myfile
#print applePlot
index = stockPlotA.set_index('month')
index2 = stockPlotM.set_index('month')
#sort by month
sortedIndex = index.sort()
sortedIndex2 = index2.sort()
#create dict to grab first elements
# stockDict = {}
#start time is first key
beginning = datetime.strptime('2006 01 01', '%Y %m %d')
appleBase = sortedIndex.get_value(beginning, "apple")
microBase = sortedIndex2.get_value(beginning, "microsoft")


fig = sortedIndex.plot(style = 'bo--', title = "Historical Stock Price of Apple and Microsoft")
fig = sortedIndex2.plot(style = 'ro-.', title = "Historical Stock Price of Apple and Microsoft")
plt.axhline(linewidth=2, color='black')
plt.ylabel("Price ($)")
plt.xlabel("Month")
plt.annotate('I used red circles to clearly \nindicate actual data points', xy = ("2007-04-01",100.00), xytext = ("2007-02-01",40.00), arrowprops=dict(facecolor='black', shrink =.05))


plt.axis(['2005-12-25', '2008-10-10', -20, 210])
#print sortedIndex

#applePlot.set_index('month').sort_index().resample('H', how = len).plot()
fig.figure.savefig('Problem1c.png', dpi = 300)
##When using juxtaposition, you can see that Microsoft and Apple
 #had similar patterns of ups and downs, but in the previous plot
 #Microsoft almost looked like  a straight line 
 #as dramatic as Apple's, but actually was very similar
 #For this data juxtaposition is a better technique to use because you don't lose Microsoft's trend pattern, which was lost in the superposition graph
