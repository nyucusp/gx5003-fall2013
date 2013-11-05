import MySQLdb
import sys



# Here we connect to the database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rs4606", # your username
                       passwd="a1s2d3f4", # your password
                       db="coursedb") # name of the data base  

cur = db.cursor()   

"""
In this query we list all addresses from incidents that occurred in the Bronx or Queens.  
Note that some of these addresses are blank, corresponding to those incidents for which 
there was no listed address.  Note that we chose to do a UNION ALL to keep duplicates,
rather than a normal UNION, because the same address may exist in Bronx and Queens.
"""
query = "(SELECT address FROM boroughs JOIN incidents WHERE borough_name = 'Bronx' AND boroughs.zip = incidents.zip) UNION ALL (SELECT address FROM boroughs JOIN incidents WHERE borough_name = 'Queens' AND boroughs.zip = incidents.zip);"
cur.execute(query)
for row in cur.fetchall():
    print row[0]

db.close()
