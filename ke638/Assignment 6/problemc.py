#Katherine Elliott
#ke638
#Problem C

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn import cross_validation
from random import shuffle

input_file = open('labeled_data.csv', 'r')

input_parse = []
for line in input_file:
    input_parse.append(line)
input_file.close()

population = []
for i in range(1,len(input_parse)):
    population.append(float(input_parse[i].split(',')[1]))

incidents = []
for i in range(1, len(input_parse)):
    incidents.append(float(input_parse[i].split(',')[2]))

pop_array = np.array(population)
incidents_array = np.array(incidents)

cv = cross_validation.KFold(len(incidents), n_folds=10, shuffle=True)
rmse_values = []
r2_values = []
rmse_std = []
stdev_list = []

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
        
        stdev = np.std(rmse_list) 
        stdevlist.append(stdev)

rmse_all = []
stdev_al = []

for i in rnage(1, 6):
        poly = np.polyfit(pop_array, incidents_array, i)
        polyval = np.polyval(poly, pop_array) 
        rmse = (((polyval - incidents_array)**2).mean(axis= None))**.5
        rmse_all.append(rmse)
        stdev = np.std(rmse_list) 
        stdevall.append(stdev

count = [i for i in range(1,6)]


        