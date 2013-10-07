import sys

inputFile = open('input4.txt', 'r')                       # open .txt file

inputLines = []                                           # save lines in a list
for line in inputFile:
  inputLines.append(line)
inputFile.close()

"""
Parse through inputLines and save each case in a list caseList. Each case 
starts with two integers that denote the dimensions n x m of the grid, followed 
by the grid, followed by an integer that denotes the number of search words, 
followed by the search words. This is similar to the structure of problem2.py.
"""

caseList = []
newLine=[]
for i in range(1,len(inputLines)):
  if inputLines[i] == '\n':
    newLine.append(i)
newLine.append(len(inputLines))
 
for k in range(0,len(newLine)-1):
  caseList.append(inputLines[newLine[k]+1:newLine[k+1]])
  
"""
Define a function searchWords that takes each case as input and outputs the starting
location of each search word as a pair of integers. Create a n x m grid, where n is the
first integer of the input and m is the second integer of the input. Create a dictionary
with keys = coordinates (ie. a pair of integers) and values = letters at those coordinates
in the grid. For a search word, make a list of those keys that have as values the 
first letter. Update the list of keys to include only those keys that are adjacent to keys
that have as values the second letter. At this point, the possible starting locations and
the possible directions will have been sorted out. Follow the possible directions until
the full word is found, or until the next key does not contain the next letter. In the
former case, return the original key. In the latter case, eliminate the key from the list
and keep iterate with the other possible keys and directions until the word is found. NOTE
TO SELF: Can I make it such that if there is only 1 key in the list it will just print?
"""

def searchWords(currentCase):
  n = int(currentCase[0].split()[0])                  # n = first integer in the input (number of rows)
  m = int(currentCase[0].split()[1])                  # m = second integer in the input (number of columns)
  gridSize = [n, m]                                   # set the size of the grid to n x m
