# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:07:28 2013

@author: yilong
"""

import MySQLdb
import csv
import os 
#connect to database

#this function creates the table: Borough
def Make_Borough_Table():    

    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  
  
    #create table  
    cur = db.cursor() 
    cur.execute("drop table if exists Borough")
    createCommand = "create table Borough (bzip varchar(255), bname varchar(255), primary key(bzip))"
    cur.execute(createCommand)

    #put data into table
    filename = 'boroughs.csv'
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            # create command to insesrt information from boroughs this into the table, use ignore to avoid duplicate lines from source
            insertCommand = "insert IGNORE into Borough values('" + row[0] + "','" + row[1] + "');"        
            cur.execute(insertCommand)
    db.commit() 
        
    '''Test table
    query = "select * from Borough where bname = 'Queens'"
    cur.execute(query)
    for row in cur.fetchall():
        # I already know 0th and 2nd columns are integers, so i am converting them to string
        print row[0],row[1]''' 
     # close connection
    db.close()



#this function creates the table: Zipcode
def Make_Zip_Table():    
    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  
    cur = db.cursor() 
    #create table
    cur.execute("drop table if exists Zipcode")
    createCommand = "create table Zipcode (zzip varchar(255), zarea float, zpop int, primary key(zzip))"
    cur.execute(createCommand)

    #read and orgainze data from file
    filename = 'zipCodes.csv'
    firstline=1
    zipdic={}
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if firstline==1:
                firstline=0
                continue
            zipc=row[1];area=float(row[7])
            
            #population empty
            try:
                pop=int(row[10])
            except:
                ''' 
                There are two possible cause for the condition:
                    1. there is no people leaving here
                    2. data mistake
                Either way, we should not use the data for analysis.
                '''
                continue
            
            #some 5-digit zipcode area have more than one record, I cumulate its area and population             
            if zipc in zipdic:
                try:
                    zipdic[zipc][0]+=area
                    zipdic[zipc][1]+=pop
                except:
                    continue
            else:
                zipdic[zipc]=[area,pop]
    #make sure area is not zero, otherwise the data is mistaken 
    for i in zipdic:
        if zipdic[i][0]==0:
            del zipdic[i]
                
    #insert into table            
    for z in zipdic:
        insertCommand = "insert into Zipcode values('" + z + "'," + str(zipdic[z][0]) + "," + str(zipdic[z][1]) +");"        
        cur.execute(insertCommand)
    db.commit() 
     
    ''' Test table
    query = "select * from Zipcode where zpop > 100000"
    cur.execute(query)
    for row in cur.fetchall():
        print row[0],row[1],row[2]'''
    # close connection
    db.close()


#this function creates the table: Zipcode
def Make_Inc_Table():    
    #connect to database
    db = MySQLdb.connect(host="localhost",user="yz1897",passwd="123456",db="coursedb")  
    cur = db.cursor() 
    #create table
    cur.execute("drop table if exists Incident")
    createCommand = "create table Incident (izip varchar(255), iaddress varchar(255))"
    cur.execute(createCommand)

    #read and orgainze data from file and insert into table
    filename = 'Incidents_grouped_by_Address_and_Zip.csv'
    firstline=1
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if firstline==1:
                firstline=0
                continue
            zipc=row[1];address=row[0]
            #Empty columns
            if zipc=='':
                zipc='NULL'
            if address=='':
                address='NULL'
            
            insertCommand = "insert into Incident values(\"" + zipc + "\",\"" + address +"\");"    
            cur.execute(insertCommand)
    db.commit()
    
    '''
    #Test table
    query = "select * from Incident where izip='11229'"
    cur.execute(query)
    for row in cur.fetchall():
        print row[0],row[1]
    '''
    # close connection
    db.close()

Make_Borough_Table()
Make_Zip_Table()
Make_Inc_Table()
