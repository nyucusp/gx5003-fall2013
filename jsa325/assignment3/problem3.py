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
(a list of lists). Define a funciton searchAuthors that takes a scenario as input 
and outputs the authors and their Erdos numbers. Return a dictionary searchDict 
with keys = authors and values = Erdos numbers.
"""

"""
1. Define a function listScenarios that splices each scenario into two lists: a 
list of papers listPapers, and a list of authors listAuthors. 
2. Create a dictionary authorsDict with keys = integers 1,...,n (where n is the 
number of authors) and values = authors. This dictionary will call the function 
findAuthors on the input listPapers.
3. Define a function findAuthors on the input listPapers that returns a list of 
unique authors.
4. Create a dictionary papersDict with keys = integers 1,...,n and values = papers.
This dictionary will call the function findPapers on the input authorsDict and 
listPapers.
5. Define a function findPapers on the input authorsDict and listPapers that returns
a list of papers associated with each author in authorsDict.
6. Define a function findErdos on the input authorsDict and listPapers that returns 
a list of all papers associated with 'Erdos, P.' REDUNDANT; FIX
6. Create a dictionary erdosDict with keys = authors and values = 0,...,infinity 
(where the string is an Erdos number). This dictionary will call the  function 
findErdos on the input papersDict and authorsDict. Manually set [Erdos, P: 0].
...
"""
