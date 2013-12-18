import pandas as pd
from _collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt


def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def R2(x, y, yhat):
    ybar = np.sum(y)/len(y) 
    ssreg = np.sum((yhat-ybar)**2)  
    sstot = np.sum((y - ybar)**2) 
    r2 = ssreg / sstot
    return r2

myDict = {}
with open('labeled_data.csv','r') as f:
    f.next()
    for row in f:
        a = row.strip('\n').split(',')
        myDict[float(a[0])] = [ float(a[1]),float(a[2]) ]

labeled = pd.DataFrame.from_dict(myDict, orient='index')
labeled.columns = ['population','incidents']

train = np.array(labeled['population'])
target = np.array(labeled['incidents'])
kf = KFold(len(train), n_folds=10, indices=True)

RMSEList = []
R2List = []

for i in range(1,6):
    RMSEsum = 0 
    R2sum = 0 
    for a, b in kf: 
        p = np.poly1d(np.polyfit(train[a],target[a], deg=i))
        x=p(train[b])
        rmse=RMSE(x,target[b])
        r2 = R2(train[a],target[a],p(train[a]))
        RMSEsum = RMSEsum+rmse 
        R2sum = R2sum+r2 
    RMSEList.append(RMSEsum/10) 
    R2List.append(R2sum/10) 

for i in range(5):
    print "The 10-fold CV " + str(i + 1) + "-degree polynomial RMSE = " + str(RMSEList[i]) + " R^2 = " + str(R2List[i])
print "The 3rd polynomial has the best fit"

print 'done'
