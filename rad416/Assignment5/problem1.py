import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('stocks.dat')
stocks['appleDelta'] = stocks['apple'].map(lambda x: x-75.51) # apply map to subtract stock price on Jan 2006
stocks['microsoftDelta'] = stocks['microsoft'].map(lambda x: x-27.06)

# generate plot for problem 1a
stocksApple = stocks[['month','apple']]
stocksApple.columns = ['Month', 'Apple']
appleplot = stocksApple.set_index('Month').sort_index().plot(style='o--',ylim=[40,220],title="Apple Stock Price - Problem 1a",legend=False)
plt.savefig('Problem_1a.png')

# generate plot for problem 1b
stocksDelta = stocks[['month','appleDelta', 'microsoftDelta']]
stocksDelta.columns = ['Month','Apple','Microsoft']
deltaPlot = stocksDelta.set_index('Month').sort_index().plot(style='o--',title="Apple and Microsoft Stock Price (diff from Jan 2006 baseline) - Problem 1b")
plt.axhline(y=0.0, color='black')
plt.savefig('Problem_1b.png')

# generate plot for problem 1c
stocksDelta = stocks[['month','appleDelta', 'microsoftDelta']]
stocksDelta.columns = ['Month','Apple','Microsoft']
deltaPlot = stocksDelta.set_index('Month').sort_index().plot(style='o--',ylim=[-30,160],subplots=True,title="Apple and Microsoft Stock Price (difference from Jan 2006 baseline) - Problem 1c")
plt.savefig('Problem_1c.png')
