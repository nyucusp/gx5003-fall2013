from avgpop import avgPop
from numberof import numberOf
from decimal import *
import csv
import sys

bname = str(sys.argv[1]).title() #capitalize the first letter

reader = csv.reader(open('zipCodes.csv'), delimiter=',')
reader1 = csv.reader(open('boroughs.csv'), delimiter=',')

zipop = [] #this is a list of zipcodes and populations
reader.next()
for row in reader:
    zipop.append((row[1],row[10]))
boroughs = [] #this is a list of boroughs and zipcodes
reader1.next()
for row in reader1:
    boroughs.append((row[0],row[1]))

population = dict(zipop)
borough = dict(boroughs)
popboro=[(borough[id], population[id]) for id in set(borough) & set(population)]

x = avgPop(len(popboro),bname,popboro)
print x

