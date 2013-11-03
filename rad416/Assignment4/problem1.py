import sys
from _collections import defaultdict
import MySQLdb
import warnings
warnings.filterwarnings("ignore")

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rad416", # your username
                       passwd="mysql", # your password
                       db="coursedb") # name of the data base

with db:

  # The Cursor object will let you execute the sql commands
  cur = db.cursor()

  query = "DROP TABLE IF EXISTS zipcode_population"
  cur.execute(query)

  query = "CREATE TABLE zipcode_population ( zcta INT, total_population INT,PRIMARY KEY (zcta) )"
  cur.execute(query)

  query = "DROP TABLE IF EXISTS boroughs_raw"
  cur.execute(query)

  query = "CREATE TABLE boroughs_raw ( zipcode INT, borough VARCHAR(40) )"
  cur.execute(query)

  query = "DROP TABLE IF EXISTS incidents"
  cur.execute(query)

  query = "CREATE TABLE incidents ( zipcode INT, incidents INT )"
  cur.execute(query)

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

  #upload incidents file (original with commas in col 1)
  zipIncidentFile = open('Incidents_grouped_by_Address_and_Zip.csv','r')
  next(zipIncidentFile) #skip header row
  zipIncidentDict = defaultdict(int) #dict to capture zipcodes and counts
  for line in zipIncidentFile:
    lineSplit = line.split(",")
    if(len(lineSplit) == 3 and len(lineSplit[1]) >= 5 and lineSplit[1][0] == '1'):
      zipIncidentDict[lineSplit[1][ :5]] += int(lineSplit[2].rstrip())
  
  zipIncidentFile.close()

  incidentsList = []
  baseQuery = "INSERT IGNORE INTO incidents (zipcode, incidents) VALUES "
  for k,v in zipIncidentDict.items():
    incidentsList.append(baseQuery + "('" + k + "','" + str(v) + "')")

  for q in incidentsList:
    cur.execute(q) 

db.close()
# #populate boroughZipList
# for line in boroughZipFile:
#   lineSplit = line.split(",")
#   boroughZipList.append([lineSplit[0], lineSplit[1].rstrip()])

#parse 

#parse incidents file and upload
