# -*- coding: utf-8 -*-
# Import packages

import matplotlib.pyplot as plt
import numpy as np
import pylab

# Set formatting parameters for plots

params = {'axes.labelsize': 11,
          'text.fontsize': 13,
          'legend.fontsize': 13,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'text.usetex': True}
          
# Read datasets into zip, population, and incidents lists

inputLData = open('/Users/JSAdams/Downloads/ML1Dataset/labeled_data.csv', 'r')
inputUData = open('/Users/JSAdams/Downloads/ML1Dataset/unlabeled_data.csv', 'r')

linesLData = []
for line in inputLData:
    linesLData.append(line)
inputLData.close()

listLZip = []
listLPopulation = []
listLIncidents = []

for i in range(0,len(linesLData)):
    listLZip.append(float(linesLData[i].split(',')[0]))
    listLPopulation.append(float(linesLData[i].split(',')[1]))
    listLIncidents.append(float(linesLData[i].split(',')[2]))
    
linesUData = []
for line in inputUData:
    linesUData.append(line)
inputUData.close()
    
listUZip = []
listUPopulation = []

for i in range(1,len(linesUData)):
    listUZip.append(float(linesUData[i].split(',')[0]))
    listUPopulation.append(float(linesUData[i].split(',')[1]))

"""
Part a: plot labeled data

"""

# Format, add guiding lines

ax = plt.subplot(1,1,1)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.set_axisbelow(True)
ax.grid(which='both', color='0.65', linestyle=':', zorder=0)

# Plot a1: plot incidents v. population

plt.plot(listLPopulation, listLIncidents, '.', color='orange')

# Format, add labels and guiding lines

ax.set_xlim([-9000,130000])
ax.set_ylim([-4000,130000])
ax.set_xlabel('Population')
ax.set_ylabel('Number of Incidents')
ax.set_title('Population v. Number of Incidents')

# plt.show()
plt.savefig('Plot a1 — Population v. Incidents.png')
plt.clf()

# Plot a2: histogram of incidents

ax = plt.subplot(1,1,1)
plt.hist(listLIncidents, 40, color='tomato')

# Format, add labels and guiding lines

ax.set_xlim([-1000,120000])
ax.set_ylim([0,200])
ax.set_xlabel('Number of Incidents')
ax.set_ylabel('Number of Zip Codes')
ax.set_title('Distribution of Incidents')

# plt.show()
plt.savefig('Plot a2 — Distribution of Incidents.png')
plt.clf()

# Plot a3: histogram of population

ax = plt.subplot(1,1,1)
plt.hist(listLPopulation, 40, color='green')

# Format, add labels and guiding lines

ax.set_xlim([-1000,120000])
ax.set_ylim([0,25])
ax.set_xlabel('Population')
ax.set_ylabel('Number of Zip Codes')
ax.set_title('Distribution of Population')

# plt.show()
plt.savefig('Plot a3 — Distribution of Population.png')
plt.clf()

# TO DO: visually analyze plots
# TO DO: additional plots

"""
Part b: cross-validation, select model complexity based on RMSE and RSQ scores for 1–5th order polynomial models

"""

# Import packages

from sklearn import cross_validation, linear_model, datasets
from random import shuffle

# Read data into train and target variables

variableTrain = []
variableTarget = []

for i in range(1,len(linesLData)):
    variableTrain.append(float(linesLData[i].split(',')[1]))
    variableTarget.append(float(linesLData[i].split(',')[2]))

# Initialize RMSE and RSQ models and lists, and define cross-validation function

cv = cross_validaion.KFold(len(variableTarget), n_folds=10, shuffle=True)
arrayTrain = np.array(variableTrain)
arrayTarget = np.array(variableTarget)

scoresRMSE = []
scoresRSQ = []

# Initialize lists to hold RMSE and RSQ values for 1–5th order polynomail models

for i in range(1,6):
    listRMSE = []
    listRSQ = []
    
    # Fit polynomail of order i to training set 
       
    for train, test in cv:
        polyTrain = np.polyfit(arrayTrain[train], arrayTarget[train], i)
        polyTest = np.polyval(polyTrain, arrayTrain[test])
    
        # Compute RMSE for folds and models, save values to listRSME
        
        RMSE = (((polyTest - arrayTarget[test]) ** 2).mean(axis=None)) ** .5
        listRMSE.append(RMSE)
        
        # Compute RSQ for folds and models, save values to listRSQ
        
        listAverage = []
        
        for j in range(0, len(arrayTarget[test])):
            averageTest = sum(arrayTarget[test])/len(arrayTarget[test])
            listAverage.append(averageTest)
        
        residuals = sum((polyTest - arrayTarget[test]) ** 2)
        totals = sum((arrayTarget[test] - listAverage) ** 2)
        
        listRSQ.append(1 - (residuals/totals))

"""
Part c: plot RMSE of whole training set against 10-fold cross-validation average

"""
"""
Part d: build final RSQ model

"""