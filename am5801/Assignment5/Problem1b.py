# Awais Malik
# Assignment 5
# Problem 1b
# Annotations at the end of the code

import pandas as pd

# Import the stocks.dat file
stock = pd.read_csv('stocks.dat')
stocks = stock[['month','apple','microsoft']]
index = stocks.set_index('month')
stock_index = index.sort()

# Plotting Stocks
plot = stock_index.plot(legend = True, style = 'o--')
plot.set_title('Monthly Stock Price Apple vs. Microsoft Jan 06 - Sep 08')
plot.set_ylabel('Stock Price')
plot.set_xlabel('Month')
plot.annotate('Apple\'s stock price has risen to a significantly higher value. \nMicrosoft\'s stock price has remained steady.', xy=(6,45))
plot.figure.savefig('Problem1b.jpg',dpi = 300)

""" Annotations:
The only difference between this plot and 1a is that I included microsoft
stock prices as a seperate column in the stock_index dataframe.
Once again, plotting the graph in pandas was very convenient.
From this plot, we can infer that apple's stock prices have 
risen to a significantly higher value than those of microsoft. """