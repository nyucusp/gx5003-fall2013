import pandas as pd
import matplotlib.pyplot as plt

stock=pd.read_csv('stocks.dat')
stock_index=stock.set_index('month')
index=stock_index.sort()


chart=index.plot(legend=True, style="o-")
chart.set_title("Apple's and Microsoft's stock price")
chart.set_xlabel('Month')
chart.set_ylabel('Price($)')

plt.axhline(y=27.06,color="g")
plt.axhline(y=75.51)
plt.annotate("$75.51, 2006-01",xy=(1,80),color="b")
plt.annotate("$27.06, 2006-01",xy=(1,30),color="g")


plt.show()

# Using referece lines for each stock to make the baseline condition clear.
# Using annotates with relevant color for each stock.