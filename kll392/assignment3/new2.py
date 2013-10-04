import sys
import string

myFile = open("input2.txt", "r")
n = int(myFile.readline())
myFile.readline()

nCand = int(myFile.readline())
N = nCand

class Candidate():
    totalvotes = None
    votelist = []
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.totalvotes = 0
        self.isElim = False
    def addvote(self):
        self.totalvotes += 1

def isMajority(candidateList, nVotesCast):
    for entry in candidateList:
        if (entry.totalvotes > nVotesCast/2):
            return entry.name
    return 0

def minCand(candidateList):
    minVotes = 1000
    losers = []
    for entry in candidateList:
        if (entry.totalvotes < minVotes):
            minVotes = entry.totalvotes
    for entry in candidateList:
        if (entry.totalvotes == minVotes):
            losers.append(entry)
    for entry in candidateList:
        if entry in losers:
            entry.isElim = True
    return minVotes

def isTie(candidateList):
    vote = candidateList[0].totalvotes
    for person in candidateList:
        newvote = person.totalvotes
        if (newvote != vote):
            return False
    return True

candidates = []
isWinner = False
#Create list of candidates:
count = 0
while count < nCand:
    count += 1
    line = myFile.readline().strip('\n')
    tempperson = Candidate(line, count)
    candidates.append(tempperson)

#First round of votes:
votearray = []
nBallots = 0
for line in myFile:
    votearray.append(line.strip('\n'))
    nBallots += 1
for line in votearray:
    vote = int(line[0])
    j = 0
    for item in candidates:
        if (int(candidates[j].index) == vote):
            candidates[j].addvote()
        j += 1

#If a candidate has >50% of votes, he or she automatically wins:
if (isMajority(candidates, nBallots) != 0):
    print isMajority(candidates, nBallots)
    isWinner = True

if (isTie(candidates) == True):
    for person in candidates:
        print person.name
    isWinner = True

print 'vote array is ', votearray

#If there is no winner after the first round: enter loop until winner is picked:

while isWinner is False:
    
    minvotes = 1000
    minvoteentry = []

    for entry in candidates:
        print entry.name, entry.totalvotes

    #find minimum number of votes, remove candidates who tied for last
    losers = []
    minVotes = minCand(candidates)
    i = 0
    while i < 20:
        if (candidates[i].isElim == True):
            print candidates[i].name, ' has been eliminated'
            entry = candidates[i]
            losers.append(entry.index)
            candidates.remove(entry)
            nCand -= 1
        else:
            i += 1
        if (i == nCand):
            break
    
    print 'Remaining Candidates:'
    for entry in candidates:
        print entry.name, entry.index

    print losers

    #Replace votes for eliminated candidates with zeros:
    for entry in losers:
        loserindex = str(entry)
        i = 0
        for ballot in votearray:
            ballot = string.replace(ballot, loserindex, '0')
            votearray[i] = ballot
            i += 1
    print 'The new vote array is: '
    for ballot in votearray:
        print ballot

    for item in candidates:
        item.totalvotes = 0

    for ballot in votearray:
        for i in range (0, (2*N - 1),2):
            vote = ballot[i]
            if (vote != '0'):
                j = 0
                for item in candidates:
                    if (int(candidates[j].index) == int(vote)):
                        candidates[j].addvote()
                    j += 1
                break
            elif (vote == '0'):
                continue

    if (isMajority(candidates, nBallots) != 0):
        print 'We have a winner!'
        print isMajority(candidates, nBallots)
        isWinner = True
    
    if (isTie(candidates) == True):
        for person in candidates:
            print person.name
        isWinner = True


