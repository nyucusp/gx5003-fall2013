import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=Body", db="coursedb")

# create cursor object
cur = db.cursor()

# create boroughs table
createCommand1 = "create table if not exists boroughs (zip varcahr(255), borough_name varchar(255))"
cur.execute(createCommand1)

# create zipcode table
createCommand2 = "create table if not exists zipcodes (zip varchar(255), area decimal(10,9), population decimal)"
cur.execute(createCommand2)

# create incidents table
createCommand3 = "create table if not exists incidents (zip varcahr(255), address varchar(255), incident_count int)"
cur.execute(createCommand3)

"""
Read data
"""

fileBoroughs = ('boroughs.csv', 'r')

linesBoroughs = []
for line in fileBoroughs:
	linesBoroughs.append(line)
fileBoroughs.close()

for i in range(0, len(linesBoroughs)):
	nameBorough = linesBoroughs[i].split(',')[1][:-1]
	zipBorough = linesBoroughs[i].split(',')[0]
	insertCommand1 = "insert into boroughs values(" + "'" + zipBorough + "'" + "," + "'" + nameBorough + "'" + ");"
	cur.execute(insertCommand1)

# remove duplicates
removeduplicates = "ALTER IGNORE TABLE boroughs ADD UNIQUE INDEX (zip)"
cur.execute(removeduplicates)

db.commit()
db.close()
