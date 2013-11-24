import MySQLdb
import sys
from string import maketrans

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="lcv232", # your username
                       passwd="12345", # your password
                       db="coursedb") # name of the data base

#The Cursor object will let you execute the sql commands
cur = db.cursor()

query = "select distinct i.Address from coursedb.BOROUGH b join coursedb.INCIDENTS i on i.Zipcode = b.zipcode where b.BoroughName in ('Queens', 'Bronx')"
cur.execute(query)

intab = "(),'"
outtab = "    "
transfer1 = maketrans(intab, outtab)
address = []
print "Data of the Addresses where Incidents occurred in either Queens OR Bronx is in the file BXQNAddressesWithIncidents.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(transfer1)
    address.append(string.strip())
    string = ""


outputFile = open("BXQNAddressesWithIncidents.txt", "w")
print >> outputFile , "Addresses where incidents occurred in either Bronx or Queens: \n"
for x in address:
    print >> outputFile, x

outputFile.close()

# close connection
db.close()
