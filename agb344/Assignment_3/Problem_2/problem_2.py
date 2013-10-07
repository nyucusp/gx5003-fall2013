import sys
def getFirst(list):
    if len(list)>0:
        return list[0]
    else:
        return 0

inputFile = open('input2.txt','r')
inputFile.seek(0)

numScenarios = int(inputFile.readline()[:-1])
#print numScenarios
inputFile.readline()
scenarios = inputFile.read()
scenarioList = [x.split('\n') for x in scenarios.split('\n\n')]
#print scenarioList
haveWinner = False
winningCandidate = ''
ballots = []
ballotsList = []
scenarioCount = 0
for scenario in scenarioList:
    haveWinner = False
    winningCandidate = ''
    #print scenarioCount
    scenarioCount += 1
    #while not(haveWinner):
    for empty in range(0, scenario.count('')):
        scenario.remove('')
    numCandidates = int(scenario[0])
    #print numCandidates
    candidates = scenario[1:numCandidates+1]
    ballots = scenario[numCandidates+1:]
    #print ballots
    ballotsList = [map(int, x.split(' ')) for x in ballots]
    eliminated = []
    #voteBase = [0 for i in range(1, numCandidates+1)]
    while not(haveWinner):
        voteCount = [([0]*(numCandidates)) for i in range(1, numCandidates+1)]
    #print candidates
        #print 'ballots'
        #print ballots
        #print 'ballotsList'
        #print ballotsList
    #print voteBase
    #print voteCount
        for ballot in ballotsList:
        #print ballot        
            for preference, vote in enumerate(ballot):
            #print preference, vote
                if preference not in eliminated:
                    voteCount[vote-1][preference]+=1
            #print voteCount

        fiftyPercent = len(ballotsList)/2.0
        #print fiftyPercent
        firstPlaceCount = map(getFirst, voteCount)
        passToNext = []
        minVotes = min(firstPlaceCount)
        #print firstPlaceCount
        if firstPlaceCount[1:] == firstPlaceCount[:-1]: #all candidates tied for first place
            passToNext = [i for i in range(0, len(firstPlaceCount))]
        else:
            for candidate, place in enumerate(firstPlaceCount):
                if place >= fiftyPercent or place != minVotes:
                    passToNext.append(candidate)
                if place == minVotes:
                    eliminated.append(candidate)
        
        
        #print 'first:'
        #print firstPlaceCount
        #print fiftyPercent
        #print 'pass:'
        #print passToNext
        #print eliminated
        #print voteCount
        #print 'pass'
        #print passToNext
        if len(passToNext) == 1:
            haveWinner = True
            winningCandidate = candidates[passToNext[0]]
        #elif not any((firstPlaceCount[i] != firstPlaceCount[i+1] for i in range(0, len(firstPlaceCount)-1))):
        elif firstPlaceCount.count(max(firstPlaceCount)) == len(passToNext):
            haveWinner = True
            for i in passToNext:
                winningCandidate += candidates[i]+'\n'
        else:
            tempBallot = []
            for ballot in ballotsList:
                #print ballot
                if ballot[0]-1 in eliminated:
                    #print ballot
                    tempBallot+=[ballot[1:]]
                    #print tempBallot
            ballotsList = tempBallot
            #print ballotsList
            

#print haveWinner
    if haveWinner:
        print winningCandidate
