import sys

inputFile = open("input3.txt", "r")

"""
A scenario is a list containing a pair of integers P N denoting the number of 
papers P and the number of authors N in each scenario, followed by P + N lines. 
Parse the input for integer pairs and splice input into a new list of scenarios
(a list of lists). Define a function that takes a scenario as input and outputs 
the authors and their Erdos numbers.
"""

numScenarios = int(inputFile.readline())

for n in range (0, numScenarios):
  PN = inputFile.readline().split()
  P = int(PN[0]
  N = int(PN[1]
  
  papers = []
  for i in range(0, P):
    papers.append(inputFile.readline())
    
"""
Create dictionary of all authors.
"""
    
  authorDict = {}
  authorList = []
  for line in papers:
    newline = line.split('.:')
    for entry in newline:
      lines = entry.split('., ')
      if (lines[0][0] != ' '):
        authorList.append(lines)
        for i in range(0, len(lines)):
          newAuthor = lines[i]
          authorDict[newAuthor] = 1000000           # set 1000000 as temporary Erdos number placeholder
          
"""
Create list of authors for whom we want to find Erdos numbers.
"""
  
  authors = []
  for i in range(0, N):
    name = inputFile.readline().strip('\n')
    authors.append(name)
    
  for line in authorList:
    if 'Erdos, P' in line:                          # if Erdos is one of the authors
      for i in range(0, len(line)):
        authorName = line[i]
        authorDict[authorName] = 1                  # set Erdos number to 1 for other paper authors
  
  for j in range(0, P):
    for line in authorList:
      minErdos = authorDict[line[0]]
      for i in range(0, len(line)):
        if (authorDict[line[i]] < minErdos):
          minErdos = authorDict[line[i]]
      for i in range(0, len(line)):
        if (authorDict[line[i]] > minErdos):
          authorDict[line[i]] = minErdos + 1        # add 1 to Erdos number of authors on paper
          
"""
For authors with no Erdos number, ie. with no "paper trail" that leads to
Erdos, loop.
"""
  
  for entry in authorDict:
    if (authorDict[entry] == 1000000):
      authorDict[entry] = 'infinity'
  
  print 'Scenario ', n + 1
  for name in authors:
    for entry in authorDict:
      if (str(entry) == str(name)):
        print entry, ". ", authorDict[entry]

inputFile.close()
