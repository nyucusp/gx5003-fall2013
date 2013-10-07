from collections import Counter
from decimal import *
import math
import itertools

inp = open("input2.txt","r")
data = inp.readlines()
inp.close()

lines = []
for line in data:
    lines.append(line.strip())

#Find the rows of the cases
data = data[2:]
numOfCase = []
numOfCase.append(0)
i = 0
for line in data:
    if line == "\n":
        numOfCase.append(i+1)
    i = i + 1
numOfCase.append(len(data))

numOfCases = int(lines[0])

numOfCase[numOfCases] = numOfCase[numOfCases]+1


#Counts the number of votes, minimum&maximum voted candidate, losers for the round
def countaq(self):
    dict = {}
    for i in range(1,numOfCand+1):
        c = Counter(self)
        if c[str(i)] !=0:
            dict[i] =c[str(i)]
    a=min(dict.items(), key=lambda x: x[1] )
    b=max(dict.items(), key=lambda x: x[1] )
    losers=[]
    mini = a[1]
    maxi = b[1]
    for k,v in dict.iteritems():
        if v==mini:
            losers.append(k)
            
    return mini, maxi, a, b, losers, dict

#rounds for each election period
def rounds1(numOfCand,ballots):
    rounds = [[] for i in range(numOfCand)]
    for i in range(numOfCand):
        for element in ballots:    
            part = element.split()
            rounds[i].append(part[i])
    return rounds

#removes the losers from the round array and replaces them
def remove(self):
    for j in range(0,len(self)):
        for i in range(0,len(ballots)):
            if int(rounds[0][i]) == self[j]:
                rounds[0].append(rounds[1][i])
    for j in range(0,len(self)):
        rounds[0].remove(str(self[j]))

#evaluates the whole thing
def evaluation():
    res=0
    while res==0:
        (mini, maxi, a, b, losers, dict) = countaq(rounds[0])
        if mini == maxi:           
            for i in range(0,len(losers)):
                print names[losers[i]-1]

            print ''
            break
        elif float(maxi)/sum(dict.values())>float(50)/100:
            print names[(b[0]-1)]+'\n'
            break
        else:
            remove(losers)

###Does it for all the cases
i = 0
while i < (numOfCases):
    numOfCand = int(lines[numOfCase[i]+2])
    names = lines[numOfCase[i]+3:numOfCase[i]+3+numOfCand]
    ballots = lines[numOfCase[i]+3+numOfCand:numOfCase[i+1]+1]
    if len(ballots) != 0:
        (rounds)=rounds1(numOfCand,ballots)
        evaluation()
    i=i+1

# IF IT DOESN'T GIVES AN ANSWER DELETE THE BLANK ROW AT THE END


