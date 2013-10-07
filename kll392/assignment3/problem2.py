#Kara Leary
#Urban Informatics
#Assignment 3 -Problem 2

#My code currently only handles inputs that hold one case. I hope to have enough time to update it to accept multiple cases.  For this problem I created a class Candidate that has a name, index, totalvotes, and isElim values.  The name stores the candidate's name, the index value stores the number that corresponds to the candidate (i.e. John Doe would be 1, Jane Smith is 2, Jane Austen is 3 in the sample input).  isElim stores true or false based on whether or not the candidate has been eliminated.  I also defined the functions isMajority, minCand and isTie to determine if a candidate has over 50% of the votes, who the minimum candidate(s) are and whether or not the remaining candidates are tied.  Basically, my program creates a list of candidates and ballots, and then for each round determines who the losers are and removes them from the candidate list.  All votes for removed candidates are replaced with zeros so that that ballot's next highest un-eliminated vote can be counted.  This continues until someone has majority or the remaining candidates are tied, at which case the program ends.

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

#Here I create list of the candidates:
count = 0
while count < nCand:
    count += 1
    line = myFile.readline().strip('\n')
    tempperson = Candidate(line, count)
    candidates.append(tempperson)

#First round of votes: the votes are stored in the list "votearray" to be accessed and updated as candidates are eliminated.  If a number in the first choices of votes corresponds to a candidates index number, I add a vote to their total:
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

#If there is no winner after the first round: enter loop until winner is picked:

while isWinner is False:
    
    minvotes = 1000
    minvoteentry = []

    #find minimum number of votes, remove candidates who tied for last
    losers = []
    minVotes = minCand(candidates)
    i = 0
    while i < 20:
        if (candidates[i].isElim == True):
            entry = candidates[i]
            losers.append(entry.index)
            candidates.remove(entry)
            nCand -= 1
        else:
            i += 1
        if (i == nCand):
            break

    #Replace votes for eliminated candidates with zeros:
    for entry in losers:
        loserindex = str(entry)
        i = 0
        for ballot in votearray:
            ballot = string.replace(ballot, loserindex, '0')
            votearray[i] = ballot
            i += 1

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

    if (isTie(candidates) == True):
        for person in candidates:
            print person.name
        isWinner = True

    if (isMajority(candidates, nBallots) != 0):
        print isMajority(candidates, nBallots)
        isWinner = True
    


myFile.close()
