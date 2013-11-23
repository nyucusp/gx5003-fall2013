import MySQLdb
import sys

borough_input = sys.argv[1]


db = MySQLdb.connect(host="localhost",user="mac1077",passwd="miquel",db="coursedb")
cur=db.cursor()

query="SELECT sum(population) FROM boroughs, zipcodes WHERE boroughs.borough_name=" + "'" + borough_input + "' AND boroughs.zip=zipcodes.zip;"
print query
cur.execute(query)
total_population = 0
for row in cur.fetchall():
        total_population += row[0]

query2="SELECT sum(incidents_num)FROM boroughs, incidents WHERE borough_name="+"'"+borough_input+"' AND boroughs.zip=incidents.zip;"
print query2
cur.execute(query2)
total_incidents=0
for row in cur.fetchall():
        total_incidents += row[0]
print total_incidents/total_population
db.close