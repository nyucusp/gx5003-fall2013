import sys

inputFile = open('input3.txt', 'r')                       # open .txt file

inputLines = []                                           # save lines in a list
for line in inputFile:
  inputLines.append(line)
inputFile.close()
