# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:17:15 2013

@author: yilong
"""

def getdata():
    
    zipdensity={}#record the population density of each zipcode area
    
    count=0#only for ignore the first line
    
    for line in file("c:/works/dropbox/Git/data/zipCodes.csv"):
        if count<1:#do nothing for first line
            count=1
            continue

        itemlist=line[:-1].split(",")#list of value in a line
        
        if itemlist[10]=='':#population missing, density=0.0
            continue
        else:#population found, computation density
            density=float(itemlist[10])/float(itemlist[7])
            
        if itemlist[1] in zipdensity:#this zipCode already found
            if density>zipdensity[itemlist[1]]:#use the larger density
                zipdensity[itemlist[1]]=density
        else:            
            zipdensity[itemlist[1]]=density

    return zipdensity


if __name__=="__main__":
    tobeorder=[]
    zipdensity=getdata()
    for i in zipdensity:
        tobeorder.append((i,zipdensity[i]))
    orderlist=sorted(tobeorder)
    f=open("output_density_problem2.txt",'w')
    for item in orderlist:
        line=item[0]+' '+str(item[1])+'\n'
        f.write(line)
    f.close()
    
    