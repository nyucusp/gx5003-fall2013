from pylab import *

stockFile = open('stocks.dat','r')
dateList = []
AppleList = []
MicrosoftList = []
stockFile.readline()

#traverse stock data file to create lists of apple and microsoft data

for line in stockFile:
    thisDate = line.split(',')[0]
    thisYear = thisDate.split('-')[0]
    thisMonth = thisDate.split('-')[1]
    thisDate = datetime.date(int(thisYear), int(thisMonth), 1)
    thisAppleStock = line.split(',')[1]
    thisMicrosoftStock = line.split(',')[2]
    dateList.append(thisDate)
    AppleList.append(thisAppleStock)
    MicrosoftList.append(thisMicrosoftStock)

fig, ax = plt.subplots(1)
ax.plot(dateList, AppleList)

#create first figure of line chart for apple prices

fig.autofmt_xdate()
plt.title('Apple (AAPL) Stock Price')
plt.xlabel('Month')
plt.ylabel('Price ($)')
plt.savefig('Problem 1a.png')
#show()

#create second figure of line chart for microsoft vs. apple prices in one plot

fig2, ax2 = plt.subplots(1)
ax2.plot(dateList, AppleList, 'r-', label='APPL')
ax2.plot(dateList, MicrosoftList, 'g-', label = 'MSFT')
ax2.legend(loc = 2)
fig2.autofmt_xdate()
plt.title('Apple (AAPL) vs. Microsoft (MSFT)  Stock Price')
plt.xlabel('Month')
plt.ylabel('Price ($)')
plt.savefig('Problem 1b.png')
#show()

#create third figure of 2 line charts for apple vs. microsoft sharing x axis

fig3, ax3 = plt.subplots(2, sharex = True)
ax3[0].plot(dateList, AppleList, 'r-', label = 'AAPL')
#red line for apple
ax3[1].plot(dateList, MicrosoftList, 'g-', label = 'MSFT')
#green line for microsoft
ax3[0].legend(loc=2)
plt.ylabel('Price ($)')
ax3[1].legend(loc=2)
#legend to show which stock each line represents
plt.ylabel('Price ($)')
fig3.autofmt_xdate()
plt.savefig('Problem 1c.png')
#show()
