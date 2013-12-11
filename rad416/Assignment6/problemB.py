"""
A script to take in the labeled data and test fit for polynomials from 1 to 5, reporting the results.
"""

import pandas as pd
from _collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

#open provided file
labeledDataFile = open('labeled_data.csv','r')
next(labeledDataFile) #dump header

#iterate through
labeledDataDict = defaultdict(list)
for line in labeledDataFile:
    line = line.rstrip()
    line = line.split(',')
    lineSplitList = []
    for el in line:
        lineSplitList.append( int(float(el)) )
    labeledDataDict[lineSplitList[0]] = [ lineSplitList[1],lineSplitList[2] ]
labeledDataFile.close()

#cast dict to dataframe
labeledDataDF = pd.DataFrame.from_dict(labeledDataDict, orient='index')
labeledDataDF.columns = ['population','incidents']

#generate training data for model creation
train = np.array(labeledDataDF['population'])
target = np.array(labeledDataDF['incidents'])
kf = KFold(len(train), n_folds=10, shuffle=True)

#go through iterations of cross-fold validation
resultRMSEList = [] #hold MSE results from operation
resultR2List = []
for el1, el2 in kf: # iterate through training and test sets
    RMSEList = [] #intermediate RMSE values
    R2List = [] #intermediate R2 values
    for i in range(1,6): # iterate through the 5 polynomial sequence
        fit_est = np.polyfit(train[el1],target[el1],i) # calculate the polyfit for the poly level [i]
        fit_func = np.poly1d(fit_est) # hold the fit function for that order polynomial
        # rms = sqrt(mean_squared_error(y_actual, y_predicted))
        rmse = sqrt(mean_squared_error(target[el2], fit_func(train[el2])))
        ss_res = sum( (target[el2] - fit_func(train[el2])) ** 2 ) 
        y_mean = np.mean(target[el2])
        ss_tot = sum( map( lambda x: (x-y_mean) ** 2, target[el2].tolist() ) )
        r2 = 1 - ( ss_res / ss_tot )
        RMSEList.append(rmse) # aggregate RMSE results in intermediate list
        R2List.append(r2) # aggregate R2 results in intermediate list

    resultRMSEList.append(RMSEList) #append RMSE to master list
    resultR2List.append(R2List) #append R2 to master list

RMSE_poly_mean = [] # reconfigure list to capture mean RMSE for each polynomial
R2_poly_mean = [] # reconfigure list to capture mean R^2 for each polynomial
for i in range(0,5):
    RMSE_list = []
    R2_list = []
    for line in resultRMSEList:
        RMSE_list.append(line[i])
    RMSE_poly_mean.append(np.mean(RMSE_list))
    for line in resultR2List:
        R2_list.append(line[i])
    R2_poly_mean.append(np.mean(R2_list))

#output result
for i in range(5):
    print "The 10-fold CV RMSE for polynomial " + str(i + 1) + " is " + str(RMSE_poly_mean[i]) + " and the R^2 is " + str(R2_poly_mean[i])
print "The 3rd polynomial has the best fit"
