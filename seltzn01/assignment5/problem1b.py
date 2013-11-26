#Nathan Seltzer
#Homework 5
#Problem1b.py

#import neccesary modules
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

f = open('stocks.dat', 'r') #opens file with intention of reading, but hasn't read yet
f.readline() #bypass first line
#same as annotions for problem1 
apple = []
microsoft = []
date = []
months = range(1, 34)
for line in f:
	header = line.split(',')
	date.append(str(header[0]))
	apple.append(float(header[1]))
	microsoft.append(float(header[2]))




"""
For some reason, the arrays that I had created by parsing the stock values from the
file were in reverse order. The following code reverses the order so that the
charts accurately reflect the data. 

"""

arr = np.array(apple)
ap = arr[::-1]
# print ap

arr2 = np.array(microsoft)
mic = arr2[::-1]
# print mic


# print "microsoft"
# print mic

# print "apple"
# print ap

sdate = sort(date)

grid(True)
plt.title("Price of Apple (AAPL) and Microsoft (MSFT) Stock\n from January 2006 to September 2008 ")
plt.xlabel("Month and Year")
plt.ylabel("Price of Stock in Dollars")
plt.xticks(range(0,34,6),sdate[0:34:6])

#I removed the default amount of tick marks (every 20) so that the graph
#is less cluttered and more aesthetically pleasing
plt.yticks([0,40,80,120,160,200])
#the following plots both apple and microsoft plots in the same graph
#i am assigning them a name so that I can later identify them in the legdn
apPlot, = plt.plot( months , ap, label="Apple")
msPlot, = plt.plot( months, mic, label="Micosoft")

#for readability, I created a lenged
# I set the location of the legend at the top left, "loc = 2", since it
# is out of the way of the plot lines
legend([apPlot,msPlot],['AAPL','MSFT'], loc = 2)

plt.show()
""" Conclusions: With the superposition, we can see that Apple's stock value
is consistently higher than Microsoft's. However, becuase we are looking at
both stock plots on the same graph, it is not possible to see whether the
relative magnitude of the stocks changes are the same."""