#Aliya Merali
#Urban Informatics
#Assignment 6
#Part A - Plot the data and reason about any phenomena of interest you see

import csv
import matplotlib.pyplot as plt
import numpy as np

data_temp = open('labeled_data.csv','r')
data = csv.DictReader(data_temp,['# zipcode','population','num_incidents'])
zips = []
pop = []
num_inc = []

for item in data:
    zips.append(item['# zipcode'])
    pop.append(item['population'])
    num_inc.append(item['num_incidents'])

del zips[0]
del pop[0]
del num_inc[0]

zips = [int(float(val)) for val in zips]
pop = [int(float(val)) for val in pop]
num_inc = [int(float(val)) for val in num_inc]

plt.scatter(pop, num_inc, color='g')
plt.title('Population vs. Number of 311 Incidents in NYC by Zip Code')
plt.xlim((-1500,125000))
plt.ylim((-2500,max(num_inc)+2500))
plt.xlabel('Population')
plt.ylabel('Number of 311 Incidents')
plt.show()

dummy_list = np.arange(0,len(zips), 1)
plt.bar(dummy_list, num_inc, 1, color='r')
plt.title('Zip Code vs. Number of 311 Incidents Reported in New York City')
zip_ticks = zips[::10]  
plt.xticks(np.arange(1,len(zips),10),zip_ticks, rotation=40)
plt.xlabel('NYC Zip Code')
plt.ylabel('Number of 311 Incidents')
plt.show()

#_____Observed Phenomena
"""
From the graph of population vs. number of incidents, you can clearly see that 
a general trend exists between increasing population and increasing number of 
311 incidents. So, in a predictive model, the more people in a region, the 
more complaints are received. 

The bar chart of number of incidents in each zip code demonstrates that certain
zip codes have higher reports, and so in a predictive model, they are likely to
again have a relatively higher number of incidents. 

"""
