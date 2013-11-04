import MySQLdb
import sys

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="jj1006", # your username
                     passwd="jpwd", # your password
                     db="coursedb") # name of the data base
# The Cursor object will let you execute the sql commands
cur = db.cursor()
cur.execute("select count(i.id) from boroughs b, incidents i where b.borough=\"" + sys.argv[1]+ "\" and b.zip=i.zip;")
numincidents = cur.fetchall()[0][0]
# NOTE: problematic because not all zip codes are in zipCodes.csv, so the estimate of population density is incomplete
cur.execute("select sum(z.population)/sum(z.area) from boroughs b, zipCodes z where b.borough=\""+sys.argv[1]+"\" and b.zip=z.zip and z.population is not null;")
pdensity = cur.fetchall()[0][0]

print str(numincidents)+"/"+str(pdensity)

db.close()
