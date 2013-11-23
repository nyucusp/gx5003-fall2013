#Aliya Merali
#Urban Informatics
#Assignment 5
#Problem 1a 


#import matplotlib.pyplot as plt; plt.rcdefaults()
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dts
#import matplotlib.ticker as ticker
from datetime import date

data = open('stocks.dat','r')

month = []
apple = []
for line in data:
    split_data = line.split(',')
    month.append(split_data[0])
    apple.append(split_data[1])
del month[0]
del apple[0]
dates = []
for element in month:
    yr = int(element.split('-')[0])
    mn = int(element.split('-')[1])
    new_date = date(int(yr),int(mn),1)
    dates.append(new_date)

fig, ax = plt.subplots()
ax.plot(dates, apple, 'o-')
fig.autofmt_xdate()
#Added the appropriate labels below for easy interpretation
plt.xlabel('Date')
plt.title("Apple's Stock Quotes at the Start of Each Month, Jan 2006 - Sept 2008")
plt.ylabel("Stock Quote")
plt.ylim((0, 220))#Adjusted the y limit so plot had top buffer
plt.grid(which = 'both', color = '0.75', linestyle = '-')#Added light gridlines to make reading easier


plt.show()

#____________________Explanation of Plotting Principles
# With this plot, I decided to use a connected symbol plot because it best represents the data. I followed the principles described in class including clear communication of data and making the data stand out by keeping it neat. I tried to use visual prominence by adding the light grid lines and accurate labels. I also added a buffer to the top of the plot so it would not touch the edge of the plotting rectangle. 
