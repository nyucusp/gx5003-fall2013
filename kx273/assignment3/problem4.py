
def find_location(string,matrix): # find the location of keyword 
    location=[float("inf"),float("inf")]
    lineNum=len(matrix)
    colNum=len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].lower()==string[0].lower():
                lStr=string[0].lower()
                rStr=string[0].lower()
                uStr=string[0].lower()
                dStr=string[0].lower()
                ulStr=string[0].lower()
                urStr=string[0].lower()
                dlStr=string[0].lower()
                drStr=string[0].lower()

                for n in range (1,len(string)): #get the string in eight horizontal, vertical and diagonal directions through the matrix
                    
                    if i in range(lineNum) and j-n in range(colNum):
                        lStr+=matrix[i][j-n]

                    if i in range(lineNum) and j+n in range(colNum):                    
                        rStr+=matrix[i][j+n]

                    if i-n in range(lineNum) and j in range(colNum):
                        uStr+=matrix[i-n][j]

                    if i+n in range(lineNum) and j in range(colNum):
                        dStr+=matrix[i+n][j]

                    if i-n in range(lineNum) and j-n in range(colNum):
                        ulStr+=matrix[i-n][j-n]

                    if i-n in range(lineNum) and j+n in range(colNum):
                        urStr+=matrix[i-n][j+n]

                    if i+n in range(lineNum) and j-n in range(colNum):
                        dlStr+=matrix[i+n][j-n]

                    if i+n in range(lineNum) and j+n in range(colNum):
                        drStr+=matrix[i+n][j+n]


                if lStr.lower()==string.lower() or rStr.lower()==string.lower() or uStr.lower()==string.lower() or dStr.lower()==string.lower() or ulStr.lower()==string.lower() or urStr.lower()==string.lower() or dlStr.lower()==string.lower() or drStr.lower()==string.lower():
                    location[0]=i+1
                    location[1]=j+1
                    return location
    return location
    
   

myFile=open("input4.txt","r") #open the input file
myInput=[]
index=0

for line in myFile: # read the file
    myInput.append(line.strip())
myFile.close()

while index<len(myInput):

    scenarioNum=int(myInput[index])
    lineNum=int(myInput[index+2].split(" ")[0])
    columnNum=int(myInput[index+2].split(" ")[1])
    checkNum=int(myInput[index+lineNum+3])

    matrix=[]
    for i in range(index+3,index+3+lineNum):
        matrix.append(myInput[i])
             
    for i in range(index+4+lineNum, index+4+lineNum+checkNum):
        location=find_location(myInput[i],matrix) #get the locations 
        print(str(location[0])+" "+str(location[1]))

    print ('')
    index=index+lineNum+checkNum+5 #move to the next scenario


"""
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
"""
