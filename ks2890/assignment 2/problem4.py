import sys
import csv
from collections import defaultdict

zipCodes = open('zipCodes.csv')
zipCodes = csv.reader(zipCodes)

boroughs = open('boroughs.csv')
boroughs = csv.reader(boroughs)

output = open('output_problem4.txt' , 'w')

#b = str(sys.argv[1])
pop = []
bDict = defaultdict(list)
myDict={}


class borough(object):
	def __init__(self, b, zipcode,population):
		self.zipcode = zipcode
		self.population = population
		self.b = b
	def average(self):
		for row in zipCodes:
			if row[10] != '':
				zipcode = row[1]
				population = row[10]
				zip_pop = zipcode +" " +population+"\n"
				pop.append(zip_pop)
				print zip_pop
manhattan = borough("manhattan", 11211, 1000)
print manhattan.average

for row in boroughs:
	borough = row[1]
	bDict[borough].append(row[0])


for key in bDict:
	bDict[key]
	pop_sum = 0
	for zipcode in bDict[key]:
		if zipcode in myDict:
			pop_sum += int(myDict[zipcode])
	output.write(str(pop_sum))
	output.write(" ")