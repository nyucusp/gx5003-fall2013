#Nathan Seltzer
#Homework 5

#the first step is to import the neccesary python modules, including
#matplotlib, numpy, and pylab
import matplotlib.pyplot as plt
import numpy as np
from pylab import *


#I start by opening the stocks.dat file
f = open('stocks.dat', 'r') #opens file with intention of reading, but hasn't read yet
f.readline() # i do this to bypass the header

#create index lists to hold the column data that I will swipe
apple = []
microsoft = []
date = []
#in order to create an ordered graph, I create a list with a range of the
#amount of months in the data
months = range(1, 34)
#now, I glean the stock data from the stocks.dat file by using a for
#loop, splitting the lines by the commas, and appending the column
#vectors to the previously created list indexes.
for line in f:
	header = line.split(',')
	date.append(str(header[0])) # i turn the "date" column into a string
	apple.append(float(header[1]))
	microsoft.append(float(header[2]))

#i print the following titles and values just to make sure that
#the previous for loop and line.split worked 
# print "apple"
# print apple
# print "microsoft"
# print microsoft
#it works

# #reverse reverse
# ap = []
# mic = []
# for stock in reversed(apple):
	
"""
For some reason, the arrays that I had created by parsing the stock values from the
file were in reverse order. The following code reverses the order so that the
charts accurately reflect the data. 

"""
arr = np.array(apple)
ap = arr[::-1]
# print ap


#saving here for the next part
# arr2 = np.array(microsoft)
# mic = arr[::-1]
# print mic

#the date was backward too.
sdate = sort(date)

#I added this grid because it is helpful for orienting the data points,
#but is also light grey and dashed, and therefore does not distract from
#the actual plot
grid(True)

#added title to the graph
plt.title("Price of Apple (AAPL) Stock from January 2006 to September 2008 ")
# creaetd labels for he x and y axes
plt.ylabel("Price of Stock in Dollars")
plt.xlabel("Year and Month")

#simply formatting what dates will be included as tick marks on the x-axis
plt.xticks(range(1,34,6),sdate[1:34:6])

#plotting it
plt.plot( months, ap )

#making sue that it displays
plt.show()