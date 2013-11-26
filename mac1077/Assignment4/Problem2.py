import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="mac1077",passwd="miquel",db="coursedb")
cur = db.cursor()

zip_code=sys.argv[1]

query = "SELECT (population/area) from zipcodes where zip = "+"'"+zip_code+"'"+";"
cur.execute(query)

for row in cur.fetchall():
        print row[0]
db.close()