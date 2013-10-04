
import csv
import sys
f = open("//home/jeongki/gx5003-fall2013/jl2684/assignment2/output_problem3.txt", 'w')
sys.stdout = f

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


''' Incidents & Zipcode ''' 

zipIncilist =[]
incilist = []

for row in nycLine:
	zipcode = row[1]
	incident = row[2]
	zipIncilist.append(row[1].rstrip('\n'))
	incilist.append(row[2].rstrip('\n'))

zipIncidic = dict(zip(zipIncilist, incilist))

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
 

''' Incidents by Boroughs ''' 

ManhattanIn = []
BrooklynIn = []
BronxIn = []
StatenIn = []
QueensIn = []
for key, value in zipIncidic.iteritems(): 
	for item in zipManhattan:
		if item == key: 
			ManhattanIn.append(value)
	for item in zipBrooklyn:
		if item == key: 
			BrooklynIn.append(value)
	for item in zipBronx:
		if item == key: 
			BronxIn.append(value)
	for item in zipStaten:
		if item == key: 
			StatenIn.append(value)
	for item in zipQueens: 
		if item == key: 
			QueensIn.append(value)


ManhattanInFloat = []
BrooklynInFloat = []
BronxInFloat = []
StatenInFloat = []
QueensInFloat = []

for value in ManhattanIn:
	if value != '':
		ManhattanInFloat.append(float(value))
for value in BrooklynIn:
	if value != '':
		BrooklynInFloat.append(float(value))
for value in BronxIn:
	if value != '':
		BronxInFloat.append(float(value))
for value in StatenIn:
	if value != '':
		StatenInFloat.append(float(value))
for value in QueensIn:
	if value != '':
		QueensInFloat.append(float(value))

ManI = sum(ManhattanInFloat) 
BknI = sum(BrooklynInFloat) 
BrxI = sum(BronxInFloat)
StaI = sum(StatenInFloat)  
QnsI = sum(QueensInFloat) 

''' Ratio by Boroughs ''' 

ManRatio = ManI/ManP
BknRatio = BknI/BknP
BrxRatio = BrxI/BrxP
StaRatio = StaI/StaP
QnsRatio = QnsI/QnsP

print 'Bronx' + ' ' + str(BrxRatio)
print 'Brooklyn' + ' ' + str(BknRatio)
print 'Manhattan' + ' ' + str(ManRatio)
print 'Queens' + ' ' + str(QnsRatio)
print 'Staten Island' + ' ' + str(StaRatio) 




zipFile.close()
nycFile.close()
boroughsFile.close()
