import sys
import csv
from zipcode import Zipcode
from borough import Borough

boro = sys.argv[1]

boro=csv.reader(open("boroughs.csv","rb"),delimiter=',')
b1=list(boro)
zips=csv.reader(open("zipCodes.csv","rb"),delimiter=',')
z3=list(zips)

zippop={}
boroughs={}

for i in range(1,len(z3)):
	zippop[z3[i][0]]=z3[i][10]


for i in range(0,len(b1)):
	if b1[i][1] not in boroughs:
		boroughs[b1[i][1]] = Borough(b1[i][1])
	zipcode = Zipcode(int(b1[i][0]),1)
	boroughs[b1[i][1]].addZipCode(zipcode.number)


for i in range(0,len(boroughs)):
	boroughs[b1[i][1]].sumpopul=0
	for j in range(0,len(boroughs[boroughs.keys()[i]].zipcodes)):
		boroughs[b1[i][1]].avgZipPop2(int(zippop[str(boroughs[boroughs.keys()[i]].zipcodes[j])]))
	
		#boroughs[b1[i][1]].avgZipPop()

