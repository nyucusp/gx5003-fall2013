import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

# create cursor object
cur = db.cursor()

# create boroughs table
createCommand1 = "create table if not exists boroughs (zip varchar(255), nameBorough varchar(255))"
cur.execute(createCommand1)

# create zipcode table
createCommand2 = "create table if not exists zipcodes (zip varchar(255), area decimal(10,9), population decimal)"
cur.execute(createCommand2)

# create incidents table
createCommand3 = "create table if not exists incidents (zip varchar(255), address varchar(255), numIncidents int)"
cur.execute(createCommand3)

"""
Read data
"""

fileBoroughs = open('boroughs.csv', 'r')

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

fileZip = open('zipCodes.csv', 'r')

linesZip = []
for line in fileZip:
	linesZip.append(line)
fileZip.close()

dictZip = {}
for i in range(1, len(linesZip)):
	if linesZip[i].split(',')[10]!="\n":
		dictZip[linesZip[i].split(',')[0]] = (float(linesZip[i].split(',')[10]), float(linesZip[i].split(',')[7]))

for key in dictZip
	insertCommand2 = "insert into zipcodes values(" + "'" + key "'" + "," + str(dictZip[key][1]) + "," + str(dictZip[key][0]) + ");"
	cur.execute(insertCommand2)

fileIncidents = open(incidents.csv', 'r')

linesIncidents = []
for line in fileIncidents:
	linesIncidents.append(line)
fileIncidents.close()

zipIncidents = []
numIncidents = len(linesIncidents)

for i in range(1, numIncidents):
	zipIncidents.append(linesIncidents[i].split(',')[1])

for i in range(1, len(linesIncidents)):
	zipIncidents = linesIncidents[i].split(',')[1][0:5]
	if (zipIncidents.isdigit()):
		addressIncidents = linesIncidents[i].split(',')[0].replace("'","")
		numIncidents = linesIncidents[i].split(',')[2][:-1]
		if numIncidents.isdigit()):
			insertCommand3 = "insert into incidents values(" + "'" + zipIncidents + "'" + "," + "'" + addressIncidents + "'" + "," + "'" + numIncidents + "'" + ");"
			cur.execute(insertCommand3)

db.commit()
db.close()
