# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:17:54 2013

@author: yilong
"""

def getzippopulation():#get the population in each zip code
    count=0
    zippopu={}
    
    for line in file("c:/works/dropbox/Git/data/zipCodes.csv"):
        if count>0:
            itemlist=line[:-1].split(",")
            if itemlist[10]!='':#population exist
                popu=int(itemlist[10])   
                if itemlist[1] in zippopu:#the zip code already exist
                    if popu>zippopu[itemlist[1]]:
                        zippopu[itemlist[1]]=popu#chose the larger one.
                        '''I assume that the lager population is more 
                        correct when meet duplicating zipcodes, given 
                        that I don't know how the data is processed.'''
                else:# if no duplication 
                    zippopu[itemlist[1]]=popu
        count+=1

    return zippopu
    

def getzipcrime():#get the crime number in each zip
    
    zipcrime={}#the crime number in each zip
    
    for line in file("c:/works/dropbox/Git/data/Incidents_grouped_by_Address_and_Zip.csv"):
        linesplit=line.split(",")
        if len(linesplit)==3:
            zipcd=linesplit[-2]
        if len(zipcd)==5:                      
            if zipcd not in zipcrime:
                zipcrime[zipcd]=0
            zipcrime[zipcd]+=1
    return zipcrime

def getboroughzipcode():#get the zipcode in each borough

    boro_zip_dic={}#the zip codes in each borough

    for line in file("c:/works/dropbox/Git/data/boroughs.csv"):
        linesplit=line[:-1].split(",")

        #put a zip code into a list of which the key is borough
        if linesplit[1] in boro_zip_dic:            
            boro_zip_dic[linesplit[1]].append(linesplit[0])

        else:
            #if not exist
            boro_zip_dic[linesplit[1]]=[linesplit[0]]
    return boro_zip_dic
    
    
if __name__=="__main__":
    zippopu=getzippopulation()
    zipcrime=getzipcrime()
    borozipgroup=getboroughzipcode()  
    #get three dict from the file
    
    '''To get the estimated incident rate in different borough
    based on the three data set, the zipcode area whose population
    is not available should be excluded.'''
    
    #if there is no crime number in this zipcode, the number is 0
    for i in zippopu:
        if i not in zipcrime:
            zipcrime[i]=0
    
    boro_inc_rate={}#the incident rate of each zone
    for bo in borozipgroup:
        inc_number=0
        popu=0
        for zi in borozipgroup[bo]:
            if zi in zippopu:
                inc_number+=zipcrime[zi]
                popu+=zippopu[zi]
                boro_inc_rate[bo]=float(inc_number)/popu
    
    #order the result        
    tobeorder=[]
    for bo in boro_inc_rate:
        tobeorder.append((bo,boro_inc_rate[bo]))
    orderlist=sorted(tobeorder)
    f=open("output_problem2.txt",'w')
    for item in orderlist:
        line=item[0]+' '+str(item[1])+'\n'
        f.write(line)
    f.close()
    
    