import pandas as pd
from _collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

labeledDataFile = open('labeled_data.csv','r')
next(labeledDataFile) #dump header

labeledDataDict = defaultdict(list)
for line in labeledDataFile:
    line = line.rstrip()
    line = line.split(',')
    lineSplitList = []
    for el in line:
        lineSplitList.append( int(float(el)) )
    labeledDataDict[lineSplitList[0]] = [ lineSplitList[1],lineSplitList[2] ]
labeledDataFile.close()

labeledDataDF = pd.DataFrame.from_dict(labeledDataDict, orient='index')
labeledDataDF.columns = ['population','incidents']

train = np.array(labeledDataDF['population'])
target = np.array(labeledDataDF['incidents'])
kf = KFold(len(train), n_folds=10, shuffle=True)

resultRMSEList = [] #hold MSE results from operation
for el1, el2 in kf: # iterate through training and test sets
    RMSEList = []
    for i in range(1,6): # iterate through the 5 polynomial series
        fit_est = np.polyfit(train[el1],target[el1],i) # calculate the polyfit for the poly level [i]
        fit_func = np.poly1d(fit_est) # hold the fit function for that order polynomial
        rmse = sqrt(mean_squared_error(target[el2], fit_func(train[el2])))
        RMSEList.append(rmse) # aggregate results in list
        
    resultRMSEList.append(RMSEList) #append RMSE to master list

RMSE_poly_mean = [] # reconfigure to capture mean for each polynomial
for i in range(0,5):
    RMSE_list = []
    for line in resultRMSEList:
        RMSE_list.append(line[i])
    RMSE_poly_mean.append(np.mean(RMSE_list))
    
RMSEList = []

for i in range(1,6):
    fit_est = np.polyfit(train,target,i) # calculate the polyfit for the poly level [i]
    fit_func = np.poly1d(fit_est) # hold the fit function for that order polynomial
    rmse = sqrt(mean_squared_error(target, fit_func(train)))
    RMSEList.append(rmse) # aggregate results in list
    
xval = []
for i in range(1,6):
    xval.append(i)
RMSE_polyList = zip(xval, RMSEList)
RMSEdf = pd.DataFrame(RMSE_polyList)
RMSEdf.columns = ['polynomial','All data']
RMSEdf['CV RMSE'] = RMSE_poly_mean

plt.xkcd()
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.plot(RMSEdf['polynomial'], RMSEdf['All data'], label='All data')
ax.plot(RMSEdf['polynomial'], RMSEdf['CV RMSE'], label='CV RMSE')
ax.set_xlabel('Polynomial Fit')
ax.set_ylabel('RMSE')
ax.set_xticks(RMSEdf['polynomial'])
ax.legend()
plt.savefig('QuestionC.png')

print "Findings:"
print "The results diverge after the 3rd polynomial"