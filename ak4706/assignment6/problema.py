import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd
import csv
from pandas.tools.plotting import scatter_matrix
from pylab import *
from numpy import arange, array, ones, linalg


#import the data
data = open('labeled_data.csv', 'r')

#read through the data and put all the lines into a list
lines = []
for line in data:
	lines.append(line)

#population - read it into a list
pop =[]
for i in range(1,len(lines)):
	pop.append(float(lines[i].split(',')[1]))
#print pop

#incidents - read it into a list
inc=[]
for i in range(1,len(lines)):
	inc.append(float(lines[i].split(',')[2]))

#problema1.png - all labeled data plotted in a scatter plot, and added
#the line of best fit
#plt.scatter(pop,inc)
plt.xlim([0,120000])
plt.ylim([-1000,140000])
plt.xlabel('Population')
plt.ylabel('Number of Incidents')
plt.title('Number of Incidents based on Population size for 311 data')
z3 = polyfit(pop,inc,1)
p3=poly1d(z3)
plt.scatter(pop,inc, label='Zip Code')
plt.plot(pop,p3(pop), color='green', label='First Degree Polynomial')
#plot(pop,inc,'yo', pop,p3(pop), 'g-', label="First Degree Polynomial")
plt.legend(loc='best')
plt.show()

#problema2.png - because there are so many zipcodes that have so few inceidents
# it is pulling the line of best fit down as seem in problema1.png so I plotted
#only those that have more than 100 incidents here, and the line fits much
#better
dictpopinc={}
for i in range(0,len(pop)):
	dictpopinc[pop[i]]=inc[i]

pop2=[]
inc2=[]
for key in dictpopinc:
	if dictpopinc[key] > 100:
		pop2.append(key)
		inc2.append(dictpopinc[key])

#plt.scatter(pop2,inc2)
z3 = polyfit(pop2,inc2,1)
p3=poly1d(z3)
#xx=linspace(0,1,100)
plt.scatter(pop2,inc2, label='Zip Code')
plt.plot(pop2,p3(pop2), color='green', label='First Degree Polynomial')
#plot(pop2,inc2,'yo', pop2,p3(pop2), 'g-', label="First Degree Polynomial")
plt.xlim([0,120000])
plt.ylim([-1000,140000])
plt.title('311 data by population where number of incidents>100')
plt.xlabel = 'Population'
plt.ylabel = 'Number of Incidents'
plt.legend(loc='best')
plt.show()
