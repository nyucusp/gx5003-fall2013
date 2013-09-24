zipcodeInFile = open('zipCodes.csv', 'r')
outFile = open('output_density_problem2.txt', 'w')
next(zipcodeInFile) #skip header in file

zipList = []

for line in zipcodeInFile:
  split_line = line.split(",")
  if split_line[10] != '\n': #test for a blank in population
    zipList.append([ split_line[0], (float(split_line[10])/float(split_line[3]))])

zipcodeInFile.close()
zipListSorted = sorted(zipList)
# print zipList
for i in range(len(zipListSorted)):
  output = zipListSorted[i][0] + " " + str(zipListSorted[i][1])
  outFile.write(output)

outFile.close()