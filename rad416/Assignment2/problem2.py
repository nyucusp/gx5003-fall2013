# A script to take in a file of zipcodes with populations, calculate the density
# and output those to a file, ignoring any zipcodes without a population figure
# output is likely population per decimal degree, though it's not clear from the 
# source file what the units are.

from _collections import defaultdict

zipcodeInFile = open('zipCodes.csv', 'r')

next(zipcodeInFile) #skip header in file

zipAreaPopList = [] #list to hold processed file contents

for line in zipcodeInFile: #iterate to populate list from file contents
  split_line = line.split(",") #split line into list
  if split_line[10] != '\n': #test for a blank in population
    zipAreaPopList.append([ split_line[0], [ split_line[7], split_line[10].rstrip()] ] )

#end loop with list of form [zipcode, [zipcodeArea, zipcodePopulation]]

zipcodeInFile.close()

#convert list to dict and aggregate area and population
zipAreaPopDict = defaultdict(list)
for k,v in zipAreaPopList:
    zipAreaPopDict[k].append(v)

#test for multiple population and area entries in dict and aggregate
for k in zipAreaPopDict:
    if (len(zipAreaPopDict[k])>1): #aggregate figures for multiples
        zipAreaPopDict[k] = [[str( float(zipAreaPopDict[k][0][0]) + float(zipAreaPopDict[k][1][0]) ),str( float(zipAreaPopDict[k][0][1]) + float(zipAreaPopDict[k][1][1]) )]]

#output result
outFile = open('output_density_problem2.txt', 'w') #open output file
for k in sorted(zipAreaPopDict):
  popPerArea = str(float(zipAreaPopDict[k][0][1]) / float(zipAreaPopDict[k][0][0])) #variable to hold ration
  outFile.write(k)
  outFile.write(" ")
  outFile.write(popPerArea)
  outFile.write('\n')

outFile.close()