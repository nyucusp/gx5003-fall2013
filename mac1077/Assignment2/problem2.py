import csv
import sys

myfile = open('zipCodes.csv','r')
fileLines = myfile.readlines()

header = fileLines.pop(0).strip().split(',')
populationDensity={}
rows = []
area = 0.0
population = 0

#breaking the rows 
for lines in fileLines:
    rows= lines.strip().split(',')
    #population density per Area
    zipC =rows[0]
    if rows [7] and rows[10]:
        area= float(rows[7])
        population = int(rows[10])
        populationDensity[zipC] = (population/area)

#code into new file
if populationDensity != []:
    output=open("output_density_problem2.txt","w")
    for s in sorted (populationDensity.keys()):
        print >> output,s,populationDensity[s]
