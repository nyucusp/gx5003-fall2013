#Special thanks to Ender Faruk Morgul.

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

myDict2 = {}
for values in myDict:
    if(myDict[values][1]>10):
        myDict2[values]= myDict[values]
        

kf = KFold(len(train), n_folds=10, indices=True)

degrees = [1, 2, 3, 4, 5]

ats={}
full={}
RMSEList = []
R2List = []
fts=[]
fak=[]

for i in range(1,6):
    RMSEsum = 0 
    R2sum = 0
    stdlist=[]
    for a, b in kf: 
        p = np.poly1d(np.polyfit(train[a],target[a], deg=i))
        x=p(train[b])
        rmse=RMSE(x,target[b])
        r2 = R2(train[a],target[a],p(train[a]))
        RMSEsum = RMSEsum+rmse 
        R2sum = R2sum+r2
        stdlist.append(RMSE(x,target[b]))
    RMSEList.append(RMSEsum/10) 
    R2List.append(R2sum/10)
    fak.append(np.std(stdlist)/2)
    
    full[i]=[RMSE(p(train),target),R2(train,target,p)]
    fts.append(RMSE(p(train),target))


for i in range(5):
    print "The 10-fold CV " + str(i + 1) + "-degree polynomial RMSE = " + str(RMSEList[i]) + " R^2 = " + str(R2List[i])
print "The 3rd polynomial has the best fit"

print 'done'

#Part_c
    
plt.figure()
plt.errorbar(degrees,RMSEList,yerr=fak,label='10-fold cross validated',color='b',linestyle='-.', linewidth=1.5)
plt.plot(degrees,fts,label='Full model',color='r', linewidth=2.0)
plt.xlim(0,6)
plt.ylim(12000,16000)
plt.xlabel('Fitted Polynomial Degree')
plt.ylabel('RMSE')
plt.title('311 Data: Number of Incidents as a function of population')
plt.ylim(12000,16000)
plt.grid()
plt.legend( loc='upper right' )
plt.show()
plt.savefig('fullmodel.png',dpi = 300)


#Part_d
d=3
p = np.poly1d(np.polyfit(train,target , deg=d))

plt.figure()
plt.plot(train,target,'o',label='Actual Data',color='red')
plt.plot(p(train),target,'s',label='Estimated Data')
plt.ylim(0,130000)
plt.xlim(0,130000)
plt.title('The number of Incidents as a function of population')
plt.legend( loc='upper left' )
plt.show()
plt.savefig('notfiltered.png',dpi = 300)


labeled = pd.DataFrame.from_dict(myDict2, orient='index')
labeled.columns = ['population','incidents']
train = np.array(labeled['population'])
target = np.array(labeled['incidents'])

p = np.poly1d(np.polyfit(train,target , deg=d))
plt.plot(train,target,'o',label='original data')
plt.plot(p(train),target,'s',label='predicted')
plt.ylim(0,130000)
plt.xlim(0,130000)
plt.title('The number of Incidents as a function of population')
plt.legend( loc='upper left' )
plt.show()
plt.savefig('filtered.png',dpi = 300)




