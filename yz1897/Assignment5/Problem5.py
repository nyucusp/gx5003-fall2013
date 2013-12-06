# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:15:11 2013

@author: yilong
"""

from datetime import datetime
import os
import json
from dateutil.parser import parse

# parseing the json data to produce the avaliable count at tiven hours.

dirs=os.listdir('./')

jsfiles=[]
for i in dirs:
    if i.find('citybike')!=-1:
        jsfiles.append(i)


frequent={"total":{}}
for js in jsfiles:
    jline=open(js,'r').readline()
    data=json.loads(jline)
    #print json.dumps(data, sort_keys=True, indent=4)

    hour=parse(data["executionTime"],fuzzy=True).hour
    #print len(data["stationBeanList"])
    stations=data["stationBeanList"]
    #print data["stationBeanList"][1].keys()
    s=0
    for i in stations:
        avil=i["availableDocks"]
        stationname=i["stationName"]
        s+=avil
        if stationname not in frequent:
            frequent[stationname]={}
        frequent[stationname][hour]=avil
        
    frequent["total"][hour]=s
        
    
import json
with open('bike.json', 'w') as outfile:
  json.dump(frequent, outfile)
    

