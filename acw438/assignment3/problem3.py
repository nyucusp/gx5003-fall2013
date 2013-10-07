#Alex Chohlas-Wood (acw438). Assignment 3, Problem 3.

class Scenario:
    def __init__(self, numPapers, numAuths, scenarioNum):
        self.numPapers = numPapers
        self.numAuths = numAuths
        self.papers = []
        self.authors = {}
        self.authorQ = []
        self.scenarioNum = scenarioNum

    def addPaper(self, paper):
        self.papers.append(Paper(paper))

    def addAuthorQ(self, author):
        self.authorQ.append(author)

    def needMorePapers(self):
        return int(self.numPapers) > len(self.papers)

    def parseAuthors(self):
        for paper in self.papers:
            for author in paper.authorList:
                if author not in self.authors:
                    self.authors[author] = 0

    def addErdosNums(self):
        erdosCounter = 1
        while True:
            foundAnother = False

            #Add erdos numbers to paper authors connected in last iteration:
            for paper in self.papers:
                if paper.erdosNum == erdosCounter:
                    for author in paper.authorList:
                        if self.authors[author] == 0:
                            self.authors[author] = erdosCounter

            #Search for next set of connections:
            for paper in self.papers:
                if paper.erdosNum == 0:
                    for author in paper.authorList:
                        if self.authors[author] != 0:
                            paper.erdosNum = self.authors[author] + 1
                            foundAnother = True

            #If no connections were found on this loop,
            #mark authors as infinity and break
            if not foundAnother:
                for paper in self.papers:
                    if paper.erdosNum == 0:
                        for author in paper.authorList:
                            self.authors[author] = 'infinity'
                break
            erdosCounter += 1


class Paper:
    def __init__(self, paper):
        self.authorList = []
        self.erdosNum = 0

        colonIndex = paper.find(':')
        self.authorList = paper[:colonIndex]
        self.authorList = self.authorList.split('., ')

        #Scope problem here, which required me to refer to original list 
        #when inside if loop.
        #Add periods to author names, find Erdos papers.
        for index, author in enumerate(self.authorList):
            if author[-1] != '.':
                self.authorList[index] += '.'
            if self.authorList[index] == "Erdos, P.":
                 self.erdosNum = 1


rawFile = open('input3.txt', 'r')
input3 = []
for line in rawFile:
    input3.append(line.strip())
rawFile.close()

#Discard number of scenarios:
input3 = input3[1:]

#Split scenarios into Scenario instances:
scenarioList = []
scenarioCounter = 0
for line in input3:
    if not line[0].isdigit():
        scenarioEntry = scenarioList[scenarioCounter-1]
        if scenarioEntry.needMorePapers():
            scenarioEntry.addPaper(line)
        else:
            scenarioEntry.addAuthorQ(line)
    else:
        scenarioCounter += 1
        scenarioList.append(Scenario(line[0], line[1], scenarioCounter))

for item in scenarioList:
    #After all papers have been added, parse authors into dict
    item.parseAuthors()

    #Add Erdos numbers to authors
    item.addErdosNums()

#Run through scenarios,
#Take author query from input and output dict value
for item in scenarioList:
    print 'Scenario', item.scenarioNum
    for author in item.authorQ:
        print author, item.authors[author]
