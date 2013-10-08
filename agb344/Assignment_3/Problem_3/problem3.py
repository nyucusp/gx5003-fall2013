import sys


class Scenario:
    firstLine = None
    lastLine = None
    authorList = None
    paperList = None
    authorTree = None

    def __init__(self, authors, papers):
        self.authorList = authors
        self.paperList = papers
        self.authorTree = {0:['Erdos P.']}

    def cleanPaperList(self):
        tempPaperList = []
        for paper in self.paperList:
            paperAuthors = paper.split(':')[0]
            tempPaperList.append(paperAuthors)
            #print paperAuthors

        tempPaperList2 = []
        for paper in tempPaperList:
            tempPaper = paper.split(',')
            tempPaper2 = [i+j for i,j in zip(tempPaper[::2],tempPaper[1::2])]
            tempPaperList2.append([x.strip() for x in tempPaper2])
            #print tempPaper2
        self.paperList = tempPaperList2#[x.strip() for x in tempPaperList2]
        #print self.paperList


    def makePaperTree(self):
        #print 'papers'
        for erdosNumber in self.authorTree.keys():
            #print erdosNumber
            for paper in self.paperList:
                print paper
                print self.authorTree[erdosNumber]
                intersection = [val for val in self.authorTree[erdosNumber] if val in self.paperList]
                print intersection

inputFile = open('input3.txt','r')
inputFile.seek(0)
numScenarios = int(inputFile.readline()[:-1])
scenarios = []

for i in range(0, numScenarios):
    nextLine = inputFile.readline()
    numPapers = int(nextLine.split(' ')[0])
    numAuthors = int(nextLine.split(' ')[1])
    #print numPapers
    #print numAuthors

    authorList = []
    paperList = []

    for paper in range(0, numPapers):
        thisPaper = inputFile.readline()[:-1]
        paperList.append(thisPaper)
    
    #print paperList

    for author in range(0, numAuthors):
        thisAuthor = inputFile.readline()[:-1]
        authorList.append(thisAuthor)
    
    #print authorList

    scenarios.append(Scenario(authorList, paperList))
    #nextLine = 
    #print i


#print scenarios

for scenario in scenarios:
    scenario.cleanPaperList()
    #print scenario.paperList
    #print scenario.authorList
    scenario.makePaperTree()
