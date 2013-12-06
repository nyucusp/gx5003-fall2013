# Awais Malik
# Assignment 5
# Problem 1c
# Annotations at the end of the code

import pandas as pd

# Import the stocks.dat file
stock = pd.read_csv('stocks.dat')
stocks = stock[['month','apple','microsoft']]
index = stocks.set_index('month')
stock_index = index.sort()

# Plotting Stocks
fig = stock_index.plot(legend = True, subplots = True, sharex = True,\
style = 'ko--', title = 'Monthly Stock Price Apple vs. Microsoft Jan 06 - Sep 08')
fig[1].set_ylabel('Stock Price')
fig[0].set_ylabel('Stock Price')

for label in fig[1].xaxis.get_ticklabels():
    label.set_ha('center')

""" Annotations:
Subplotting in pandas is incredibly easy (as the code shows).
From this plot, we see a very interesting similarity in the trends
of both apple's and microsoft's stock values. They share an almost
identical trendline even if the actual values of apple's stocks are
still much higher than those of microsoft. """