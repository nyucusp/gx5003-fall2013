import MySQLdb
import sys



# Here we connect to the database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rs4606", # your username
                       passwd="a1s2d3f4", # your password
                       db="coursedb") # name of the data base  

cur = db.cursor()   

"""
In this query we list all Manhattan zip codes along with their populations where 
incidents occurred.
"""
query = "SELECT intermediate.zip, population FROM (SELECT distinct incidents.zip FROM boroughs JOIN incidents WHERE borough_name = 'Manhattan' AND boroughs.zip = incidents.zip) AS intermediate JOIN zipcodes WHERE intermediate.zip = zipcodes.zip;"
cur.execute(query)

for row in cur.fetchall():
    print row[0], row[1]
db.close()
