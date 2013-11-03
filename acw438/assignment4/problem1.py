#Alex Chohlas-Wood (acw438). Assignment 4, Problem 1.

import MySQLdb
import csv

#Initialize database variables
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')
cur = db.cursor()


try:
    cur.execute('DROP TABLE zip_incidents')
    cur.execute('DROP TABLE zip_population_area')
    cur.execute('DROP TABLE zip_boroughs')
except:
    pass

#DEFINE FUNCTIONS
def emptyChk(string):
    if string == "":
        return "DEFAULT"
    else:
        return string

def stringChk(string):
    if string == "":
        return False
    try:
        int(string)
        return string
    except:
        return False
    


#ADD ZIPCODE & INCIDENTS

#Initialie original file
incidentsFile = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')
incidentsCSV = csv.reader(incidentsFile)
incidentsList = list(incidentsCSV)[1:]

#Create table
maketable = "CREATE TABLE zip_incidents (address VARCHAR(255), zip VARCHAR(5) NOT NULL, incidents INT, records INT, primary key (address))"
cur.execute(maketable)

#Add incident count to table
#rejects = 0
abbreviations = [['ST', 'STREET'], ['AVE', 'AVENUE'], ['BLVD', 'BOULEVARD'], ['PL', 'PLACE'], \
                 ['W', 'WEST'], ['E', 'EAST'], ['N', 'NORTH'], ['S', 'SOUTH'], \
                 ['SW', 'SOUTHWEST'], ['SE', 'SOUTHEAST'], ['NW', 'NORTWEST'], ['NE', 'NORTHEAST'], \
                 ['SW', 'SOUTH WEST'], ['SE', 'SOUTH EAST'], ['NW', 'NORTH WEST'], ['NE', 'NORTH EAST'], \
                 [' SW', ' S W '], [' SE', ' S E '], [' NW', ' N W '], [' NE', ' N E ']]
for line in incidentsList:
    zipcode = line[1][:5]
    if stringChk(zipcode):
        standardized = line[0] + (" ") #Add space on end of address for 'S W' type abbreviations
        for abbr in abbreviations: #Standardize address
            standardized = standardized.replace(abbr[1], abbr[0])
        standardized = standardized.strip() #Delete leading or trailing spaces
        standardized = ' '.join(standardized.split()) #Eliminate double spaces
        doubleUpQuotes = '\"' + standardized + '\"' #Surround in double quotes for MySQL
        add_tuple = "INSERT zip_incidents " + \
                    "VALUES (" + doubleUpQuotes + ",'" + zipcode + "','" + line[2] + "',1)" + \
                    "ON DUPLICATE KEY UPDATE incidents=incidents+VALUES(incidents), " + \
                    "records=records+1"
        cur.execute(add_tuple)
    # else:
    #     rejects += 1
#print rejects, "rejected records"
#print len(incidentsList), "total records"
incidentsFile.close()



#ADD ZIPCODE AREA & POPULATION DATA

#Initialize original file
areapopFile = open('zipCodes.csv', 'r')
areapopCSV = csv.reader(areapopFile)
areapopList = list(areapopCSV)[1:]

#Create table
maketable = 'CREATE TABLE zip_population_area (zip VARCHAR(5) NOT NULL, area DOUBLE(9,9), population INT, records INT, primary key (zip))'
cur.execute(maketable)

#Add rows to table
#duplicates = 0
for item in areapopList:
    add_tuple = "INSERT zip_population_area " + \
                "VALUES ('" + item[0] + "'," + item[7] + "," + \
                (emptyChk(item[10])) + ",1)" + \
                "ON DUPLICATE KEY UPDATE area=area+VALUES(area), " + \
                "records=records+1" + \
                (", population=IFNULL(population,0)+VALUES(population)" if item[10] else "")


#    if item[0] == "12066": print add_tuple
    cur.execute(add_tuple)
areapopFile.close()



#ADD ZIPCODE BOROUGH DATA

#Initialize original file
borFile = open('boroughs.csv', 'r')
borCSV = csv.reader(borFile)

#Create table
maketable = 'CREATE TABLE zip_boroughs (zip VARCHAR(5) NOT NULL, borough varchar(255), records INT, primary key (zip))'
cur.execute(maketable)

#Add rows to table
#duplicates = 0
for item in borCSV:
    add_tuple = "INSERT zip_boroughs VALUES('" + item[0] + "','" + item[1] + "',1)" + \
                "ON DUPLICATE KEY UPDATE records=records+1"
    cur.execute(add_tuple)
borFile.close()



#COMMIT and CLOSE DATABASE
db.commit()
db.close()
