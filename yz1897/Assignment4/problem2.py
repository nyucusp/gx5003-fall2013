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
    query = "select zpop,zarea from Zipcode where zzip = '"+z+"'"
    cur.execute(query)
    row = cur.fetchall()
        # I already know 0th and 2nd columns are integers, so i am converting them to string
    print row[0][0]/row[0][1]
         # close connection
    db.close()

zipcode=sys.argv[1]
print Count_Zip_Popdensity(zipcode)


