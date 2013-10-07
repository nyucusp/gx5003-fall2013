#Alex Chohlas-Wood (acw438). Assignment 3, Problem 4.

'''
1

8 11
abcDEFGhigg
hEbkWalDork
FtyAwaldORm
FtsimrLqsrc
byoArBeDeyv
Klcbqwikomk
strEBGadhrb
yUiqlxcnBjf
4
Waldorf
Bambi
Betty
Dagbert
'''

import copy

class Scenario:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)
        self.wordCount = 0
        self.wordList = []
        self.grid = []
        self.locations = {}

    def gridComplete(self):
        return self.height == len(self.grid)

    def wordListComplete(self):
        return self.wordCount == len(self.wordList)

    def everythingToLower(self):
        for index,word in enumerate(self.wordList):
            self.wordList[index] = word.lower()
        for index,line in enumerate(self.grid):
            self.grid[index] = line.lower()

def addStep(cursor, xStep, yStep):
    newCursor = cursor
    newCursor[0] += xStep
    newCursor[1] += yStep
    return newCursor

rawFile = open('input4.txt', 'r')
input4 = []
for line in rawFile:
    input4.append(line.strip())

#Get rid of number of scenarios:
input4 = input4[2:]

#Make list of grid, queried words:
inGrid = True
addLine = False
scenarioList = []
for line in input4:
    if inGrid:
        if not line == '':
            if addLine:
                currentScenario.grid.append(line)
                if currentScenario.gridComplete():
                    inGrid = False
                    addLine = False
            else:
                dimsList = line.split(' ')
                scenarioList.append(Scenario(dimsList[0], dimsList[1]))
                currentScenario = scenarioList[-1]
                addLine = True
    else:
        if addLine:
            currentScenario.wordList.append(line)
            if currentScenario.wordListComplete():
                inGrid = True
                addLine = False
        else:
            currentScenario.wordCount = int(line[0])
            addLine = True
        


for scenario in scenarioList:
    #Convert everything to lowercase letters:
    scenario.everythingToLower()
    thisGrid = scenario.grid
    for word in scenario.wordList:

        #Take first letter of word:
        firstLetter = word[0]

        #Make list of first letter hits in grid (initialHits):
        initialHits = []
        for yIndex, line in enumerate(thisGrid):
            for xIndex, letter in enumerate(line):
                if letter == firstLetter:
                    initialHits.append([xIndex, yIndex])

        #For entries in initialHits, explore around for matching 2nd letter
        for hit in initialHits:
            neighborhood = [[x,y] 
                            for y in range(hit[1]-1, hit[1]+2) 
                            for x in range(hit[0]-1, hit[0]+2) 
                            if not ((x==hit[0] and y==hit[1]) or x<0 or y<0 
                            or x>=scenario.width or y>=scenario.height)]
            
            #Store leads in list (hitLeads)
            anyGoodNeighbors = False
            goodNeighbors = []
            for neighbor in neighborhood:
                xCoord = neighbor[0]
                yCoord = neighbor[1]
                if thisGrid[yCoord][xCoord] == word[1]:
                    goodNeighbors.append(neighbor)
                    anyGoodNeighbors = True

            #For hits with neighboring leads, follow direction 
            #(diff btwn hit & lead) iterating through word
            if anyGoodNeighbors:
                for goodNeighbor in goodNeighbors:
                    if word not in scenario.locations:
                        counter = 2
                        wordLength = len(word)
                        xStep = goodNeighbor[0]-hit[0]
                        yStep = goodNeighbor[1]-hit[1]
                        cursor = copy.copy(goodNeighbor)
                        while counter < wordLength:
                            cursor = addStep(cursor, xStep, yStep)
                            try:
                                cursorLetter = thisGrid[cursor[1]][cursor[0]]
                                if word[counter] == cursorLetter:
                                    counter += 1
                                    if counter == wordLength:
                                        scenario.locations[word]=(str(hit[1]+1) 
                                                                  + " " + 
                                                                  str(hit[0]+1))
                                        break

                                #If find non-matching letter:
                                else:
                                    break

                            #If cursor moves off grid:
                            except:
                                break

    for key,value in scenario.locations.iteritems():
        print value
    print ''
               

#If get to end of word, put initialHit in outputList

#print outputList
# for line in scenarioList:            
#     print line.grid, line.wordList
