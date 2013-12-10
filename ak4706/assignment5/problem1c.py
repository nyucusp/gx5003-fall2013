import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv('stocks.dat', parse_dates=True, index_col=0)
#print df
close_px = df[['apple', 'microsoft']]
#close_px= df.resample('B', fill_method='ffill')

#print close_px

fig, axs = plt.subplots(2,1, sharex=True)
#fig.subplots_adjust(hspace=.5)
close_px['apple'].plot('Apple', ax=axs[0], style='o-', legend=True)
#plt.title('Apple')
axs[0].set_xlabel('')
#plt.xlabel('Date')
#plt.show()
axs[0].set_title('Apple')
axs[1].set_title('Microsoft')

close_px['microsoft'].plot('Microsoft', ax=axs[1], style='go-', legend=True)
#plt.title('Microsoft')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Stock Price', fontsize=14)

#plt.ylabel('Stock Price')
plt.suptitle('Stock Prices', fontsize = 20)

plt.show()

#When using juxtaposition, you can see that Microsoft and Apple
#had similar patterns of ups and downs, but in the previous plot
#Microsoft almost looked like  a straight line because it wasn't
#as dramatic as Apple's, but actually was very similar
#For this data juxtaposition is a better technique to use because
#you don't lose Microsoft's trend pattern, which was lost in the
#superposition graph.