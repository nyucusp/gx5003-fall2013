import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv('stocks.dat', parse_dates=True, index_col=0)
#print df
close_px = df[['apple', 'microsoft']]

#print close_px
close_px.ix['2006':].plot(style='o-')
#pd.DataFrame.plot(frame= None, x='Date', y = 'Stock Price', Legend = True, title = "Apple Closing Stock Prices")
plt.title('Apple and Microsoft Closing Stock Prices', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Stock Price', fontsize=16)
plt.show()

#From this plot it seems that Apple is doing better than Microsoft,
# and had a lot more ups and downs than Microsoft