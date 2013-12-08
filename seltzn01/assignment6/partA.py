# Nathan Seltzer
# Homework 6
# assignment6a.py

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from pylab import *
from scipy.stats import gaussian_kde

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

print zipcode[0]
print population[0]
print num_incidents[0]

print zipcode[-1]
print population[-1]
print num_incidents[-1]


num_obs = len(zipcode)
# print num_obs



s = sort(num_incidents)
sre = np.array(s)
srev = sre[::-1]





# #1
a = plt.figure()
plt.hist(s, bins=17, color='darkblue', alpha =0.8)
plt.title("Distribution of Number of 311 Incident Calls (A)")
plt.ylabel("Number of zipcodes (out of 300 total)")
plt.xlabel("Number of Incidents")
grid(True)

# #2
b = plt.figure()
plt.plot(s, linewidth=4, color='darkblue', alpha =0.8)
# plt.fill(srev, alpha=0.4)
xticks(range(0,300,20))
plt.title("Distribution of Number of 311 Incident Calls (B)")
plt.ylabel("Number of Incidents")
plt.xlabel("Number of Observations")
grid(True)

# #3
c = plt.figure()
plt.scatter( population, num_incidents, c = 'k', marker = '.' )
plt.title("Scatter Plot of Zipcodes by \n Population Size and Number of Incidents")
plt.ylabel("Number of Incidents")
plt.xlabel("Population Size")
grid(True)


# I considered creating a Kernal Density plot instead of what I did for 
# chart #2

# density = gaussian_kde(num_incidents)
# xs = np.linspace(0,400000,200)
# # density.covariance_factor = lambda : .25
# # density._compute_covariance()
# plt.plot(xs,density(xs))
# # plt.plot(density(s, bw=0.5))






#making sure that it displays
plt.show()

