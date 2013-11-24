import MySQLdb
import sys 
input = str(sys.argv[1])

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="jl2684", # your username
                    passwd="199900", # your password
                    db="coursedb") # name of the data base  
cur = db.cursor()   

query = "select population_of_zip, area from zipcode where zipcode = " + input

cur.execute(query)

for row in cur.fetchall() :
    print float(row[0])/float(row[1])

db.close() 
