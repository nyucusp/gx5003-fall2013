#Katherine Elliott
#ke638
#Problem1c Assignment 5

import matplotlib.pyplot as plt
import pandas as pd
import pylab

stocks = pd.read_csv('stocks.dat', index_col = 'month')
stocks_data = stocks.sort_index()#still need to account for the bad row in the data
ax1, ax2 = stocks_data.plot(subplots=True, sharex=False, sharey =False,  style = 'o--')

#set labels
ax1.set_title('Apple Price Fluctuations')
ax1,ax2.set_xlabel('Month')
ax1,ax2.set_ylabel('Price in Dollars')
ax2.set_title('Microsoft Price Fluctuations')

#adjust limits
ax1.set_ylim([0,220])
ax2.set_ylim([0,100])

#adjust spines
ax1,ax2.spines['top'].set_visible(False)
ax1,ax2.xaxis.set_ticks_position('bottom')
ax1,ax2.spines['right'].set_visible(False)
ax1,ax2.yaxis.set_ticks_position('left')

ax1.legend(loc='best')
ax2.legend(loc='best')

plt.subplots_adjust(wspace=.5, hspace=.5)#need to change color
plt.savefig('problem1c.png', dpi=300)
plt.show()

#When comparing the market effects of the two diffenet variables(companies in this case) it makes more sense
#to plot on the same graph through superposition rather than juxtaposition, so that both can be analyzed simultaneously.
#This makes the most sense for this case.
#Juxtaposition makes more sense if you want to individually analyze the effects of the market on each company.