from pylab import *

stockFile = open('stocks.dat','r')
dateList = []
AppleList = []
MicrosoftList = []
stockFile.readline()
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

fig.autofmt_xdate()
plt.title('Apple (AAPL) Stock Price')
plt.xlabel('Month')
plt.ylabel('Price ($)')
plt.savefig('Problem 1a.png')
#show()

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

fig3, ax3 = plt.subplots(2, sharex = True)
ax3[0].plot(dateList, AppleList, 'r-', label = 'AAPL')
ax3[1].plot(dateList, MicrosoftList, 'g-', label = 'MSFT')
ax3[0].legend(loc=2)
plt.ylabel('Price ($)')
ax3[1].legend(loc=2)
plt.ylabel('Price ($)')
fig3.autofmt_xdate()
plt.savefig('Problem 1c.png')
#show()
