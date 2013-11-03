# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:08:19 2013

@author: yilong
"""

import MySQLdb
import sys
#connect to database

#Caculate the population of a zipcode
def Count_Incident_Per_Person(borough):    
    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  

    cur = db.cursor() 
    query1 = "Select sum(zpop) from Zipcode,Borough where zzip=bzip and bname='"+borough+"'"
    cur.execute(query1)
    row = cur.fetchall()
    population=row[0][0]
    
    query2 = "Select zzip from Zipcode,Borough where zzip=bzip and bname='"+borough+"'"
    cur.execute(query2)
    row = cur.fetchall()
    
    query3="Select count(*) from Incident, ("+query2+") as A where izip=A.zzip"
    cur.execute(query3)
    row = cur.fetchall()
    incident=row[0][0]
    # close connection
    db.close()
    return float(incident)/float(population)
         
    

borough=sys.argv[1]
#borough="Manhattan"
print Count_Incident_Per_Person(borough)