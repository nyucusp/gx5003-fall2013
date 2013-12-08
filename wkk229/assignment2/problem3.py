#main idea is you want the ration of number of incidents /population for each borough

#from numberOf import numberOf
from decimal import *
import csv
#from collections import orderedDict 
#from numberOf import numberOf
#from collections import counter

#calculate number of accidents / create dictionaries fo ach file
#end product is:each line the name of borough and the calculated ratio 
#the lines should be sorted by alphabetically 

#creating dictionaries for each file 
#number of incidents per borough
#first open all files
code=csv.reader(open('zipCodes.csv'),delimiter=',')
bor= csv.reader(open('boroughs.csv'),delimiter=',')
zipIncident= csv.reader(open('Incidents.csv'),delimiter=',')
zipIncident.next () #so as to skip the header because you want to start from second colomn
#cities = [row[1] for row in zipIncident] #calculating how many times zip occurs
freq=[]

for row in zipIncident:
	freq.append(row[1])
zip_pop=[] #list of zip codes by population
code.next()
for row in code:
	zip_pop.append ((row[1],row[10]))

zip_boroughs=[] #list of boroughs and zipcodes
bor.next()

for row in bor:
	zip_boroughs.append((row[0],row[1]))

#the common among the three file is zipcode. thus we will use it to form dictionaris
incidents = dict(freq)
population = dict(zip_pop)
borough = dict(zip_boroughs)

incident_in_borough= [(borough[id]) 
	for id in set(borough) & set (incidents)] #incidents and population
population_in_borough=[(borough[id]) 
	for id in set(borough)& set (population)] #population and borough name

# we have to create a clas that calculates the total population and incidents for each borough
# then use them to calculate the ratio

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




	