import sys

inputFile = open('input3.txt', 'r')                       # open .txt file

inputLines = []                                           # save lines in a list
for line in inputFile:
  inputLines.append(line)
inputFile.close()

"""
A scenario is a list containing a pair of integers P N denoting the number of 
papers P and the number of authors N in each scenario, followed by P + N lines. 
Parse the input for integer pairs and splice input into a new list of scenarios
(a list of lists). Define a function that takes a scenario as input and outputs 
the authors and their Erdos numbers. Return a dictionary searchDict with keys = 
authors and values = Erdos numbers.
"""

listScenarios = []
newScenario = [1]
numScenarios = int(inputLines[0])
new = 1

for i in range(1, numScenarios):
    new += int(inputLines[marker].split()[0])+int(inputLines[new].split()[1])+1
    newScenario.append(marker)

newScenario.append(len(inputLines))

for k in range(0,len(newScenario)-1):
    listScenarios.append(inputLines[newScenario[k]:newScenario[k+1]])
    
"""
1. Create a list of lists listScenarios that splices each scenario into two lists: a list of papers 
listPapers, and a list of authors listAuthors. 
"""

def solveErdos(currentScenario):
  numPapers = int(currentScenario[0].split()[0])
  papersList = currentScenario[1:numPapers+1]
  
  searchAuthors = currentScenario[numPapers+1:]
  
  authorsDict = findAuthors(listPapers)
  papersDict = findPapers(authorsDict, listPapers)
  
  keyErdos = -1
  for key,value in authorsDict.items():
    if value == 'Erdos, P.':
      keyErdos = key
  erdosDict = {}
    
  for i in range(1, len(authorsDict)+1):
    count = 0
    for k in range(1, numPapers + 1):
      if [i-1, keyErdos - 1] != 0 and count == 0 and keyErdos != -1:
        count += 1
        erdosDict[authorsDict[i]] = k
      elif k == numPapers and count == 0:
        erdosDict[authorsDict[i]] = "infinity"
    
  erdosDict['Erdos, P.'] = 0
    
  for author in searchAuthors:
    mark = 0
    for key in erdosDict:
      if author[:-1] == key or author[:-1]+"." == key:
        print key + " " + str(erdosDict[key])
        mark += 1
      if mark == 0:
        print author[:-1] + " " + "infinity"
  
"""
2. Create a dictionary authorsDict with keys = integers 1,...,n (where n is the number 
of authors) and values = authors. This dictionary will call the function findAuthors
on the input listPapers.
3. Define a function findAuthors on the input listPapers.
4. Define a function findPaperAuthors on the input listPapers that will split up the
list of authors for each paper.
"""

def findAuthors(papers):
  authorsDict = {}
  authors = set()
    
  for line in papers:        
    listAuthors = find_authors(line)
      for elt in listAuthors:
        authors.add(elt)    
    
  tempList = []
  for author in authors:
    tempList.append(author)
    
  for i in range(0, len(tempList)):
    authorsDict[i+1] = tempList[i]
    
  return authorsDict

def findPaperAuthors(paper):
  parseAuthorsList = paper.split(':', 1)[0]
  splitList = parseAuthorsList.split(',')
  listPaperAuthors = []
  for i in range(0, len(splitList)/2):
    listPaperAuthors.append((splitList[2*i] + "," + splitList[2*i + 1]).lstrip())
    
  return listPaperAuthors

"""
5. Create a dictionary papersDict with keys = integers 1,...,n and values = papers.
This dictionary will call the function findPapers on the input authorsDict and 
listPapers.
6. Define a function findPapers on the input authorsDict and listPapers.
"""

def findPapers(authorsDict, papers):
  papersDict = {}
  
  for key in authorsDict:
    listPapers = []
    for paper in papers:
      if paper.find(authorsDict[key]) != -1:
        listPapers.append(paper.ssplit(':')[1].lstrip())
    papersDict[key] = papersList
    
  return papersDict

"""
7. Create a dictionary erdosDict with keys = authors and values = strings 0,...,infinity
(where the string is an Erdos number). This dictionary will call the function findErdos 
on the input searchAuthors and authorsDict. Manually set [Erdos, P: 0].
8. Define a function findErdos on the input searchAuthors and authorsDict.
"""

def findErdos(searchAuthors, authorsDict):
  erdosDict = {}
  
  for key in authorsDict:
    listErdos = []
