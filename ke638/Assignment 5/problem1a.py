#Katherine Elliott
#ke638
#Problem1a Assignment 5

import matplotlib.pyplot as plt
import pandas as pd
import pylab

stocks = pd.read_csv('stocks.dat', index_col = 'month')
stocks_data = stocks.sort_index()#still need to account for the bad row in the data
ax = stocks_data.plot(y='apple', style = 'o--', label='Apple')

#set labels
ax.set_title('Apple Stock Price Fluctuations')
ax.set_xlabel('Month')
ax.set_ylabel('Price in Dollars')

#adjust spine
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

ax.legend(loc='best')

plt.savefig('problem1a.png', dpi=300)
plt.show()