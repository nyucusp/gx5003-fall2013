#Aliya Merali
#Urban Informatics
#Assignment 4
#Problem 3: Given a borough name, your task is to compute the ratio between the number of incidents and the population in that borough. 
 
import MySQLdb
import sys

bor_input = str(sys.argv[1]).title()

#connect to database
db = MySQLdb.connect(host="localhost", user="ajm777", passwd="pepper89", db="coursedb")
cur = db.cursor()   

query1 = "SELECT zip_code FROM bor WHERE name = %s"
cur.execute(query1, bor_input)

bor_zips = []
for row in cur.fetchall(): 
    zip_val = int(row[0])
    bor_zips.append(zip_val)

tot_pop = 0
tot_inc = 0
for element in bor_zips:  
    query2 = "SELECT pop_by_zip FROM zips WHERE zip_code = %s"
    cur.execute(query2, element)
    for row in cur.fetchall():
        tot_pop = tot_pop + int(row[0])

    query3 = "SELECT num_inc FROM inc WHERE zip_code = %s"
    cur.execute(query3, element)
    for row in cur.fetchall():
        tot_inc = tot_inc + int(row[0])

ratio = float(tot_inc)/float(tot_pop)
print 'The ratio between the number of incidents and the population in ' + str(bor_input) + ' is: ' + str(ratio)


db.close()
