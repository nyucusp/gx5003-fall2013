
from decimal import *
import csv
from number import numberOf
from collections import counter

code=csv.reader(open('zipCodes.csv'),delimiter=',')
bor= csv.reader(open('boroughs.csv'),delimiter=',')
zipIncident= csv.reader(open('Incidents.csv'),delimiter=',')
zipIncident.next () 
cities = [row[1] for row in zipIncident] 
freq=[]

for (x,y) in counter (cities).iteritems():
	freq.append((x,y))
zip_pop= [] 
code.next()

for row in code:
	zip_pop.append ((row[1],row[10]))
zip_boroughs=[] 
bor.next()

for row in bor:
	zip_boroughs.append((row[0],row[1]))

#
incidents = dict(freq)
population = dict(zip_pop)
borough = dict(zip_boroughs)

incident_in_borough= [(borough[id]) 
	for id in set(borough) & set (incidents)] 
population_in_borough=[(borough[id]) 
	for id in set(borough)& set (population)] 


class1= numberOf(len(incedent),len(population_in_borough),'Brooklyn',incident_in_borough,population_in_borough)
class2=numberOf(len(incedent),len(population_in_borough),'Bronx',incident_in_borough,population_in_borough)
class3=numberOf(len(incedent),len(population_in_borough),'Manhattan',incident_in_borough,population_in_borough)
class4=numberOf(len(incedent),len(population_in_borough),'Queens',incident_in_borough,population_in_borough)
class5=numberOf(len(incedent),len(population_in_borough),'Staten',incident_in_borough,population_in_borough)

outputFile= open('output_problem3.txt','w')
outputFile.write("Borough Name\tClass1\n")
outputFile.write("Bronx\t"+str(class1) +"\n"
                  "Brooklyn\t"+str(class2) +"\n"
                  "Manhattan\t"+str(class3) +"\n"
                  "Queens\t"+str(class4) +"\n"
                  "Staten\t"+str(class5) +"\n")
outputFile.close()
print "done"




	