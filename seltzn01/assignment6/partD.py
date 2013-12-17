# Nathan Seltzer
# Homework 6
# partD.py

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy import stats
import math
import random
from matplotlib.pyplot import *


f = open('labeled_data.csv', 'r') 
f.readline() 

zipcode = []
population = []
num_incidents = []
for line in f:
	header = line.split(',')
	zipcode.append(float(header[0]))
	population.append(float(header[1]))
	num_incidents.append(float(header[2]))

Zip = zipcode
Pop = population
Ni = num_incidents



"""
This first part gets the predicted values for the full set
"""

coefs3 = polyfit(Pop, Ni, 3)
xp = np.linspace(-1,120000,1000)
p3 = poly1d(coefs3)
# print "p3: ", p3
# m3 = plt.plot(xp, p3(xp), 'g')

"""
This second part gets the predicted values for the 10-fold CV model
from the csv I exported from Stata
"""

f = open('predicted.csv', 'r') 
f.readline() 

predicted = []
for line in f:
	header = line.split(',')
	predicted.append(float(header[0]))


print predicted


plt.figure()
grid(True)
plt.scatter(Pop, Ni, c = 'k', marker = '.', alpha = .5)
plt.scatter(Pop, predicted, c = 'r', alpha = .5)
m3 = plt.plot(xp, p3(xp), 'b', alpha = .6)


plt.title("10-Fold CV 3rd Order Predicted Values (red dots) \n vs. Full Dataset Predicted Values (blue line) ")
plt.ylabel("Number of Incidents (311 Calls)")
plt.xlabel("Population of Zipcode")

plt.show()