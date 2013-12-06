import pandas as pd
import matplotlib.pyplot as plt


stock=pd.read_csv('stocks.dat')
apple=stock[['month','apple']]
apple_index=apple.set_index('month')
index=apple_index.sort()

plot=index.plot(legend=True, style="oy-")
plot.set_title("Apple's stock price")
plot.set_xlabel('Month')
plot.set_ylabel('Price($)')
plt.show()

# Using pandas to draw the plot.