#Katherine Elliott
#ke638
#Assignment 6 Problem B

import sys
import csv
import numpy as np
from sklearn import cross_validation

input_file = open('labeled_data.csv','r')

input_list = []
for line in input_file:
    input_list.append(line)
input_file.close()

population = []
for i in range(1,len(input_list)):
    population.append(float(input_list[i].split(',')[1]))

#this is our target variable
incidents = []
for i in range(1, len(input_list)):
    incidents.append(float(input_list[i].split(',')[2]))

pop_array = np.array(population)
incidents_array = np.array(incidents)

cv = cross_validation.KFold(len(incidents), n_folds=10, shuffle = True)# error folds greater than tuples
rmse_values = []
r2_values = []
rmse_std = []

for i in range(1, 6):
    rmse_list = []
    r2_list = []
    
    for j, k in cv:
        poly = np.polyfit(pop_array[j], incidents_array[k], i)
        polyval = np.polyval(poly, pop_array[k])
        
        rmse = (((polyval - incidents_array[k])**2).mean(axis= None))**.5
        rmse_list.append(rmse)
        
        average = sum(incidents_array[k])/len(incidents_array[k])
        avg_list = []
        
        for x in range(0, len(incidents_array[k])):
            avg_list.append(average)
        
        ss = sum((polyval - incidents_array[k])**2)
        total = sum((incidents_array[k] - avg_list)**2)
        r2_list.append(1-ss/total)
        
        rmse_values.append(sum(rmse_list)/len(rmse_list))
        r2_values.append(sum(r2_list)/len(r2_list))
        
print rmse_values
print r2_values
        
        
        
        
        
        
            
            
            
        
        










