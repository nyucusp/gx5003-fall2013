# A script to take in a file of zipcodes with populations, calculate the density
# and output those to a file, ignoring any zipcodes without a population figure
# output is population per square mile.

zipcodeInFile = open('zipCodes.csv', 'r')

next(zipcodeInFile) #skip header in file

zipList = [] #list to hold processed file contents

for line in zipcodeInFile:
  split_line = line.split(",") #split line into list
  if split_line[10] != '\n': #test for a blank in population
    zipList.append([ split_line[0], (float(split_line[10])/float(split_line[3]))])

zipcodeInFile.close()
zipListSorted = sorted(zipList)
outFile = open('output_density_problem2.txt', 'w') #open output file
for i in range(0,len(zipListSorted)):
  outFile.write(zipListSorted[i][0])
  outFile.write(" ")
  outFile.write(str(zipListSorted[i][1]))
  outFile.write('\n')

outFile.close()