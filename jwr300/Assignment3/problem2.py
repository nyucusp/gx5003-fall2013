#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 2

import sys

myFile = open('input2.txt', 'r')
numElections = int(myFile.readline())

currentElection = 0

myFile.readline() #read blank line

def ballotCounter(candidates, ballots_list):
    #first check to see if first candidate has greater than 50% of the votes 
    candidatesdict = candidates.copy()
    isWinner = False
    ballotLength = len(ballots_list)

    for key in candidatesdict:
        voteCount = 0   ####fix bug on vote count
        for j in range(0,ballotLength):
            if (candidatesdict[key] == int(ballots_list[j].split()[0])):
            	voteCount += 1
                
        candidatesdict[key] = voteCount
    
    #check if one candidate has more than 50% of the votes 
    for key in candidatesdict:
        if float(candidatesdict[key])/ballotLength > .5:
            isWinner = True
            print key
            
    #all candidates are tied 
    tally = [(votes, name) for name, votes in candidatesdict.items()]
    
    
    if max(tally)[0] == min(tally)[0] and len(tally) > 1:
        isWinner = True
        
        for key in candidatesdict:
            print key
    
    candidates_runoff = candidates.copy()
    new_ballots = ballots_list[:]
    lowest_candidates = {}
    if (isWinner == False):
        for key in candidatesdict:
            if candidatesdict[key] == min(tally)[0]:
                lowest_candidates[key] = candidates[key]
                del candidates_runoff[key]

        for k in range(0,len(new_ballots)):
            for key in lowest_candidates:
                new_ballots[k] = new_ballots[k].translate(None, str(lowest_candidates[key])).lstrip()

        ballotCounter(candidates_runoff, new_ballots)
                
    
while (currentElection < numElections):
    numCandidates = int(myFile.readline())

    candidates = {}
    for i in range(0,numCandidates):
        candidates[myFile.readline().strip()] = int(i+1)

    ballots = []
    line = myFile.readline()
    while(line != "" and line != "/n"):
        ballots.append(line.strip())

        line = myFile.readline()
    ballotCounter(candidates, ballots)

    currentElection += 1