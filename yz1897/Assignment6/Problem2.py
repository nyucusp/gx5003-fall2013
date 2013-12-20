# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:01:27 2013

@author: yilong
"""

'''
---------------
Get Data
---------------
'''

import numpy as np
datapath=""
def get_labeled_data():
    zipcode=[];pop=[];inc=[];count=0
    for line in file(datapath+"labeled_data.csv"):
        if count==0:
            count=1
            continue
        spt=line[:-1].split(",")
        zipcode.append(str(int(float(spt[0]))))
        pop.append(float(spt[1]))#to caculate the population delsity, float will be better
        inc.append(float(spt[2]))
    return zipcode,pop,inc

def get_unlabeled_data():
    zipcode=[];pop=[];count=0
    for line in file(datapath+"unlabeled_data.csv"):
        if count==0:
            count=1
            continue
        spt=line[:-1].split(",")
        zipcode.append(str(int(float(spt[0]))))
        pop.append(float(spt[1]))#to caculate the population delsity, float will be better
    return zipcode,pop

zip1,pop1,inc=get_labeled_data()
zip2,pop2=get_unlabeled_data()


'''
---------------
Cross validation
---------------
'''

from numpy import polyfit, polyval,poly1d
import random


l=len(pop1)



def ithfold(ith,rand,po,inc):
    trainx=[];trainy=[];testx=[];testy=[]
    for i in range(len(po)):
        if chose[i]==ith:
            testx.append(po[i]);testy.append(inc[i])
        else:
            trainx.append(po[i]);trainy.append(inc[i])
    return np.array(trainx),np.array(trainy),np.array(testx),np.array(testy)
    
def crosstest(chose,pop1,inc):
    crossresult=[];means=[]
    for i in range(5):
        result=[]
        for fold in range(10):
            trainx,trainy,testx,testy=ithfold(fold,chose,pop1,inc)
            polypara=polyfit(trainx,trainy,i+1)
            predict = np.poly1d(polypara)
            rmse=(((predict(testx)-testy)**2).mean())**(0.5)
            result.append(rmse)
        result=np.array(result)
        means.append(result.mean())
        crossresult.append((result.std(),result.mean()))
    return means

ind=[]
for x in range(100):
    chose=[random.randrange(10) for i in range(l)]
    means=crosstest(chose,pop1,inc)
    ind.append(means.index(min(means)))     
    
x=[random.randrange(10) for i in range(1000)]
dis={}
for i in ind:
    if i not in dis:
        dis[i]=1
        continue
    dis[i]+=1
print "Frequence of best model complexity:"
print dis
