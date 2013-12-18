import MySQLdb
import csv

db = MySQLdb.connect(host="localhost", user="agb344", passwd="amir", db="assignment4")

cur = db.cursor()

query = "select address from incidents where zipcode in (select zipcode from zipBoroughs where borough = 'Manhattan');"

'''
SELECT address
FROM incidents
WHERE zipcode in
(
    SELECT zipcode
    FROM zipBoroughs
    WHERE borough = 'Manhattan'
);
'''


cur.execute(query)

addresses = cur.fetchall()

for address in addresses:
    if address[0] != '':
        print address[0]

db.close()
