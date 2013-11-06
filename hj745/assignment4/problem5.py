import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", user="hj745", passwd="000000", db="coursedb")
 
#The cursor object executes the sql commands
#List addresses of all incidents that have occurred either in Bronx or Queens
cur = db.cursor()
cur.execute("select incident_address from incidents left join (select distinct zip, borough from boroughs) newBoroughs on incidents.incident_zip=newBoroughs.zip where newBoroughs.borough='bronx' or newBoroughs.borough='queens' ")

# process the result
rows = cur.fetchall()
for row in rows:
    print row[0]

# close connection
db.close()
