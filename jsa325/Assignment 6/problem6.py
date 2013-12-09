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

for i in range(1,len(linesLData)):
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

"""
Part b: cross-validation, select model complexity based on RMSE and OLS scores for 1–5th order polynomial models

"""

# Initialize target and training sets

def kfolds(numberFolds, listTrain, listTest):
    numberFolds = numberFolds
    sizeCrossValidation = len(listTrain)/numberFolds
    
    arrayTarget = []
    arrayTrain = []
    
    for x in range(numberFolds):
        data = zip(listTest, listTrain)
        boundLower = sizeCrossValidation * x
        boundUpper = sizeCrossValidation * (x + 1)
        
        setTarget = data[boundLower:boundUpper]
        arrayTarget.append(setTarget)
        
        setTrain = data[:boundLower]
        setTrain.extend(data[boundUpper])
        arrayTrain.append(setTrain)
        
    return numberFolds, sizeCrossValidation, arrayValidate, arrayTrain

# Define functions to calculate RMSE and RSQ scores

def calculateRMSE(x, y, xTarget=None, yTarget=None, degree=0, computeRSQ=True)

    if xTarget==None:
        xTarget = x
        yTarget = y

    # Fit to training set

    coefFit = np.polyfit(x, y, degree)    
    
    # Compute residuals on validation set

    residualsRSQ = sum((yTarget - np.polyval(coefFit, xTarget))**2)

    # Compute RMSE and RSQ scores from validation set on training regression

    RMSE = residualsRSQ/len(xTarget)
    RSQ = RMSE**(0.5)

    # Define function to calculate RMSE scores for 1–5th order polynomial models

    if computeRSQ:
        averageTarget = sum(yTarget/len(yTarget))
        for yi in yTarget:
            listSquares = (yi - averageTarget)**2
        sumSquares = sum(listSquares)
        RSQ = 1 - (residualsRSQ/sumSquares)
    else:
        RSQ = 0

    # Compute RMSE and RSQ scores for models

"""
Part c: plot RMSE of whole training set against 10-fold CV average

"""
"""
Part d: build final OLS model

"""