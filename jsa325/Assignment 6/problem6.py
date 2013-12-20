# -*- coding: utf-8 -*-
# Import packages

import matplotlib.pyplot as plt
import numpy as np
import math

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

# TO DO: visually analyze plots
# TO DO: additional plots?

"""
Part b: cross-validation, select model complexity based on RMSE and RSQ scores for 1–5th order polynomial models

"""

print'\nPart B:'

# Import packages

from sklearn import cross_validation

# Read data into train and target variables

variableTrain = []
variableTarget = []

for i in range(1,len(linesLData)):
    variableTrain.append(float(linesLData[i].split(',')[1]))
    variableTarget.append(float(linesLData[i].split(',')[2]))

# Initialize RMSE and RSQ models and lists, and define cross-validation function

cv = cross_validation.KFold(len(variableTarget), n_folds=10, shuffle=True)
arrayTrain = np.array(variableTrain)
arrayTarget = np.array(variableTarget)

scoresRMSE = []
scoresRSQ = []
scoresRMSE_std = [] # Initialize list to hold standard deviations of listRMSE for part c

# Initialize lists to hold RMSE and RSQ values for 1–5th order polynomail models

for i in range(1,6):
    listRMSE = []
    listRSQ = []
    
    # Fit polynomail model of order i to training set 
       
    for train, test in cv:
        polyTrain = np.polyfit(arrayTrain[train], arrayTarget[train], i)
        polyTest = np.polyval(polyTrain, arrayTrain[test])
    
        # Compute RMSE for folds and models, save values to listRSME
        
        RMSE = (((polyTest - arrayTarget[test]) ** 2).mean(axis=None)) ** .5
        listRMSE.append(RMSE)
        
        # Compute RSQ for folds and models, save values to listRSQ
        
        listAverage = []
        
        for j in range(0,len(arrayTarget[test])):
            averageTest = sum(arrayTarget[test])/len(arrayTarget[test])
            listAverage.append(averageTest)
        
        residuals = sum((polyTest - arrayTarget[test]) ** 2)
        totals = sum((arrayTarget[test] - listAverage) ** 2)
        
        listRSQ.append(1 - (residuals/totals))
    
    # Average over listRMSE and listRSQ, save to scoresRMSE and scoresRSQ
    
    scoresRMSE.append(sum(listRMSE)/len(listRMSE))
    scoresRSQ.append(sum(listRSQ)/len(listRSQ))

# Print scores

# print scoresRMSE
# print scoresRSQ

print "Polynomial of order", (scoresRMSE.index(min(scoresRMSE)) + 1), "is the model with the lowest RMSE score."
print "Polynomial of order", (scoresRSQ.index(min(scoresRSQ)) + 1), "is the model with the lowest RSQ score."

# Based on the RMSE scores, 3rd order polynomial model gives the best fit
# Based on the RSQ scores, 5th order polynomial model gives the best fit

# TO DO: plot both 3rd and 5th order polynomial models

"""
Part c: plot RMSE of whole training set against 10-fold cross-validation average

"""

# Compute standard deviations, save to scoresRMSE_std

scoresRMSE_std.append(np.std(listRMSE))

# Compute RMSE for each model on all data without 10-fold cross-validation

allRMSE = []

for i in range(1,6):
    polyTrain = np.polyfit(arrayTrain[train], arrayTarget[train], i)
    polyTest = np.polyval(polyTrain, arrayTrain[test])
    RMSE = (((polyTest - arrayTarget[test]) ** 2).mean(axis=None)) ** .5
    allRMSE.append(RMSE)
    
# Plot 10-fold cross-validation average (y-axis) as a function of model complexity (x-axis)

ax = plt.subplot(1,1,1)
order = np.arange(1,6)

plt.bar(order, scoresRMSE, width=0.6, color='dimgray', zorder=1, align='center')
plt.bar(order, allRMSE, width=0.3, color='darkgray', zorder=2, align='edge')

# Format, add labels and guiding lines

ax.set_xlim([0.5,5.5])
ax.set_ylim([9000,19000])
ax.set_xlabel('Model Complexity (Order of Polynomial)')
ax.set_ylabel('RMSE (Number of Incidents)')
ax.set_title('RMSE and Model Complexity')

# plt.show()
plt.savefig('Plot c1 – RMSE v. Model Complexity.png')
plt.clf()

# TO DO: add error bars and legend

"""
Part d: build final RSQ model

"""

print'\nPart D:'

# Read New York City zip code data from previous assignment into new zip code list

inputBData = open('/Users/JSAdams/gx5003-fall2013/jsa325/tutorial2/boroughs.csv', 'r')

linesBData = []
for line in inputBData:
    linesBData.append(line)
inputBData.close()

listBZip = []
for elt in linesBData:
    listBZip.append(elt[0:5])
setBZip = set(listBZip)

# Divide training set into two training incident variables and initialize two target incident variables
# NOTE: I = inside NYC, O = outside NYC

variableTrainI = []
variableTrainO = []
variableTargetI = []
variableTargetO = []

for i in range(1,len(linesLData)):
    if str(int(float(linesLData[i].split(',')[0]))) in setBZip:
        variableTrainI.append(float(linesLData[i].split(',')[1]))
    else:
        variableTrainO.append(float(linesLData[i].split(',')[1]))
        
for i in range(1,len(linesLData)):
    if str(int(float(linesLData[i].split(',')[0]))) in setBZip:
        variableTargetI.append(float(linesLData[i].split(',')[2]))
    else:
        variableTargetO.append(float(linesLData[i].split(',')[2]))

# Repeat model, cross-validation, RMSE, and RSQ steps from part b for I and O

# I: initialize RMSE and RSQ models and lists, and define cross-validation function

cv = cross_validation.KFold(len(variableTargetI), n_folds=10, shuffle=True)
arrayTrainI = np.array(variableTrainI)
arrayTargetI = np.array(variableTargetI)

scoresRMSEI = []
scoresRSQI = []

# Initialize lists to hold RMSE and RSQ values for 1–5th order polynomail models

for i in range(1,6):
    listRMSEI = []
    listRSQI = []
    
    # Fit polynomail model of order i to training set 
       
    for train, test in cv:
        polyTrainI = np.polyfit(arrayTrainI[train], arrayTargetI[train], i)
        polyTestI = np.polyval(polyTrainI, arrayTrainI[test])
    
        # Compute RMSE for folds and models, save values to listRSME
        
        RMSE = (((polyTestI - arrayTargetI[test]) ** 2).mean(axis=None)) ** .5
        listRMSEI.append(RMSE)
        
        # Compute RSQ for folds and models, save values to listRSQ
        
        listAverageI = []
        
        for j in range(0,len(arrayTargetI[test])):
            averageTestI = sum(arrayTargetI[test])/len(arrayTargetI[test])
            listAverageI.append(averageTestI)
        
        residualsI = sum((polyTestI - arrayTargetI[test]) ** 2)
        totalsI = sum((arrayTargetI[test] - listAverageI) ** 2)
        
        listRSQI.append(1 - (residualsI/totalsI))
        
    # Average over listRMSEI and listRSQI, save to scoresRMSEI and scoresRSQI
    
    scoresRMSEI.append(sum(listRMSEI)/len(listRMSEI))
    scoresRSQI.append(sum(listRSQI)/len(listRSQI))
        
# O: initialize RMSE and RSQ models and lists, and define cross-validation function

cv = cross_validation.KFold(len(variableTargetO), n_folds=10, shuffle=True)
arrayTrainO = np.array(variableTrainO)
arrayTargetO = np.array(variableTargetO)

scoresRMSEO = []
scoresRSQO = []

# Initialize lists to hold RMSE and RSQ values for 1–5th order polynomail models

for i in range(1,6):
    listRMSEO = []
    listRSQO = []
    
    # Fit polynomail model of order i to training set 
       
    for train, test in cv:
        polyTrainO = np.polyfit(arrayTrainO[train], arrayTargetO[train], i)
        polyTestO = np.polyval(polyTrainO, arrayTrainO[test])
    
        # Compute RMSE for folds and models, save values to listRSME
        
        RMSE = (((polyTestO - arrayTargetO[test]) ** 2).mean(axis=None)) ** .5
        listRMSEO.append(RMSE)
        
        # Compute RSQ for folds and models, save values to listRSQ
        
        listAverageO = []
        
        for j in range(0,len(arrayTargetO[test])):
            averageTestO = sum(arrayTargetO[test])/len(arrayTargetO[test])
            listAverageO.append(averageTestO)
        
        residualsO = sum((polyTestO - arrayTargetO[test]) ** 2)
        totalsO = sum((arrayTargetO[test] - listAverageO) ** 2)
        
        listRSQO.append(1 - (residualsO/totalsO))
    
    # Average over listRMSEO and listRSQ), save to scoresRMSEO and scoresRSQO
    
    scoresRMSEO.append(sum(listRMSEO)/len(listRMSEO))
    scoresRSQO.append(sum(listRSQO)/len(listRSQO))

# Print scores

# print scoresRMSEI
# print scoresRSQI
# print scoresRMSEO
# print scoresRSQO

print "Polynomial of order", (scoresRMSEI.index(min(scoresRMSEI)) + 1), "is the model with the lowest RMSEI score."
print "Polynomial of order", (scoresRSQI.index(min(scoresRSQI)) + 1), "is the model with the lowest RSQI score."
print "Polynomial of order", (scoresRMSEO.index(min(scoresRMSEO)) + 1), "is the model with the lowest RMSEO score."
print "Polynomial of order", (scoresRSQO.index(min(scoresRSQO)) + 1), "is the model with the lowest RSQO score."


# Based on the RMSEI scores, the 1st order polynomial model gives the best fit
# Based on the RMSEO scores, the 2nd order polynomial model gives the best fit
# Based on both the RSQI and RSQO scores, the 5th order polynomial model gives the best fit

# Train 1st and 2nd order polynomial models on the whole training set

polyTrainI = np.polyfit(arrayTrainI, arrayTargetI, 1)
polyTrainO = np.polyfit(arrayTrainO, arrayTargetO, 2)

# Test models on unlabeled data

# Divide data set into two actual population variables

indexActualI = []
indexActualO = []

for i in range(1,len(linesUData)):
    if str(int(float(linesUData[i].split(',')[0]))) in setBZip:
        indexActualI.append([float(linesUData[i].split(',')[1]),i,0])
    else:
        indexActualO.append([float(linesUData[i].split(',')[1]),i,0])
        
# Remove index from population variable lists

populationActualI = []
populationActualO = []

for elt in indexActualI:
    populationActualI.append(elt[0])
for elt in indexActualO:
    populationActualO.append(elt[0])
    
# Compute predicted values

polyActualI = np.polyval(polyTrainI, populationActualI)
polyActualO = np.polyval(polyTrainO, populationActualO)

# Reassemble linesUData with predicted incidents

for i in range(0,len(indexActualI)):
    indexActualI[i][2] = polyActualI[i]
for i in range(0,len(indexActualO)):
    indexActualO[i][2] = polyActualO[i]
    
# Initialize final output list

listFinal = []

for i in range(1,len(linesUData)):
    for elt in indexActualI:
        if elt[1] == i:
            listFinal.append(elt)
    for elt in indexActualO:
        if elt[1] == i:
            listFinal.append(elt)
            
# Write results to file

outputResults = open('testData.txt', 'w')
for i in range(1,len(linesUData)):
    outputResults.write("%s, %s, %s \n" % (linesUData[i].split(',')[0], listFinal[i-1][0], math.ceil(listFinal[i-1][2])))
outputResults.close()

# Export predictions

filePredictions = open('predictions.csv', 'w')
filePredictions.write('setBZip,populationActualI,indexActualI\n')
for line in zip(setBZip, populationActualI, indexActualI):
    filePredictions.write(str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n')
for line in zip(setBZip, populationActualO, indexActualO):
    filePredictions.write(str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n')


print '\n'