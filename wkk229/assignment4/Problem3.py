import MySQLdb
import sys

givenBorough = sys.argv[1]

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="wkk229", # your username
                   passwd="python", # your password
                   db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands
cur = db.cursor()
query = "select distinct z.PopPerZip, b.zipcode from coursedb.borough b join coursedb.zipcodes z on z.ZipcodeTab = b.zipcode where b.BoroughName = " + "'" + givenBorough + "'"
cur.execute(query)
totalPop = 0
zipcodes = []
for row in cur.fetchall() :
    totalPop += row[0]
    zipcodes.append(row[1])

zipcodes = ', '.join(str(x) for x in zipcodes)
query = "select count(*) from coursedb.incidents where zipcode in (" + zipcodes + ")"
cur.execute(query)
totalIncidents = 0
for row in cur.fetchall() :
    totalIncidents = row[0]

print "Total population from " + givenBorough + ": " + str(totalPop) + " \nIncidents: " + str(totalIncidents)
print "Ratio of incidents per pop: " + str(float(totalIncidents) / float(totalPop))
# close connection
db.close()

    