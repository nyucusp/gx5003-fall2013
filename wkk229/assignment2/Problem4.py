import csv
import sys
#ration between population and area
#sort the code
#save in a new file


myfile = open('zipCodes.csv','r')
fileLines = myfile.readlines()

header = fileLines.pop(0).strip().split(',')
populationDensity={}
rows = []
area = 0.0
population = 0

#separing the rows so as to enable computation
for lines in fileLines:
    rows= lines.strip().split(',')
    #calculating the popdensity= pop/Area
    zipC =rows[0]
    if rows [7] and rows[10]:
        area= float(rows[7])
        population = int(rows[10])
        populationDensity[zipC] = (population/area)



#putting the code into the new file and saving it..also display the new file
if populationDensity != []:
    output=open("output_density_problem2.txt","w")
    for s in sorted (populationDensity.keys()):
        print >> output,s,populationDensity[s]
