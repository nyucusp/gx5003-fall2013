import MySQLdb
import sys
import csv


Borough_name = sys.argv[1]

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="lcv232", # your username
                   passwd="12345", # your password
                   db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands
cur = db.cursor()
query = "select distinct z.PopulationPerZipcode, b.zipcode from coursedb.BOROUGH b join coursedb.ZIPCODE z on z.ZipcodeTab = b.zipcode where b.BoroughName = " + "'" + Borough_name + "'"
cur.execute(query)
Pop_Overall = 0
zipc_arr = []
for row in cur.fetchall() :
    Pop_Overall += row[0]
    zipc_arr.append(row[1])

zipc_arr = ', '.join(str(x) for x in zipc_arr)
query = "select count(*) from coursedb.INCIDENTS where zipcode in (" + zipc_arr + ")"
cur.execute(query)
Incid_Overall = 0
for row in cur.fetchall() :
    Incid_Overall = row[0]

print "Total Population from the Borough " + Borough_name + " is : " + str(Pop_Overall) + " \n & Incidents: " + str(Incid_Overall)
print "The Ratio of Incidents per Population is : " + str(float(Incid_Overall) / float(Pop_Overall))
# close connection
db.close()

    