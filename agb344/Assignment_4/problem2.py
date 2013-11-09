import MySQLdb
import csv
import sys

zipToFind = sys.argv[1]

query = "select population/area from zipcodes where zipcode ='"+zipToFind+"';"

db = MySQLdb.connect(host="localhost", user="agb344", passwd="amir", db="assignment4")
cur = db.cursor()

cur.execute(query)
print cur.fetchall()[0]

db.close()
