import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", user="hj745", passwd="000000", db="coursedb")
 
# The cursor object executes the sql commands
#List the set of zip codes in Manhattan along with their population where incidents have occurred
cur = db.cursor()

cur.execute("select distinct name, total_population_per_zip_code from zipcodes right join (select incident_zip from incidents left join (select distinct zip, borough from boroughs) newBoroughs on incidents.incident_zip=newBoroughs.zip where newBoroughs.borough='manhattan') newIncidentManhattan on zipcodes.name=newIncidentManhattan.incident_zip")

# process the result
rows = cur.fetchall()
for row in rows:
    print row[0], row[1]

# close connection
db.close()

