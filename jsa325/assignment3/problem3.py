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

# def scenarioSolve(current_scenario):
# num_papers = int(current_scenario[0].split()[0])
#  papers_list = current_scenario[1:num_papers+1]
#  authors_to_search = current_scenario[num_papers+1:]

    
#  authors_dictionary = find_all_authors(papers_list)
#  papers_dictionary = find_all_papers(authors_dictionary, papers_list)
    
#  A = create_adjacency_matrix(papers_dictionary)
    
#  erdos_key = -1
#  for key,value in authors_dictionary.items():
#    if value == 'Erdos, P.':
#      erdos_key = key
#  authors_erdos_numbers = {}
    
#  for i in range(1, len(authors_dictionary)+1):
#    count = 0
#      for k in range(1, num_papers + 1):
#        if numpy.linalg.matrix_power(A, k)[i-1, erdos_key - 1] != 0 and count == 0 and erdos_key != -1:
#          count += 1
#          authors_erdos_numbers[authors_dictionary[i]] = k
#        elif k == num_papers and count == 0:
#          authors_erdos_numbers[authors_dictionary[i]] = "infinity"
    
#  authors_erdos_numbers['Erdos, P.'] = 0
    
#  for author in authors_to_search:
#    mark = 0
#    for key in authors_erdos_numbers:
#      if author[:-1] == key or author[:-1]+"." == key:
#        print key + " " + str(authors_erdos_numbers[key])
#        mark += 1
#    if mark == 0:
#      print author[:-1] + " " + "infinity"
            
"""
1. Define a function listScenarios that splices each scenario into two lists: a list of papers 
listPapers, and a list of authors listAuthors. 
"""

def listScenarios(lines):
  
"""
2. Create a dictionary authorsDict with keys = integers 1,...,n (where n is the number 
of authors) and values = authors. This dictionary will call the function findAuthors
on the input listPapers.
3. Define a function findAuthors on the input listPapers.
4. Define a function findPaperAuthors on the input listPapers that will split up the
list of authors.
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
on the input listPaperAuthors and authorsDict. Manually set [Erdos, P: 0].
8. Define a function findErdos on the input listPaperAuthors and authorsDict.
"""

def findErdos(listPaperAuthors, authorsDict):
  erdosDict = {}
  
  for key in authorsDict:
    listErdos = []
