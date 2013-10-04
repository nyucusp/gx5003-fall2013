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

    def addErdosOnes(self):
        for paper in self.papers:
            if paper.isErdos:
                for author in paper.authorList:
                    self.authors[author] = 1

class Paper:
    def __init__(self, paper):
        self.authorList = []
        self.isErdos = False
        colonIndex = paper.find(':')
        self.authorList = paper[:colonIndex]
        self.authorList = self.authorList.split('., ')
        #Scope problem here, which required me to refer to original list 
        #in if loop
        for index, author in enumerate(self.authorList):
            if author[-1] != '.':
                self.authorList[index] += '.'
            if self.authorList[index] == "Erdos, P.":
                self.isErdos = True


rawFile = open('input3.txt', 'r')
input3 = []
for line in rawFile:
    input3.append(line.strip())

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
    item.parseAuthors()
    item.addErdosOnes()
#    item.calcOtherErdos()

for item in scenarioList:
    print 'Scenario', item.scenarioNum
#    for paper in item.papers:
#        print paper.isErdos
    print item.authors
    print ''

#Have a list of Paper objects.
#Have a dict of names, values = -1.
#Get the names of people with Erdos#1, change value in dict to 1.
#Mark Erdos papers as "recorded"
#Go through remaining papers. If find paper with author with Erdos # != -1:
 #Make other authors that author's number + 1
 #Mark paper as "recorded"
#If program has cycled through all remaining papers and none have been marked as recorded, mark those authors as "infinity"

#Take author query from input, run through dict and output dict value
