# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:08:21 2013

@author: yilong
"""


import MySQLdb

#connect to database

#Caculate the population of a zipcode
def Pop_Addr_With_Incident():    
    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  

    cur = db.cursor() 
    query1="select distinct bzip from Incident, Borough where bzip=izip and bname='Manhattan'"
    query2 = "Select distinct zzip,zpop from Zipcode as Z, ("+query1+") as M \
    where zzip=M.bzip and zzip is not NULL"    
    cur.execute(query2)
    for row in cur.fetchall():
        print row[0],row[1]
        
    # close connection
    db.close()
    
Pop_Addr_With_Incident()