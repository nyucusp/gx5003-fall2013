import csv
import sys

Func2 = open('C:/Git_CUSP/gx5003-fall2013/lcv232/Assignment2/zipCodes.csv','r')
data2 = csv.reader(Func2, delimiter = ',')


array2 = []
data2.next()

# For Loop for picking data in array field values & arrangement

for line in data2:
    total1 = line[10]
    if total1 != '': 
        volume = float(line[10])/float(line[7])
        zip = int(line[1])
        value = zip, volume
        array2.append(value)

arrNEW = sorted(array2)
outputFile = open('Output_Density_PRBLM2.txt','w')

#For loop for Output Data

for val in arrNEW:
    outputFile.write(str(val)+'\n')
outputFile.close()

Func2.close()
