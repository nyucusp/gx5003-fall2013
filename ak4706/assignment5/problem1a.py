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
close_px['apple'].plot('Apple', style = 'o-')
#pd.DataFrame.plot(frame= None, x='Date', y = 'Stock Price', Legend = True, title = "Apple Closing Stock Prices")
plt.title('Apple Closing Stock Prices', fontsize=20)
plt.xlabel('Date', fontsize= 16)
plt.ylabel('Stock Price', fontsize=16)
plt.legend(loc='upper left', fontsize='medium')
plt.show()

# graph = pd.DataFrame((df), index=pd.date_range('01/2006', periods = 32), columns = ['month', 'apple'])
# plt.figure();
# graph.plot(x = 'month', y='apple', style ='o')
# plt.legend(loc='best')
# plt.show()

#print df.iloc[[1:],[1:]]
# data = open('stocks.dat', 'r')
# lines = data.readlines()[1:]
# for line in lines:
# 	p = line.split(',')
# months, apple = np.loadtxt(p, unpack=True, converters = {0: mdates.strpdate2num('%Y-%m')}, usecols=(0, 1))
# data.close()

# print months
# #print (lines[0].split(','))

# x = []
# y = []

# for line in lines:
# 	p = line.split(',')
# 	x.append(p[0])
# 	y.append(p[1])

# #converters = {0: mdates.strpdate2num('%Y-%m')}
# #dates = [dt.datetime.strptime(d, '%Y-%m').date() for d in x]
# #print dates
# #xv = np.array(x)
# #yv = np.array(y)

# plt.plot(x, y)

# plt.show()