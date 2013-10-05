#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 2


from collections import defaultdict

myFile = open('input2.txt', 'r')
numElections = int(myFile.readline())

currentElection = 0

myFile.readline() #read blank line

def ballotCounter(candidates, ballots):
    isWinner = False
    #first check to see if first candidate has greater than 50% of the votes 
    candidatesdict = candidates.copy()

    for key in candidatesdict:
        voteCount = 0
        for j in range(0,len(ballots)):
            if (candidatesdict[key] == int(ballots[j].split()[0])):
                voteCount += 1
        candidatesdict[key] = voteCount
    print candidatesdict
    
    #check if one candidate has more than 50% of the votes 
    for key in candidatesdict:
        if float(candidatesdict[key])/len(ballots) > 0.5:
            isWinner = True
            print key
            
    #all candidates are tied 
    tally = [(votes, name) for name, votes in candidatesdict.items()]
    print "tally below:"
    print tally
    
    
    if max(tally) == min(tally) and len(tally) > 1:
        isWinner = True
        for key in candidatesdict:
            print key
    
    candidates_runoff = candidatesdict.copy()
    new_ballots = ballots[:]
    lowest_candidates = {}
    if (isWinner == False):
        for key in candidatesdict:
            if candidatesdict[key] == min(tally):
                lowest_candidates[key] = candidatesdict[key]
                del candidates_runoff[key]
    
        for i in range(0,len(new_ballots)):
            for key in lowest_candidates:
                new_ballots[i] = new_ballots[i].translate(None, str(lowest_candidates[key])).lstrip()
    
        ballotCounter(candidates_runoff, new_ballots)
                
    
while (currentElection < numElections):
    numCandidates = int(myFile.readline())
    print "numCandidates: %s" % (numCandidates)
    candidates = {}
    for i in range(0,numCandidates):
        candidates[myFile.readline().strip()] = int(i+1)
        print candidates
    ballots = []
    line = myFile.readline()
    while(line != "" and line != None and line != "/n"):
        ballots.append(line.strip())
        print ballots
        line = myFile.readline()
    ballotCounter(candidates, ballots)
    print len(ballots)
    currentElection += 1