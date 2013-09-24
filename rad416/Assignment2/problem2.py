zipcodeInFile = open('zipCodes.csv', 'r')
# outFile = open('output_density_problem2.txt', 'w')
next(zipcodeInFile)
for line in zipcodeInFile:
  split_line = line.split(",")
  if split_line[10] != '\n':
    print "The population density of " + split_line[0] + " is " + str((float(split_line[10])/float(split_line[3])))

zipcodeInFile.close()