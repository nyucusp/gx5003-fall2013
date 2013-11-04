# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:08:18 2013

@author: yilong
"""

import MySQLdb
import sys
#connect to database

#Caculate the population of a zipcode
def Count_Zip_Popdensity(z):    
    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  
    cur = db.cursor() 
    #fet data
    query = "select zpop,zarea from Zipcode where zzip = '"+z+"'"
    cur.execute(query)
    row = cur.fetchall()
    #handle don't exist data
    if len(row)==0:
        print 'Zipcode '+z+" dose not exist in our dataset."
    else:#print density, note row area is non-zero
        print row[0][0]/row[0][1]
         # close connection
        
    db.close()
    

zipcode=sys.argv[1]
#zipcode='10000'
Count_Zip_Popdensity(zipcode)


