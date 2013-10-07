"""
An implementation of a generic tree to encode Erdos numbers based on input
"""
from _collections import defaultdict
from collections import deque

class Tree(object):
    def __init__(self, name, children=[]):
        self.data = name
        self.children = list(children)

    def add(self, child):
        self.children.append(child)

inputFile = open('input3.txt','r')

inputQue = deque()

for line in inputFile:
    inputQue.append(line.rstrip())

instances = int(inputQue.popleft()) #instances of Erdos calculations

#start while loop for instances

papers, names = inputQue.popleft().split(" ") #split P,N into variables

authorList = [] #generate list of papers
for i in range(0,int(papers)):
    #intern string of paper citation to variable
    paperString = inputQue.popleft()
    #extract author block
    authorBlock = paperString[0:paperString.find(":")]
    authorSplit = authorBlock.replace('.,','.;').split("; ")
    authorList.append(authorSplit)

nameDict = defaultdict(int)
for i in range(0,int(names)):
    nameDict[inputQue.popleft()] = -1

erdosTree = Tree("Erdos, P.")

for line in authorList:
  addChildren(line)

def addChildren(authorLine):
    if authorLine.count('Erdos, P.') > 0: #Erdos present in author list
        for i in authorLine:
            if (i != 'Erdos, P.'): 
                erdosTree.add(Tree(i))
    else: #handle authors removed from Erdos
        #search for match
        for i in range(len(erdosTree.children)): #iterator 
            for authorName in authorLine:
                if authorName == erdosTree.children[i].name:
                    filterLine = filter(lambda x: x!=authorName, authorLine)
                    for childName in filterLine:
                        erdosTree.children[i].add(Tree(childName)) 

def treeToMap(erdosTree):
    #convert the tree to a map of values

#end while loop for instances