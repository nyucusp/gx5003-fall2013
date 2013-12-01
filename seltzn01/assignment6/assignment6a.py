# Nathan Seltzer
# Homework 6
# assignment6a.py

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from pylab import *
from scipy.stats import gaussian_kde

f = open('labeled_data.csv', 'r') #opens file with intention of reading, but hasn't read yet
f.readline() #bypass header line
#i create indexes for each gene, and then place them into lists using a for loop
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

"""
There are two obvious plots that need to be created given the variables.

(1) I want to get a sense of the spread of the dependent/target
variable "num_incidents", which is the number of incidents of 311 calls.
To do this, I plotted a histogram using num_incidents. I used 17 bins,
somewhat arbitrarily. It created cut points at intervals of every 7,010
number of incidents. This can be seen in "chart1.png". It's clear that 
the distribution is positively skewed, with by far a large majority of
observations from the data inside the first bin. 

The histogram I created is informative, but I  don't think it accurately 
represents the data. I could increase the bin size, but I feel like the 
histogram would not be effective, since there would be missing bins as the 
values of num_incidents increased. What I did do instead was plot a sorted 
num_incidents on the y-axis by the number of observations, "num_obs" on the 
x-axis (chart2.png). Here, we can see that about 175 of the zipcodes have 
num_incidents value of less than 100, a flat line. (The first 160 of those
have a 311 incident rate of less than 20.) The remaining 125 zipcodes begin 
to increase in a curvilinear manner. One can see that only 40 zipcodes in 
the dataset, or roughly 12% of all the zipcodes, have number of incidents 
over 40,000.

(2) The second way to visually interpret the given data is by creating a
scatterplot with population on the y-axis and num_incidents on the x-axis 
to see if thereis any correlation between population and number of incidents. 
Doing so results in "chart3.png". There are two interesting "phenomena of
interest" within this scatterplot. (A) First, there are a large number of
observations (i.e. zipcodes) that have a very small incident reports -- 
essentially zero, or at most 10 -- but have populations that span up to 70,000.
I double-checked this scatterplot by creating it in Stata for accuracy.
There could be some legitimate explanations for this, but it seems highly
probable that this could be due to reporting error. Going forward, I'll have
to drop these observations from the data set in order to adhere to OLS
assumptions. (B) Second, their is evidence of heteroskedascticity. The spread
of the data is narrow at the lower values, but then  widens as the values 
increase. One can see this by the cone shape. While the OLS estimates
are not BLUE if the data is heteroskedastic (BLUE assumes homoskedasticity)
it does not bias the estimation of regression parameters. Though, it *does* 
inflate the standard errors of the parameters which affects significance. 
There's not much I can do about this using only Python, nor is it essential
since the assignment does not ask about testing the coefficients for
significance.


"""
s = sort(num_incidents)
sre = np.array(s)
srev = sre[::-1]

grid(True)

# #2
# plt.plot(s, linewidth=4, color='darkblue', alpha =0.8)
# # plt.fill(srev, alpha=0.4)
# xticks(range(0,300,20))

# #1
# plt.hist(s, bins=17)

# density = gaussian_kde(num_incidents)
# xs = np.linspace(0,400000,200)
# # density.covariance_factor = lambda : .25
# # density._compute_covariance()
# plt.plot(xs,density(xs))
# # plt.plot(density(s, bw=0.5))


#3
plt.scatter( population, num_incidents )

#making sue that it displays
plt.show()

