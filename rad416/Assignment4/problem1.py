"""
A script to take three prepared files, each containing information on NYS zipcodes, 
boroughs, population, and incidents in those zipcodes.  The following script
creates tables for the files, parses the files and uploads them to the database.
The code must be loaded in the same folder as the code in order to successfully run.
"""

import sys
from _collections import defaultdict
import MySQLdb
from subprocess import call
from decimal import *
import warnings
warnings.filterwarnings("ignore")

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:

  # The Cursor object will let you execute the sql commands
  cur = db.cursor()

  #################
  # Create Tables #
  #################

  query = "DROP TABLE IF EXISTS zipcode_population"
  cur.execute(query)

  query = "CREATE TABLE zipcode_population ( zcta INT, total_population INT, area NUMERIC(10,9) )"
  cur.execute(query)

  query = "DROP TABLE IF EXISTS boroughs_raw"
  cur.execute(query)

  query = "CREATE TABLE boroughs_raw ( zipcode INT, borough VARCHAR(40) )"
  cur.execute(query)

  query = "DROP TABLE IF EXISTS incidents"
  cur.execute(query)

  query = "CREATE TABLE incidents ( address VARCHAR(255), zipcode INT, incidents INT )"
  cur.execute(query)

  ##########################
  #   Load Boroughs Data   #
  ##########################

  #parse boroughs file and upload
  boroughZipFile = open('boroughs.csv', 'r')

  boroughZipInsert = []

  baseQuery = "INSERT INTO boroughs_raw (zipcode, borough) VALUES "
  for line in boroughZipFile:
    lineSplit = line.split(",")
    boroughZipInsert.append(baseQuery + "('" + lineSplit[0] + "','" + lineSplit[1].rstrip() + "')")

  boroughZipFile.close()

  for q in boroughZipInsert:
    cur.execute(q) 

  query = "DROP TABLE IF EXISTS boroughs"
  cur.execute(query)

  # deduplicate data
  query = "CREATE TABLE boroughs AS ( SELECT DISTINCT zipcode, borough FROM boroughs_raw)"
  cur.execute(query)

  #drop duplicate table
  query = "DROP TABLE IF EXISTS boroughs_raw"
  cur.execute(query)

  ##########################
  #  Load Incidents Data   #
  ##########################

  #remove the single quote in the address field
  call("tr \"'\" \" \" < Incidents_grouped_by_Address_and_Zip.csv > Incidents_grouped_by_Address_and_Zip_tr.csv", shell=True)

  #upload incidents file (original with commas in col 1)
  zipIncidentFile = open('Incidents_grouped_by_Address_and_Zip_tr.csv','r')
  next(zipIncidentFile) #skip header row
  zipIncidentList = [] #list for formatted file contents
  for line in zipIncidentFile:
    lineSplit = line.split(",")
    if(len(lineSplit) == 3 and len(lineSplit[1]) >= 5 and lineSplit[1][0] == '1'):
      zipIncidentList.append( [ lineSplit[0], lineSplit[1][ :5] , int(lineSplit[2].rstrip()) ] )
  
  zipIncidentFile.close()

  incidentsList = []
  baseQuery = "INSERT IGNORE INTO incidents (address, zipcode, incidents) VALUES "
  for element in zipIncidentList:
    incidentsList.append(baseQuery + "('" + element[0] + "','" + element[1] + "','" +  str(element[2]) + "')")

  for q in incidentsList:
    cur.execute(q) 

  ##########################
  #  Load Population Data  #
  ##########################

  zipPopFile = open('zipCodes.csv','r')
  next(zipPopFile) #skip header row

  zipPopDict = defaultdict(int) #dict for file contents

  #populate zipList
  for line in zipPopFile: 
    lineSplit = line.split(",")
    if(lineSplit[10] != '\n'): #skip if population is empty
      zipPopDict[lineSplit[1]] += int(lineSplit[10].rstrip())

  zipPopFile.close() #close file

  populationList = []
  baseQuery = "INSERT IGNORE INTO zipcode_population (zcta, total_population) VALUES "

  for k,v in zipPopDict.items():
    populationList.append(baseQuery + "('" + k + "','" + str(v) + "')")

  for q in populationList:
    cur.execute(q) 

  ##########################
  #     Load Area Data     #
  ##########################

  zipPopFile = open('zipCodes.csv','r')
  next(zipPopFile) #skip header row

  zipPopDict = defaultdict(Decimal) #dict for file contents

  for line in zipPopFile:
    lineSplit = line.split(",")
    if(lineSplit[10] != '\n'): #skip if population is empty
      zipPopDict[lineSplit[1]] += Decimal(lineSplit[7])

  areaList = []
  baseQuery = "UPDATE zipcode_population SET area = "

  for k, v in zipPopDict.items():
    areaList.append(baseQuery + str(v) + " WHERE zcta = '" + k + "'")

  for q in areaList:
    cur.execute(q)

db.close()
