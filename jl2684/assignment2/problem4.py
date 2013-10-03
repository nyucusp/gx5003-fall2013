import sys
import csv
BoroughName = sys.argv[1]


zipFile = open('/home/jeongki/Documents/zipCodes.csv', 'rb')
zipLine = csv.reader(zipFile)

nycFile = open('/home/jeongki/Documents/Incidents_grouped_by_Address_and_Zip.csv', 'rb')
nycLine = csv.reader(nycFile) 

boroughsFile = open('/home/jeongki/Documents/boroughs.csv', 'rb')
boroughsLine = csv.reader(boroughsFile) 


'''Boroughs & Zipcode''' 
with open('/home/jeongki/Documents/boroughs.csv') as f: 
	BoroughsDic = dict(filter(None, csv.reader(f)))

zipManhattan =[]
zipBrooklyn = []
zipBronx = []
zipStaten = []
zipQueens = []

for key, value in BoroughsDic.iteritems(): 
	if value == 'Manhattan':
		zipManhattan.append(key)
	if value == 'Brooklyn':
		zipBrooklyn.append(key)
	if value == 'Bronx':
		zipBronx.append(key)
	if value == 'Staten':
		zipStaten.append(key)
	if value == 'Queens':
		zipQueens.append(key)

''' Zipcode Total by Boroughs ''' 

ManZipTotal = len(zipManhattan)
BknZipTotal = len(zipBrooklyn)
BrxZipTotal = len(zipBronx)
StaZipTotal = len(zipStaten)
QnsZipTotal = len(zipQueens)


''' Population & Zipcode ''' 

ziplist =[]
poplist = []

for row in zipLine:
	zipcode = row[1]
	pop = row[10]
	ziplist.append(row[1].rstrip('\n'))
	poplist.append(row[10].rstrip('\n'))

del ziplist[0]
del poplist[0]


zipPopdic = dict(zip(ziplist, poplist))


''' Population by Boroughs ''' 

ManhattanPop = []
BrooklynPop = []
BronxPop = []
StatenPop = []
QueensPop = []
for key, value in zipPopdic.iteritems(): 
	for item in zipManhattan:
		if item == key: 
			ManhattanPop.append(value)
	for item in zipBrooklyn:
		if item == key: 
			BrooklynPop.append(value)
	for item in zipBronx:
		if item == key: 
			BronxPop.append(value)
	for item in zipStaten:
		if item == key: 
			StatenPop.append(value)
	for item in zipQueens: 
		if item == key: 
			QueensPop.append(value)

ManhattanPopFloat = []
BrooklynPopFloat = []
BronxPopFloat = []
StatenPopFloat = []
QueensPopFloat = []

for value in ManhattanPop:
	if value != '':
		ManhattanPopFloat.append(float(value))
for value in BrooklynPop:
	if value != '':
		BrooklynPopFloat.append(float(value))
for value in BronxPop:
	if value != '':
		BronxPopFloat.append(float(value))
for value in StatenPop:
	if value != '':
		StatenPopFloat.append(float(value))
for value in QueensPop:
	if value != '':
		QueensPopFloat.append(float(value))

ManP = sum(ManhattanPopFloat) 
BknP = sum(BrooklynPopFloat) 
BrxP = sum(BronxPopFloat)
StaP = sum(StatenPopFloat)  
QnsP = sum(QueensPopFloat) 


AvgManPZ = ManP/ManZipTotal
AvgBknPZ = BknP/BknZipTotal
AvgBrxPZ = BrxP/BrxZipTotal
AvgStaPZ = StaP/StaZipTotal
AvgQnsPZ = QnsP/QnsZipTotal


if sys.argv[1] == 'manhattan': 
	print AvgManPZ
if sys.argv[1] == 'brooklyn':
	print AvgBknPZ
if sys.argv[1] == 'bronx':
	print AvgBrxPZ
if sys.argv[1] == "staten island":
	print AvgStaPZ
if sys.argv[1] == 'queens':
	print AvgQnsPZ


zipFile.close()
nycFile.close()
boroughsFile.close()
