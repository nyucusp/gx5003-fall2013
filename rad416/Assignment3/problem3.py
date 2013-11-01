"""
An implementation of a generic tree to encode Erdos numbers based on input
"""
from _collections import defaultdict
from collections import deque

class Tree(object):
    def __init__(self, name, children=[]):
        self.name = name
        self.children = list(children)

    def add(self, child):
        self.children.append(child)

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

def treeToMap():
    authNumberDict = defaultdict(int)
    for i in range(len(erdosTree.children)):
        authNumberDict[erdosTree.children[i].name] = 1
        if erdosTree.children[i].children:
            for j in range(len(erdosTree.children[i].children)):
                authNumberDict[erdosTree.children[i].children[j].name] = 2
    return authNumberDict

inputFile = open('input3.txt','r')

inputQue = deque()

for line in inputFile:
    inputQue.append(line.rstrip())

instances = int(inputQue.popleft()) #instances of Erdos calculations

#start while loop for instances
instanceCounter = 1
while instanceCounter <= instances:
    papers, names = inputQue.popleft().split(" ") #split P,N into variables

    papers = int(papers)
    names = int(names)

    authorList = [] #generate list of papers
    for i in range(0,papers):
        #intern string of paper citation to variable
        paperString = inputQue.popleft()
        #extract author block
        authorBlock = paperString[0:paperString.find(":")]
        authorSplit = authorBlock.replace('.,','.;').split("; ")
        authorList.append(authorSplit)

    namesList = []
    for i in range(0,names):
        namesList.append(inputQue.popleft())

    erdosTree = Tree("Erdos, P.")

    for line in authorList:
      addChildren(line)

    authNumberDict = treeToMap()

    print "Scenerio " + str(instances)

    for name in namesList:
        if name in authNumberDict:
            print name, authNumberDict[name]
        else:
            print name, "infinity"

    instanceCounter += 1
#end while loop for instances