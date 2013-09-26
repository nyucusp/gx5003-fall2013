import csv
from collections import defaultdict

zipCodes = open('zipCodes.csv')
zipCodes = csv.reader(zipCodes)
zipCodes.next()

boroughs = open('boroughs.csv')
boroughs = csv.reader(boroughs)

incidents = open('incidents.csv')
incidents = csv.reader(incidents)
incidents.next()

output = open('output_problem3.txt', 'w')
inc_list = open('inc_list.csv', 'w')
inc_list2 = open('inc_list.csv' , 'r')
inc_list2 = csv.reader(inc_list2)
print inc_list2

myDict={}
bDict = defaultdict(list)
inDict = defaultdict(list)
compDict = defaultdict(list)

for row in zipCodes:
	zipcode = row[1]
	population = row[10]
	if population == '':
		population = 0
	myDict[zipcode] = population

for row in incidents:
	incident = row[2]
	zipcode =row[1]
	if incident > 1:
		incident = 1
	inDict[zipcode] = incident

for row in boroughs:
	borough = row[1]
	bDict[borough].append(row[0])

for key in bDict:
	bDict[key]
	inc_sum = 0
	for zipcode in bDict[key]:
		if zipcode in inDict:
			inc_sum += int(inDict[zipcode])
			inc = str(zipcode) + ", " + str(inc_sum) + ", " + str(borough)+"\n"
			inc_list.write(inc)

#for row in inc_list2:
#	zipcode = row[0]
#	incident = row[1]
#	borough = row[2]
#	if incident == 0:
#		pass
#	data = str(incident) + ", " + str(borough)
#	compDict[zipcode].append(data)

for key in bDict:
	bDict[key]
	pop_sum = 0
	for zipcode in bDict[key]:
		if zipcode in myDict:
			pop_sum += int(myDict[zipcode])
	output.write(str(pop_sum))
	output.write(" ")