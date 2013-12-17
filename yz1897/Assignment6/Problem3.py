# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:28:23 2013

@author: yilong
"""

'''
---------------
Get Data
---------------
'''
import matplotlib.pyplot as plt
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
    means=[];std=[]
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
        std.append(result.std())
    return means,std

'''
---------------
Test All Data
---------------
'''
def normaltest():
    popu=np.array(pop1);inci=np.array(inc)
    result=[]
    for i in range(5):
        polypara=polyfit(popu,inci,i+1)
        predict = np.poly1d(polypara)
        rmse=(((predict(popu)-inci)**2).mean())**(0.5)
        result.append(rmse)
        print rmse
    return result

m,s=crosstest(chose,pop1,inc)
alldata=normaltest()
print alldata
plt.errorbar(range(1,6),m,yerr=s, fmt='-o',label="Cross Vali")
plt.plot(range(1,6),alldata,'-<',label="All Data")

plt.xlabel("Complexity")
plt.ylabel("RMSE")
plt.legend(loc=0,fontsize=12)
plt.xlim(0,6)
plt.savefig("Figure5.png",dpi=400)
