"""
A script to take in a series of candidates and ballots and perform instant run-off voting.
"""

from _collections import defaultdict
from collections import deque

def ballotCounter(ballotList):
    ballotDict = defaultdict(int)
    for i in ballotList:
        ballotDict[i[0]] += 1
    return ballotDict

# check for majority winner
def calcWinner(ballotDict): 
    ballotSum = 0
    for k in ballotDict:
        ballotSum += ballotDict[k]

    for k in ballotDict:
        if (float(ballotDict[k]) / float(ballotSum) > 0.5):
            return k
        else:
            return -1

def genLoserList():
    minVotes = min(ballotDict.values())
    loserList = []
    for k,v in ballotDict.iteritems():
        if v == minVotes:
            loserList.append(k)
    return loserList

inputFile = open('input2.txt','r')

inputQue = deque()

for lines in inputFile:
    inputQue.append(lines.rstrip())

caseInt = int( inputQue.popleft() ) #number of cases

caseCounter = 1 #counter to control iterations of ballot runs   
while ( caseCounter <= caseInt):

    inputQue.popleft() #blank linespace removal

    candidateDict = defaultdict(str) #dict for candidates

    candidatesNum = int(inputQue.popleft()) #number of candidates

    #populate dict with candidates
    #key is int, value is name string
    for i in range(1,candidatesNum+1):
        candidateDict[i] = ( inputQue.popleft() )

    #find break point
    breakPoint = 0
    for i in range(len(inputQue)):
        if inputQue[i] == '':
            breakPoint = i
    if breakPoint == 0:
        breakPoint = len(inputQue)

    ballotList = [] #list of deques containing ballots

    # populate list with list of ballots in selection order
    for i in range(breakPoint):
        ballotList.append( inputQue.popleft().split(" ") )

    # generate dict key on candidate number and value number votes
    ballotDict = ballotCounter(ballotList)

    #check for majority winner in first round
    winnerCheck = calcWinner(ballotDict) 

    while (winnerCheck == -1 and len(ballotDict) > 2): #loop until find majority winner or tie between two
        #loser check
        loserList = genLoserList()
        for i in range(len(ballotList)):
            for loser in loserList: 
                ballotList[i] = filter(lambda x : x != loser, ballotList[i]) #filter loser(s) from ballotList

        #recalc ballotDict
        ballotDict = ballotCounter(ballotList)

        #check again for winner
        winnerCheck = calcWinner(ballotDict)

    if winnerCheck != -1:
        print candidateDict[int(winnerCheck)]
    else:
        for k in ballotDict:
            print candidateDict[int(k)]
    print "\n"
    caseCounter += 1 #increment the control counter


