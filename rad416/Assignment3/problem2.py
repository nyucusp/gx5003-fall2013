from _collections import defaultdict

inputFile = open('input2.txt','r')

inputList = []

for lines in inputFile:
  inputList.append(lines.rstrip())



# take in candiates
#populate dict
candDict = defaultdict(str)

