from _collections import defaultdict
from collections import deque

def ballotCounter(ballotList):
    ballotDict = defaultdict(int)
    for i in ballotList:
        ballotDict[i[0]] += 1
    return ballotDict

# check for majority winner
def calcWinner(ballotList): 
    ballotSum = 0
    for i in range(len(ballotList)):
        ballotSum += ballotDict[k]

    for k in ballotDict:
        if (float(ballotDict[k]) / float(ballotSum) > 0.5):
            return k
        else:
            return -1

def genLoserList(ballotDict):
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

# loopCounter = 1 #counter to control iterations of ballot runs   
# while (i <= caseInt):

inputQue.popleft() #blank linespace removal

candidateDict = defaultdict(str) #dict for candidates

candidatesNum = int(inputQue.popleft()) #number of candidates

#populate dict with candidates
#key is int, value is name string
for i in range(1,candidatesNum+1):
    candidateDict[i] = ( inputQue.popleft() )

ballotList = [] #list of deques containing ballots

# populate list with deques of ballots
for i in range(len(inputQue)):
    ballotList.append( deque(inputQue[i].split(" ")) )

# generate dict key on candidate number and value number votes
ballotDict = ballotCounter(ballotList)

#check for majority winner in first round
winnerCheck = calcWinner(ballotDict) 

while (winnerCheck == -1): #loop until find majority winner
    #loser check
    
    loserList = genLoserList()
    for i in range(len(ballotList)):
        for loser in loserList:
            print filter(lambda x : x != loser, ballotList[i])

    #filter loser(s) from ballotList

    #recalc ballotDict
    ballotDict = ballotCounter(ballotList)





    # condition = True
    # while condition:
    #     loserKey.append(min(ballotDict, key=ballotDict.get)) #find min
        

    #     #test for other min in dict, if not, break list
    #     if ( returnValCount(ballotList,minVotes) > 1 ):
    #         #pop item from dict
    #     else:  
    #         condition = False #break while loop
        
    #filter loser

    #check again for winner
    winnerCheck = calcWinner(ballotList)
  


print candidateDict[int(winnerCheck)]
  # loopCounter += 1 #incrememt the control counter

# transform ballotList into dictionary keyed on candidate number
