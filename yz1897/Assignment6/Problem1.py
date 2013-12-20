# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:17:48 2013

@author: yilong
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as opt
import pylab
import math
from scipy.special import zeta
datapath=""


params = {'axes.labelsize': 15,
          'text.fontsize': 15,
          'legend.fontsize': 15,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          
          'text.usetex': True}

pylab.rcParams.update(params)



'''
---------------
Get Data
---------------
'''

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
Map two Data sets relationship
---------------
'''

print "Intersection of zip codes:",set(zip1).intersection(set(zip2))

#Population Distribution
print "Data Size:"
print "   Labeled:",len(zip1)
print "  Unlabeled:",len(zip2)

plt.hist(pop1,label="Labeled Zipcode",alpha=0.5,normed=1)
plt.hist(pop2,label="Unlabeled Zipcode",alpha=0.5,normed=1)
plt.xlabel("Population")
plt.ylabel("Percentage")

plt.legend(fontsize=10)
plt.savefig("Figure1.png",dpi=400)
plt.close()


'''
---------------
Population Vs Incident
---------------
'''

#fig = plt.figure(figsize=(10, 8), dpi=400)
l=len(pop1)
#plt.plot(pop1,inc,'.')
#plt.plot([pop1[i] for i in range(len(pop1)) if inc[i]>10],[i for i in inc if i>10],'o')
#fig = plt.figure(figsize=(5, 4), dpi=400)
logp=[];logi=[]
for i in range(l):
    if pop1[i]>0 and inc[i]>0:
        logp.append(math.log(pop1[i]))
        logi.append(math.log(inc[i]))
p1=[];p2=[];i1=[];i2=[]
for i in range(len(logp)):
    if logi[i]>6:
        p1.append(logp[i]);i1.append(logi[i])
    else:
        p2.append(logp[i]);i2.append(logi[i])
plt.plot(p1,i1,"o",label="Class 1",alpha=0.5)
plt.plot(p2,i2,"<",label="Class 2",alpha=0.5)
plt.xlabel("log(Population)")
plt.ylabel("log(Incidents)")
plt.legend(loc=0,fontsize=13)
plt.savefig("Figure2.png",dpi=400)
plt.close()


'''
---------------
Map two Data sets
---------------
'''
#get the city, state and geolocation information of the zipcodes need to be analyzed from another dataset
def get_zip_infor(zips):
    zipinfor={}
    count=0;foundzip=[]
    for line in file(datapath+'zipcode.csv'):
        if count==0:
            count=1
            continue
        spt=line[:-1].split(",")
        z=str(spt[0][1:-1])
        
        if z in zips:
            foundzip.append(z)
            zipinfor[z]=[spt[1][1:-1],spt[2][1:-1],spt[3][1:-1],spt[4][1:-1]]
    if len(foundzip)==len(zips):
        print "All Zipcodes have find information"
    return zipinfor
        


#fig = plt.figure(figsize=(10, 8), dpi=400)



def map_zips(zipinfor,name,c):
    x=[];y=[]
    for i in zipinfor:
        x.append(zipinfor[i][3]);y.append(zipinfor[i][2])
    plt.plot(x,y,'.',label=name,alpha=0.5,markersize=5,color=c)
    #return x,y
zips=zip1
print "Finding zipcode information in Labeled Dataset..."
zipinfor1=get_zip_infor(zips)
map_zips(zipinfor1,"Labeled",'g')
zips=zip2
print "Finding zipcode information in Unlabeled Dataset..."
zipinfor2=get_zip_infor(zips)
map_zips(zipinfor2,"Unlabeled",'r')

#boroughs=["Brooklyn","New York","Queens","Bronx","Staten Island"]    
#for b in boroughs:
#    plot_zip_position(zipinfor,boroughs)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
#plt.ylim(40.5,40.95)
#plt.xlim(-74.3,-73.7)
plt.savefig("Figure3.png",dpi=400)
#plt.legend(loc=0)
plt.close()

'''
---------------
Map two Classes
---------------
'''

lats={1:[],2:[]};longs={1:[],2:[]}
for i in range(len(zip1)):
    if inc[i]<=0 or math.log(inc[i])<6:
        lats[2].append(zipinfor1[zip1[i]][2])
        longs[2].append(zipinfor1[zip1[i]][3])
    else:
        lats[1].append(zipinfor1[zip1[i]][2])
        longs[1].append(zipinfor1[zip1[i]][3])
        
#fig = plt.figure(figsize=(10, 8), dpi=400)

plt.plot(longs[1],lats[1],'.',label="Class 1",alpha=0.5,markersize=5,color='r')
plt.plot(longs[2],lats[2],'.',label="Class 2",alpha=0.5,markersize=5,color='g')
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.savefig("Figure4.png",dpi=400)
#plt.legend(loc=0)
plt.close()
#utmToLatLng(-5)
