# Awais Malik
# Assignment 5
# Problem 1a
# Annotations at the end of the code

import pandas as pd

# Import the stocks.dat file
stock = pd.read_csv('stocks.dat')
apple_stock = stock[['month','apple']]
index = apple_stock.set_index('month')
apple_index = index.sort()

# Plotting Apple's Stock
plot = apple_index.plot(legend = True, style = "ko--")
plot.set_title('Monthly Apple Inc. Stock Price Jan 06 - Sep 08')
plot.set_ylabel('Stock Price')
plot.set_xlabel('Month')
plot.annotate('Used Pandas to sort data \nsetting "month" as index.', xy=(17,85))
plot.figure.savefig('Problem1a.jpg',dpi = 300)

""" Annotations:
I used the pandas package for plotting all the 3 plots. (a, b, c)
It is super convenient, for it automatically takes care of a lot of
formatting issues that are otherwise tedious to work out in matplotlib.
I set the month column as the index for the dataframes in all 3 plots. """