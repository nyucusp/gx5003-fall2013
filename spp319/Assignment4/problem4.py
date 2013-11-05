import MySQLdb
import sys
from string import maketrans

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="spp319", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base

#The Cursor object will let you execute the sql commands
cur = db.cursor()

query = "select distinct i.Address from coursedb.borough b join coursedb.incidents i on i.Zipcode = b.zipcode where b.BoroughName = 'Manhattan'"
cur.execute(query)

intab = "(),'"
outtab = "    "
trantab = maketrans(intab, outtab)
addresses = []
print "Addresses where incidents occurred in Manhattan are in the file ManhattanAddressesWithIncidents.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(trantab)
    addresses.append(string.strip())
    string = ""


# rowIndex = 0
# for item in addresses:
#     print addresses[rowIndex]
#     print "\n"
#     rowIndex = rowIndex + 1

outFile = open("ManhattanAddressesWithIncidents.txt", "w")
print >> outFile , "Addresses where incidents occurred in Manhattan: \n"
for a in addresses:
    print >> outFile, a

outFile.close()

# close connection
db.close()
