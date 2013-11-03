# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:08:20 2013

@author: yilong
"""

import MySQLdb


#Caculate the population of a zipcode
def Manhattan_Incident_Address():    
    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  

    cur = db.cursor() 
    query1 = "Select iaddress from Incident, Borough where izip=bzip and bname='Manhattan' and iaddress is not NULL"    
    cur.execute(query1)
    for row in cur.fetchall():
        print row[0]
    # close connection
    db.close()
    
Manhattan_Incident_Address()