import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('stocks.dat')
stocks['appleDelta'] = stocks['apple'].map(lambda x: x-75.51) # apply map to subtract stock price on Jan 2006
stocks['microsoftDelta'] = stocks['microsoft'].map(lambda x: x-27.06)

# generate plot for problem 1a
# The plot uses a connected symbol to make clear these are discrete measurements rather than continuous measurements
# Grid lines are used to make the graph clear to read.
stocksApple = stocks[['month','apple']]
stocksApple.columns = ['Month (01-2006 to 09-2008)', 'Apple']
appleplot = stocksApple.set_index('Month (01-2006 to 09-2008)').sort_index().plot(style='o--',ylim=[40,220],title="Apple Stock Price - Problem 1a",legend=False)
plt.savefig('Problem_1a.png')

# generate plot for problem 1b
stocksDelta = stocks[['month','appleDelta', 'microsoftDelta']]
stocksDelta.columns = ['Month (01-2006 to 09-2008)','Apple','Microsoft']
deltaPlot = stocksDelta.set_index('Month (01-2006 to 09-2008)').sort_index().plot(style='o--',title="Apple and Microsoft Stock Price (diff from Jan 2006 baseline) - Problem 1b")
plt.axhline(y=0.0, color='black')
# Two connected symbol graphs of different colors show the two stock prices. A horizontal line at x=0 makes clear
# the zero mark.  This clearly shows the price difference over the baseline price in real dollar terms.  
# Change as some percentage of the initial stock price might be more accurate, as well as an indication whether these
# are inflation adjusted dollars.
plt.savefig('Problem_1b.png')

# generate plot for problem 1c
stocksDelta = stocks[['month','appleDelta', 'microsoftDelta']]
stocksDelta.columns = ['Month (01-2006 to 09-2008)','Apple','Microsoft']
deltaPlot = stocksDelta.set_index('Month (01-2006 to 09-2008)').sort_index().plot(style='o--',ylim=[-30,160],subplots=True,title="Apple and Microsoft Stock Price (difference from Jan 2006 baseline) - Problem 1c")
#juxataposition doesn't allow for easy comparison of the stock prices.  This wouldn't work well if the intention 
# is to make that type of comparison
plt.savefig('Problem_1c.png')

