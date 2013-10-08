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

        tempPaperList2 = []
        for paper in tempPaperList:
            tempPaper = paper.split(',')
            tempPaper2 = [i+j for i,j in zip(tempPaper[::2],tempPaper[1::2])]
            tempPaperList2.append([x.strip() for x in tempPaper2])

        self.authorList = [a.replace(',','') for a in self.authorList]
        self.paperList = tempPaperList2


    def makePaperTree(self, papers, maxIter):
        #print self.authorList
        if len(papers) > 0 and maxIter>0:
            newPapers = []
            for erdosNumber in self.authorTree.keys():
                for paper in papers:
                    #print paper
                    #print [a for a in paper if a in self.authorList]
                    #if len([a for a in paper if a in self.authorList]) > 0:
                    intersection = [val for val in self.authorTree[erdosNumber] if val in paper]
                    if len(intersection) > 0:
                        if erdosNumber+1 in self.authorTree.keys():
                            self.authorTree[erdosNumber+1] += list(set(paper) - set(intersection))
                        else:
                            self.authorTree[erdosNumber+1] = list(set(paper) - set(intersection))
                    else:
                        newPapers.append(paper)

            #print self.authorTree
            self.makePaperTree(newPapers, maxIter-1)
            
    def printErdosNumbers(self):
        authorDict = {}
        for author in self.authorList:
            authorDict[author] = -1
        for author in self.authorList:
            #print author
            for erdosNumber, erdosAuthors in self.authorTree.iteritems():
                if author in erdosAuthors and authorDict[author] == -1:
                    authorDict[author] = erdosNumber
        for author in authorDict.keys():
            if authorDict[author] != -1:
                print author +' %i'%authorDict[author]
            else:
                print author + ' infinity'

inputFile = open('input3.txt','r')
inputFile.seek(0)
numScenarios = int(inputFile.readline()[:-1])
scenarios = []

for i in range(0, numScenarios):
    nextLine = inputFile.readline()
    numPapers = int(nextLine.split(' ')[0])
    numAuthors = int(nextLine.split(' ')[1])

    authorList = []
    paperList = []

    for paper in range(0, numPapers):
        thisPaper = inputFile.readline()[:-1]
        paperList.append(thisPaper)

    for author in range(0, numAuthors):
        thisAuthor = inputFile.readline()[:-1]
        authorList.append(thisAuthor)

    scenarios.append(Scenario(authorList, paperList))

numScen = 1

for scenario in scenarios:
    print 'Scenario %i' %numScen
    numScen += 1
    scenario.cleanPaperList()
    scenario.makePaperTree(scenario.paperList, len(scenario.authorList)-1)
    scenario.printErdosNumbers()
