import matplotlib.pyplot as plt
import pandas as pd

myfile = pd.read_csv('stocks.dat', nrows=34, parse_dates=['month'])
pd.set_option('display.mpl_style', 'default')

pd.set_option('display.line_width', 4000)
pd.set_option('display.max_columns', 100)
#figsize(15, 6)

applePlot = myfile[['month', 'apple']]
#print myfile
#print applePlot
index = applePlot.set_index('month')
sortedIndex = index.sort()
fig = sortedIndex.plot(style = 'ro--', title = "Historical Stock Price of Apple")
plt.ylabel("Price ($)")
plt.xlabel("Month")
plt.annotate('I used red circles to clearly \nindicate actual data points', xy = ("2007-04-01",100.00), xytext = ("2007-02-01",40.00), arrowprops=dict(facecolor='black', shrink =.05))
plt.annotate('I used a dashed red line to indicate \nthe dot to dot progression, yet still \nconvey that it is inferred data', xy = ("2008-02-01",140.00), xytext = ("2007-12-01",70.00), arrowprops=dict(facecolor='black', shrink =.2))
plt.annotate('Increased size of grid on all sides \nso that no points were on the borders', xy = ("2005-12-01",150.00), xytext = ("2006-02-01",150.00), arrowprops=dict(facecolor='black', shrink =.05))
plt.annotate('Y-axis scale goes to zero to give more \naccurate impression of relative price', xy = ("2005-12-01",0.00), xytext = ("2006-02-01",20.00), arrowprops=dict(facecolor='black', shrink =.05))
plt.axis(['2005-12-25', '2008-10-10', 0, 210])
#print sortedIndex

#applePlot.set_index('month').sort_index().resample('H', how = len).plot()
fig.figure.savefig('Problem1a.png', dpi = 200)
