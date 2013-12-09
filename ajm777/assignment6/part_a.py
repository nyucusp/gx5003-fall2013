#Aliya Merali
#Urban Informatics
#Assignment 6
#Part A

import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

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

#__Create dictionary for incidents by zip code to be able to sort
zips_dict = {}
i = 0
while i < len(zips):
    zips_dict[zips[i]]= num_inc[i]
    i= i + 1
zips_dict = OrderedDict(sorted(zips_dict.items()))

#Create new lists to chart
zips = []
inc_by_zip = []
for k, v in zips_dict.items():
    zips.append(k)
    inc_by_zip.append(v)

plt.scatter(pop, num_inc, color='g')
plt.title('Population vs. Number of 311 Incidents in NYC by Zip Code')
plt.xlim((-1500,125000))
plt.ylim((-2500,max(num_inc)+2500))
plt.xlabel('Population')
plt.ylabel('Number of 311 Incidents')
plt.show()

dummy_list = np.arange(0,len(zips), 1)
plt.bar(dummy_list, inc_by_zip, 1, color='r')
plt.title('Zip Code vs. Number of 311 Incidents Reported in New York City')
zip_ticks = zips[::10]
plt.xticks(np.arange(1,len(zips),10),zip_ticks, rotation=40)
plt.xlabel('NYC Zip Code')
plt.ylabel('Number of 311 Incidents')
plt.show()
