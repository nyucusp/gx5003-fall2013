import pandas as pd
from _collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

def calcRMSE_r2(train, target):
    RMSEList = []
    R2List = []

    for i in range(1,6):
        fit_est = np.polyfit(train,target,i) # calculate the polyfit for the poly level [i]
        fit_func = np.poly1d(fit_est) # hold the fit function for that order polynomial
        rmse = sqrt(mean_squared_error(target, fit_func(train)))
        ss_res = sum( (target - fit_func(train)) ** 2 ) 
        y_mean = np.mean(target)
        ss_tot = sum( map( lambda x: (x-y_mean) ** 2, target.tolist() ) )
        r2 = 1 - ( ss_res / ss_tot )
        RMSEList.append(rmse) # aggregate results in list
        R2List.append(r2)
    return [RMSEList, R2List]

# a file of zipcodes that fall within the NYC boroughs
boroughsFile = open('nyc_zctas.csv','r')
next(boroughsFile)

boroughsList = []
for line in boroughsFile:
    boroughsList.append(line.rstrip())
boroughsFile.close()
boroughsList = map(lambda x: int(x),boroughsList)

labeledDataFile = open('labeled_data.csv','r')
next(labeledDataFile) #dump header

labeledDataDict = defaultdict(list) #dictionary of zipcodes, population, and incidents in NYC
nonNYCDict = defaultdict(list) #dictionary of zipcodes, population, and incidents that fall outside NYC
for line in labeledDataFile:
    line = line.rstrip()
    line = line.split(',')
    lineSplitList = []
    for el in line:
        lineSplitList.append( int(float(el)) )
    if lineSplitList[0] in boroughsList:
        labeledDataDict[lineSplitList[0]] = [ lineSplitList[1],lineSplitList[2] ]
    else:
        nonNYCDict[lineSplitList[0]] = [ lineSplitList[1],lineSplitList[2] ]
labeledDataFile.close()

labeledDataDF = pd.DataFrame.from_dict(labeledDataDict, orient='index')
labeledDataDF.columns = ['population','incidents']
nonNYCzipDF = pd.DataFrame.from_dict(nonNYCDict, orient='index')
nonNYCzipDF.columns = ['population','incidents']

NYCtrain = np.array(labeledDataDF['population'])
NYCtarget = np.array(labeledDataDF['incidents'])
nonNYCtrain = np.array(nonNYCzipDF['population'])
nonNYCtarget = np.array(nonNYCzipDF['incidents'])

NYCRMSE, NYCr2 = calcRMSE_r2(NYCtrain, NYCtarget)
nonNYCRMSE, nonNYCr2 = calcRMSE_r2(nonNYCtrain, nonNYCtarget)

xval = []
for i in range(1,6):
    xval.append(i)

plt.xkcd()
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(221)
ax1.plot(xval,NYCRMSE)
ax1.set_xticks(xval)
ax1.set_xlabel('RMSE for NYC Zipcodes')
ax2 = fig.add_subplot(222)
ax2.plot(xval,NYCr2)
ax2.set_xticks(xval)
ax2.set_xlabel('R^2 for NYC Zipcodes')
ax3 = fig.add_subplot(223)
ax3.plot(xval,nonNYCRMSE)
ax3.set_xticks(xval)
ax3.set_xlabel('RMSE for non-NYC Zipcodes')
ax4 = fig.add_subplot(224)
ax4.plot(xval,nonNYCr2)
ax4.set_xticks(xval)
ax4.set_xlabel('R^2 for non-NYC Zipcodes')
plt.savefig('QuestionD1.png')

print "The prediction is that for zipcodes in NYC, a 3rd order polynomial will have the best fit while for zipcodes outside NYC, a 4th order polynomial will fit"

