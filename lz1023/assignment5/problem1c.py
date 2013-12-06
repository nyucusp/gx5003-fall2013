import pandas as pd
import matplotlib.pyplot as plt

stock=pd.read_csv('stocks.dat')
stock_index=stock.set_index('month')
index=stock_index.sort()

chart=index.plot(legend=True, style="o-", subplots=True, title="Apple's and Microsoft's stock price")

chart[0].set_xlabel('')
chart[0].set_ylabel('Price($)')

chart[1].set_xlabel('Month')
chart[1].set_ylabel('Price($)')

plt.show()

# In the subplots, the two companies' stock price have similar fluctuation
# But their fluctuant scale are not same. The superpostion in problem 1b is 
# better for us to understand the comparision of these two stock price.