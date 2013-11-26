from pylab import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import pyplot

dates = []
apple = []
microsoft = []
with open('stocks.dat','r') as f:
    f.next()
    for row in f:
        a = row.strip('\n').split(',')
        dates.append(a[0])
        apple.append(a[1])
        microsoft.append(a[2])

#changes the dates to strings
a = [datetime.datetime.strptime(str(date),'%Y-%m') for date in dates]

#creates the figure and the subplot
fig = plt.figure()
plt.title("Apple and Microsoft stock price relative to Jan 2006",fontsize=15)
ax1 = plt.subplot(211,xlim=(datetime.datetime(2005,12,31,0,0),datetime.datetime(2008,9,2,0,0)),ylim=(0,205))
plt.plot(a, apple, 'o-', label = 'Apple')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gcf().autofmt_xdate()
plt.legend(loc=2)
plt.ylabel('Stocks')
plt.grid()


ax2 = plt.subplot(212,xlim=(datetime.datetime(2005,12,31,0,0),datetime.datetime(2008,9,2,0,0)),ylim=(0,50))
plt.plot(a, microsoft, 'o-', color='red', label = 'Microsoft')

#Formats the date 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.gcf().autofmt_xdate()


plt.legend(loc=2)
plt.xlabel('Date')
plt.ylabel('Stocks')

#shows grids
plt.grid()

#plot
pyplot.savefig('problem 1c.png', dpi=200)
plt.show()


Annotation=[
'  Juxtaposition is a lot better then superposition and also axes can be adjusted to see',
'  the fluctuations between lines. (if they are similar e.g.)',
'  Graphs are plotted on a grid screen in order to read values clearly',
'  Maximum and minimum values are shown',
'  There is a legend to explain the data.',
'  Date is formatted in a way that looks better.(every 3 months)'
]

