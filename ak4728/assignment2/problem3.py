from numberof import numberOf
from decimal import *
import csv
from collections import Counter
#open the files in reader
reader = csv.reader(open('Incidents_grouped_by_Address_and_Zip.csv'), delimiter=',')
reader1 = csv.reader(open('zipCodes.csv'), delimiter=',')
reader2 = csv.reader(open('boroughs.csv'), delimiter=',')

reader.next() #skip header
cities = [row[1] for row in reader] #count how many times the same zip occurs

freq = [] #this is a list of zips and frequencies
for (k,v) in Counter(cities).iteritems():
    freq.append((k,v))
zipop = [] #this is a list of zipcodes and populations
reader1.next()
for row in reader1:
    zipop.append((row[1],row[10]))
boroughs = [] #this is a list of boroughs and zipcodes
reader2.next()
for row in reader2:
    boroughs.append((row[0],row[1]))

#Common ground is zipcodes, therefore I turned them into dictionaries in which I can match the zipcodes.
incidents = dict(freq)
population = dict(zipop)
borough = dict(boroughs)

incboro=[(borough[id], incidents[id]) for id in set(borough) & set(incidents)] #incidents and population
popboro=[(borough[id], population[id]) for id in set(borough) & set(population)] #population and borough name
#I created a class that calculates the total population and incidents for each boro and gives me the ratio
ratio1 = numberOf(len(incboro),len(popboro),'Bronx',incboro, popboro)
ratio2 = numberOf(len(incboro),len(popboro),'Brooklyn',incboro, popboro)
ratio3 = numberOf(len(incboro),len(popboro),'Manhattan',incboro, popboro)
ratio4 = numberOf(len(incboro),len(popboro),'Queens',incboro, popboro)
ratio5 = numberOf(len(incboro),len(popboro),'Staten',incboro, popboro)


outputFile = open('output_problem3.txt','w')
outputFile.write( "Borough Name\tRatio\n") #header
outputFile.write("Bronx\t\t"+str(ratio1)+"\n"
                 "Brooklyn\t"+str(ratio2)+"\n"
                 "Manhattan\t"+str(ratio3)+"\n"
                 "Queens\t\t"+str(ratio4)+"\n"
                 "Staten\t\t"+str(ratio5)+"\n")
outputFile.close()

print "done"
    









