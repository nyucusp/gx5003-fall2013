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
(a list of lists). Define a funciton X that takes a scenario as input and outputs 
the authors and their Erdos numbers. Return a dictionary searchDict with keys = 
authors and values = Erdos numbers.
"""

"""
1. Define a function X that splices each scenario into two lists: a list of papers 
listPapers, and a list of authors listAuthors. 
2. Create a dictionary authorsDict with keys = integers 1,...,n (where n is the number 
of authors) and values = authors. This dictionary will call the function findAuthors
on the input listPapers.
3. Define a function findAuthors on the input listPapers.
4. Create a dictionary papersDict with keys = integers 1,...,n and values = papers.
This dictionary will call the function findPapers on the input authorsDict and 
listPapers.
5. Define a function findPapers on the input authorsDict and listPapers.
6. Create a dictionary erdosDict with keys = authors and values = strings 0,...,infinity
(where the string is an Erdos number). This dictionary will call the function findErdos 
on the input papersDict and authorsDict. NOTE TO SELF: I DON'T KNOW IF THIS IS RIGHT.
Manually set [Erdos, P: 0].
7. Define a function findErdos on the input ?
"""

erdos_key = -1
    for key,value in authorsDict.items():
        if value == 'Erdos, P.':
            erdos_key = key
    authors_erdos_numbers = {}
    
    for i in range(1, len(authorsDict)+1):
        count = 0
        for k in range(1, num_papers + 1):
            if numpy.linalg.matrix_power(A, k)[i-1, erdos_key - 1] != 0 and count == 0 and erdos_key != -1:
                count += 1
                authors_erdos_numbers[authorsDict[i]] = k
            elif k == num_papers and count == 0:
                authors_erdos_numbers[authorsDict[i]] = "infinity"
    
    authors_erdos_numbers['Erdos, P.'] = 0
    
    for author in authors_to_search:
        mark = 0
        for key in authors_erdos_numbers:
            if author[:-1] == key or author[:-1]+"." == key:
                print key + " " + str(authors_erdos_numbers[key])
                mark += 1
        if mark == 0:
            print author[:-1] + " " + "infinity"
