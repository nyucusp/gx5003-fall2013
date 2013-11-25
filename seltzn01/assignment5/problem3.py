#Nathan Seltzer
#Homework 5
#Problem3.py

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

#the following import form pylab will allow me to use the subplot function
from pylab import *
import datetime

f = open('microprocessors.dat', 'r') 
f.readline()
processor = []
year = []
transistors = []
trans_range = range(1,14)
for line in f:
	header = line.split(',')
	processor.append(str(header[0]))
	year.append(int(header[1]))
	transistors.append(int(header[2]))


#I sorted these so that I could set up the dot plots later on
trans_sorted = sort(transistors)
years_sorted=sort(year)
print years_sorted

# I couldn't figure out how to align the y-axis title so that they would be in order, so I had to manually type them in as a list
p = ['4004','8008', '8080','8086','286', '386TM processor','486TM DX processor','Pentium processor','Pentium II processor',' Pentium III processor','Pentium 4 processor','Xeon' ,'Itanium']

#make sure it works
print p

fig = plt.figure()            #create a figure
ax = fig.add_subplot(1,2,1)    # add plot 1

ax = scatter( years_sorted, trans_range) # scatter(x,y)
ax = plt.yticks(trans_range,p)
ax = xlabel("Year of Introduction")
ax = title("Microprocessors and their Year of Introduction")
grid(True) #sets the grid
gca().xaxis.grid(False) #sets the grid to only contain horizontal lines

ax2 = fig.add_subplot(1,2,2) #add plot 2
#i did this to set the x-axis variable, transistors, to be
#in the format of a log base 10 scale, per the instructions of the assignment 
ax2.set_xscale('log')
ax2 = scatter(trans_sorted, trans_range)

"""
I felt that the y-axis labels for the type of microprocessor was unneccesary
#and redundant for the second, right side dot-plot. I felt that the horizontal
#grid lines on both charts were in alignment, and that the viewer of the chart
#would be able to instantly recognize that the y-axis is the same for both charts. 
"""
ax2 = tick_params(axis='y', direction='out')
ax2 = plt.yticks(trans_range,processor[1:14:-100]) #this just throws of the labels from showing up
ax2 = xlabel("Log Number of Transistors")
ax2 = title("Microprocessors and their Number of Transistors")
grid(True) #sets the grid
gca().xaxis.grid(False) #sets the grid to only contain horizontal lines

plt.show()       #displays chart

""" note: I played around with the subplots option in the pylab viewer
#to format the final png that I saved. """