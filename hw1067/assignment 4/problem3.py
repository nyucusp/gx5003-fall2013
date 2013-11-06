    ##########################
    #  Assignment4 Problem3  #
    #  Haozhe Wang           #
    ##########################

import MySQLdb
import sys

boroughinput = sys.argv[1]

db = MySQLdb.connect(host = "localhost",
	user = "hw1067",
	passwd = "81828384yomama",
	db = "coursedb")
cur = db.cursor()
"""
#find population using this query 
query = "SELECT b.name FROM boroughs AS b "
query1 = "SELECT SUM(pop_by_zip) FROM zips WHERE  GROUP BY "+ "'" + boroughinput + "'" +"";""      

query = "SELECT i.num_inc/z.pop_by_zip FROM incident AS i INNER JOIN zips AS z ON z.zip_code = i.zip_code INNER JOIN boroughs as b on z.zip_code = b.zip_code WHERE b.name = "+ "'" + boroughinput + "'" +" GROUP BY "+ "'" + boroughinput + "'" +"" ON 
"""

query_king = "SELECT bp.name, bi.num_inc/bp.pop_by_zip FROM (SELECT b.name name,SUM(num_inc) FROM incident AS i INNER JOIN boroughs AS b ON i.zip_code = b.zip_code WHERE b.name = '"+sys.argv[1]+"' GROUP BY b.name) AS bi INNER JOIN (SELECT b.name name,SUM(pop_by_zip) FROM zips as z INNER JOIN boroughs AS b ON z.zip_code = b.zip_code WHERE b.name = '" + sys.argv[1] +"' GROUP BY b.name) as bp on bi.name = bp.name"
#subquery1 = "SELECT SUM(num_inc) FROM incident as i INNER JOIN boroughs AS b ON i.zip_code = b.zip_code WHERE b.name = '"+sys.argv[1]+"' GROUP BY b.name"
#subquery2 = "SELECT SUM(pop_by_zip) FROM zips as z INNER JOIN boroughs AS b ON z.zip_code = b.zip_code WHERE b.name = '" + sys.argv[1] +"' GROUP BY b.name"
cur.execute(query)

for row in cur.fetchall():
	print row
# close connection
db.close()


