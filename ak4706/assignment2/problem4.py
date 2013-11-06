import sys
import csv
import collections

#from zip import Zipcode
from borough import Borough

#import and open the files
bor = sys.argv[1]
filezipCode = open('zipCodes.csv')
csvreaderzc = csv.reader(filezipCode, delimiter=',')
fileboroughs = open('boroughs.csv')
csvreaderb = csv.reader(fileboroughs, delimiter=',')
seq = csvreaderb

BorObj = Borough(bor)
#csvreaderb = csv.reader(fileboroughs, ['namezip','namebor'])

#counting population per zipcode
population = {}
count = 0
for line in csvreaderzc:
	if count > 0 and line[10] != '':
			population[line[1]] = line[10]
	count = count + 1
#print population

#tried to add the population for the whole borough but wasn't working and was
#messing up the rest - seems to be the same issue I'm having in problem #3

popMan = 0
for line[0] in csvreaderb:
	if line[1] == 'Manhattan':
		popMan = popMan + population[line[1]]
print popMan

#counting up the zips for each borough and finally got it to account for doubles :-)
countM = 0
countBx = 0
countBrook = 0
countSI = 0
countQ =0

seen = set()
def f7_nohash(seq):
	return [x for x in seq if str(x) not in seen and not seen.add(str(x))]
borough = {}
borough = [x for x in seq if str(x) not in seen and not seen.add(str(x))]
print borough
for line in borough:
	if line[1] == 'Manhattan':
 		countM = countM +1
	if line[1] == 'Bronx':
		countBx = countBx +1
	if line[1] == 'Brooklyn':
		countBrook = countBrook +1
	if line[1] == 'Staten':
		countSI = countSI +1
	if line[1] == 'Queens':
		countQ = countQ +1
print countM
print countBx
print countBrook
print countSI
print countQ

#use the class borough to calculate the average population for the given borough
BorObj.calcAvgPop(totPop, count)


#I tried to do it this way by making a dictionary and appending the population
#to the zip and borough, but it kept giving me errors.  And then I found a different
#way to do it with collections but still gave me errors.
# boroughgroup = collections.defaultdict(list)
# boroughgroup = {}

# for line in csvreaderb:
# 	if line[0]>10000:
# 		line[1] = line[1]

# count = 0
# for line in csvreaderzc:
# 	if (count>0 and line[0] in boroughgroup):
# 		line[1].append(line[10])
# 	elif(count>0 and line[0] != boroughgroup):
# 		line[1] = boroughgroup[line[10]]
# 	count = count + 1

# countM = 0
# countBx = 0
# countBrook = 0
# countSI = 0
# countQ =0

# for line in boroughgroup:
# 	if line[1] == 'Manhattan':
# 		countM = countM +1
# 	if line[1] == 'Bronx':
# 		countBx = countBx +1
# 	if line[1] == 'Brooklyn':
# 		countBrook = countBrook +1
# 	if line[1] == 'Staten':
# 		countSI = countSI +1
# 	if line[1] == 'Queens':
# 		countQ = countQ +1
# print countM
# print countBx
# print countBrook
# print countSI
# print countQ