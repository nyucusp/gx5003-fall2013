import MySQLdb
import csv
import sys


db = MySQLdb.connect(host="localhost", user="agb344", passwd="amir", db="assignment4")          
cur = db.cursor()

boroughToFind = sys.argv[1]

incidentsQuery = "select sum(count) from (select count(zipcode) as count from incidents where zipcode in (select zipcode from zipBoroughs where borough = '"+boroughToFind+"') group by zipcode) as counts;"

populationQuery = "select sum(population) from zipcodes where zipcode in (select zipcode from zipBoroughs where borough = '"+boroughToFind+"');"

cur.execute(incidentsQuery)
numIncidents = cur.fetchall()[0][0]
#print numIncidents

cur.execute(populationQuery)
popTotal = cur.fetchall()[0][0]
#print popTotal

ratio = round(numIncidents / popTotal, 3)

print "The ratio of incidents to population in "+boroughToFind+" is "+str(ratio)+" incidents per person"

'''
query = "select zipcode from zipBoroughs where borough = '"+boroughToFind+"';"

db = MySQLdb.connect(host="localhost", user="agb344", passwd="amir", db="assignment4")
cur = db.cursor()

cur.execute(query)
#print str(cur.fetchall()[0])[1:-2]
zipTuples = cur.fetchall()
zipList = []
for zip in zipTuples:
    zipList.append(int(zip[0]))

#print zipList

numZips = len(zipList)
totalPop = 0
totalIncidents = 0

for zip in zipList:
    query = "select count(zipcode) from incidents where zipcode = "+str(zip)+";"
    cur.execute(query)
    #zipIncidents = cur.fetchall()[0]
    totalIncidents += cur.fetchall()[0][0]
print totalIncidents

for zip in zipList:
    query = "select population from zipcodes where zipcode = "+str(zip)+";"
    cur.execute(query)
    print cur.fetchall()


'''
db.close()

