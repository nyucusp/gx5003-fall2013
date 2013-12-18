import MySQLdb
import csv

db = MySQLdb.connect(host="localhost", user="agb344", passwd="amir", db="assignment4")

cur = db.cursor()

query = "select zipcode, population from zipcodes where zipcode in (select zipcode from incidents where zipcode in (select zipcode from zipBoroughs where borough = 'manhattan'));"

'''
SELECT zipcode, population
FROM zipcodes
WHERE zipcode IN
(
    SELECT zipcode
    FROM incidents
    WHERE zipcode IN
    (
        SELECT zipcode
        FROM zipBoroughs
        WHERE borough = 'Manhattan'
    )
);
'''

cur.execute(query)

results = cur.fetchall()

for result in results:
    print str(result[0]) + ", " + str(result[1])

db.close()
