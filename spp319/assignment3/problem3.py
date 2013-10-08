#read in file
lines =  open('input3.txt').readlines()
scenarios = lines[0]

lineTotal = 0
line = 1
scen = int(scenarios)
numPapers = 0
numNames = 0
scenInfo = []
authorsTitle = []
justAuthors = []
eNumDict = {}
papersForAuthorDict = {}
pName = ""
erdosFound = False
relationshipCounter = 0

def numBuilder(erdosNumber):
    pName = 0

    for entries in eNumDict:
        if eNumDict.get(entries) == erdosNumber:

            i = 0
            while i < len(namesInPapers):

                n = 0
                while n < len(namesInPapers[i]):

                    if namesInPapers[i][n].strip() == entries:

                        for items in namesInPapers[i]:
                            if items.strip() != namesInPapers[i][n].strip():
                                if items.strip() != nameErdos:
                                    if eNumDict.get(items.strip()) == "na":

                                        pName = items.strip()
                                        eNumDict[pName] = erdosNumber + 1


                    n = n + 1
                i = i + 1
    return eNumDict

def findErdos(primaryName):
    pName = 0
    i = 0
    while i < len(namesInPapers):
        n = 0
        while n < len(namesInPapers[i]):
            if namesInPapers[i][n].strip() == primaryName:
                eNumDict[namesInPapers[i][n].strip()] = 0
                for items in namesInPapers[i]:
                    if items != namesInPapers[i][n]:
                        pName = items.strip()
                        eNumDict[pName] = int(1)



            n = n + 1
        i = i + 1
    return eNumDict

def buildDict(names):

    i = 0
    empty = []
    papersAIn = []
    while i < len(names):
        n = 0
        while n < len(names[i]):
            eNumDict[names[i][n].strip()] = "na"


            n = n + 1
        i = i + 1
    return eNumDict

def readPapers(self, line):
    myLine = 1
    scenInfo = lines[line].split()
    numPapers = int(scenInfo[0])
    numNames = int(scenInfo[1])
    authorsByPaper = []
    authorsToFind = []
    line = line + 1

    #while there are papers in the scenario, add to list
    while myLine <= numPapers:

        #split line by colon
        authorsTitle = lines[line].split(":")
        #now split authors names by comma
        justAuthors = authorsTitle[0].split(',')
        #now rejoin parts of authors names (add a comma back in)
        justAuthors = [i+","+j for i,j in zip(justAuthors[::2], justAuthors[1::2])]
        authorsByPaper.append(justAuthors)
        #strip of empty space
        #authorsByPaper = [x.strip() for x in authorsByPaper]
        # iter control variables
        line = line + 1
        myLine = myLine + 1

    #print authorsByPaper
    myLine = 1

    #while there are authors in scenario, add to list
    while myLine <= numNames:
        authorsToFind.append(lines[line].strip())
        myLine = myLine + 1
        line = line + 1
    #print authorsToFind
    return authorsByPaper, authorsToFind, line

#this code assumes there are no spaces between cases, instructions did not indicate
while scen > 0:
    x = readPapers(scen, line)
    namesInPapers = x[0]
    namesToRate = x[1]
    nameErdos =  'Erdos, P.'

    eNumDict = buildDict(namesInPapers)

    # i = 0
    # while i < len(namesInPapers):
    #     n = 0
    #     while n < len(namesInPapers[i]):
    #         if namesInPapers[i][n].strip() == nameErdos:
    #             eNumDict[namesInPapers[i][n].strip()] = 0
    #         n = n + 1
    #     i = i + 1

    eNumDict = findErdos(nameErdos)
    relationshipCounter += 1
    justAuthors = eNumDict.keys()
    justAuthors.remove(nameErdos)
    while relationshipCounter < len(eNumDict) and len(justAuthors) > 0:
         eNumDict = numBuilder(relationshipCounter)
         relationshipCounter += 1

    m = 0
    while m < len(namesToRate):
        if eNumDict.get(namesToRate[m]) == "na":
            print "infinity"
        else:
            print eNumDict.get(namesToRate[m])
        m = m + 1
    scen -= 1
    lineTotal = lineTotal + x[2]

    x = []
    namesInPapers = 0
    namesToRate = 0
    eNumDict = {}
    line = lineTotal
    numPapers = 0
    numNames = 0
    scenInfo = []
    authorsTitle = []
    justAuthors = []
    eNumDict = {}
    papersForAuthorDict = {}
    pName = ""
    erdosFound = False
    erdosNumber = 0
    relationshipCounter = 0
    m = 0


    #numBuilder()
    #print eNumDict

    #list of each paper
    #find erdos in lists, and create lists of two
    #every list without erdos but a 1, give 2

