import MySQLdb
import sys

# Here we save the user's input borough name as given_borough.  The borough name should
# be given WITHOUT quotation marks.
input = sys.argv
input.pop(0)
given_borough = input[0].split()[0]


# Here we connect to the database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rs4606", # your username
                       passwd="a1s2d3f4", # your password
                       db="coursedb") # name of the data base  

cur = db.cursor()   

"""
In these queries we compute the ratio of the number of incidents to the population of
the borough given by the user.  First we get the total population of given_borough, and
save this as total_pop, then we get the total number of incidents in given_borough, and
save this as total_incidents.  
"""
query = "select sum(population) from boroughs join zipcodes where borough_name = " + "'" + given_borough + "'" + "and boroughs.zip = zipcodes.zip;"
cur.execute(query)
total_pop = 0
for row in cur.fetchall():
    total_pop += row[0]



query2 = "select sum(incident_count) from boroughs join incidents where borough_name = " + "'" + given_borough + "'" + "and boroughs.zip = incidents.zip;"
cur.execute(query2)
total_incidents = 0
for row in cur.fetchall():
    total_incidents += row[0]


# Here we print the population density
print total_incidents/total_pop


db.close()
