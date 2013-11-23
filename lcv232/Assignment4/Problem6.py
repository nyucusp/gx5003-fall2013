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

query = "select distinct b.zipcode, z.PopulationPerZipcode from coursedb.BOROUGH b join coursedb.ZIPCODE z on z.ZipcodeTab = b.zipcode where b.BoroughName = 'Manhattan' and b.zipcode in (select zipcode from coursedb.INCIDENTS)"
cur.execute(query)

intab = "(),'L"
outtab = "     "
transfer1 = maketrans(intab, outtab)
address = []
print "Data of Manhattan Zipcodes and the corresponding populations from where the Incidents have occurred are in the file ManhattanZipPop.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(transfer1)
    address.append(string.strip())
    string = ""


outputFile = open("ManhattanZipPop.txt", "w")
print >> outputFile , "Data of the Zipcodes and the corresponding Populations from where Incidents have occurred in Manhattan are: \n"
for x in address:
    print >> outputFile, x

outputFile.close()

# close connection
db.close()
