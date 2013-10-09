import csv
import sys

#open and read all the necessary files properly
filezipCode = open('zipCodes.csv')
csvreaderzc = csv.reader(filezipCode, delimiter=',')
fileboroughs = open('boroughs.csv')
csvreaderb = csv.reader(fileboroughs, delimiter=',')
fileincidents = open('Incidents_grouped_by_Address_and_Zip.csv')
csvreaderinc = csv.reader(fileincidents, delimiter=',')

#counting the incidents per zipcode
incidents = {}
count = 0
for line in csvreaderinc:
	if count > 0 and line[1] != '':
		if line[1] in incidents.keys():
			incidents[line[1]]=incidents[line[1]]+1
		else:
			incidents[line[1]]=1
	#print incidents
	count = count + 1

#print incidents

#counting population per zipcode
population = {}
count = 0
for line in csvreaderzc:
	if count > 0 and line[10] != '':
			population[line[1]] = line[10]
	count = count + 1
#print population

#finding the ratio of incidents per population in each zipcode
ratio ={}
for key in incidents:
	if key in incidents.keys() and key in population.keys():
		ratio[key] = float(incidents[key])/float(population[key])
#print ratio

#finding the ratio of incidents per population in each Borough
Bronx = 0
Manhattan = 0
Staten = 0
Brooklyn = 0
Queens = 0

#tried different ways, but nothing was working
#seems to be the same issue that I'm having in problem 4
#can't figure out how to use 2 dictionaries at once

for key in ratio:
#	zip == line[0]
	if key != '' and key>=10001 and key<=10282:
			print ratio
			Manhattan = Manhattan + ratio[key]
#for line in csvreaderb:
#	if line[1] != '' and key in ratio.keys():
#		if line[1] == 'Bronx':
#			Bronx = Bronx + ratio[line[0]]
#		if line[1] == 'Manhattan':
#			Manhattan = Manhattan + ratio[line[0]]
#		if line[1] == 'Staten':
#			Staten = Staten + ratio[key]
#		if line[1] == 'Brooklyn':
#			Brooklyn = Brooklyn + ratio[key]
#		if line[1] == 'Queens':
#			Queens = Queens + ratio[key]

#write the ratio's into a txt document
sys.stdout = open('output_problem3.txt', 'w')

print Bronx
print Brooklyn
print Manhattan
print Staten
print Queens

