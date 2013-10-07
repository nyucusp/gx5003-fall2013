from _collections import defaultdict
from collections import deque

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

numVoters = len(ballotList)

# generate dict key on candidate number and value number votes
ballotDict = ballotCounter(ballotList)

#check for majority winner in first round
winnerCheck = calcWinner(ballotList) 

while (winnerCheck == -1): #loop until find majority winner
    #loser check
    minVotes = min(ballotList.values())
    loserList = []

    condition = True
    while condition:
        loserKey.append(min(ballotDict, key=ballotDict.get)) #find min
        

        #test for other min in dict, if not, break list
        if ( returnValCount(ballotList,minVotes) > 1 ):
            #pop item from dict
        else:  
            condition = False #break while loop
        
    #filter loser

    #check again for winner
    winnerCheck = calcWinner(ballotList)
  


print candidateDict[winnerCheck]
  # loopCounter += 1 #incrememt the control counter

# transform ballotList into dictionary keyed on candidate number
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
        if (ballotDict[k] / ballotSum > 0.5):
            return k
        else:
            return -1

#check for loser or loser tie
def calcLoser(ballotDict):
    ballotSum = 0
    for k in ballotDict:
        ballotSum += ballotDict[k]

    for k in ballotDict:

def returnValCount(dictionary, value):
    return ballotDict.values().count(value)

def loserList(ballotDict):
  #find min
  #find count of min
  #iterate through dict and return key for losers in list