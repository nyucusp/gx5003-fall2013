#Nathan Seltzer
#Homework 5
#Problem1c.py

#import the neccessary modules and rename them
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

#the following import form pylab will allow me to use the subplot function
from pylab import *

#same as previous annotations
f = open('stocks.dat', 'r') #opens file with intention of reading, but hasn't read yet
f.readline()
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






plt.title("Price of AAPL and MSFT Stock from January 2006 to September 2008 ")
plt.xlabel("Month and Year")
plt.ylabel("Price of Stock")

sdate = sort(date)
#In order to juxtapose both, i'm  going to use the subplot command from pyplot
#I think it makes most sense to juxtopose vertically rather than horizontally
#(2,1,1) refers to the number of rows, number of columns, and number of this first plot
subplot(2,1,1)
plt.plot( months , ap)
plt.title("Apple (AAPL)", weight = 'bold', )
plt.ylabel("Price of Stock in Dollars")
plt.xticks(range(0,34,6),sdate[0:34:6])

grid(True, c = 'g')
#(2,1,1) refers to the number of rows, number of columns, and number of this second plot
subplot(2,1,1)
subplot(2,1,2)
plt.plot( months, mic)
plt.title("Microsoft (MSFT)", weight = 'bold')
plt.xlabel("Month and Year")
plt.ylabel("Price of Stock in Dollars")
plt.xticks(range(0,34,6),sdate[0:34:6])
grid(True, c = 'g')
plt.show()

"""
Superposition vs. Juxtoposition?

There really isn't one clear-cut answer. If one wants to look at larger
market trends, it makes sense to juxtapose both of the stock plots. Having
both on the same scale gives one a better understanding of the magnitude of
changes for both, and we can also see how both stocks reacted to temporal 
events. However, if the goal is to look at both stocks value on the same
scale, the superpositioning is a better idea because one can see the 
true difference in value.

"""


#still need to create labels