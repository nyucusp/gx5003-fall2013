#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 2

"""
Australian ballots require that voters rank all the candidates in order of choice.
Initially only the first choices are counted, and if one candidate receives more than
50% of the vote then that candidate is elected. However, if no candidate receives more 
than 50%, all candidates tied for the lowest number of votes are eliminated. Ballots 
ranking these candidates first are recounted in favor of their highest-ranked 
non-eliminated candidate. This process of eliminating the weakest candidates and 
counting their ballots in favor of the preferred non-eliminated candidate continues
until one candidate receives more than 50% of the vote, or until all remaining candidates 
are tied.
"""

import sys

def ballotCounter(candidates, ballots_list): 
    isWinner = False
    candidatesdict = candidates.copy()
    ballotLength = len(ballots_list)

    for key in candidatesdict:
        voteCount = 0   
        for j in range(0,ballotLength):
            if (candidatesdict[key] == int(ballots_list[j].split()[0])):
            	voteCount += 1
                
        candidatesdict[key] = voteCount
    
    #check if one candidate has more than 50% of the votes and if true return candidate 
    for key in candidatesdict:
        if float(candidatesdict[key])/ballotLength > .5:
            isWinner = True
            print key
            
    tally = [(votes, name) for name, votes in candidatesdict.items()]
    
    #all candidates are tied 
    if max(tally)[0] == min(tally)[0] and len(tally) > 1:
        isWinner = True

        for key in candidatesdict:
            print key
    


    #removes the lowest voted candidates from candidates dictionary
    if (isWinner == False):
    	candidates_runoff = candidates.copy()
    	new_ballots = ballots_list[:]
    	lowest_candidates = {}

        for key in candidatesdict:
            if candidatesdict[key] == min(tally)[0]:
                lowest_candidates[key] = candidates[key]
                del candidates_runoff[key]
        #updates ballots by removing lowest candidates from ballot list
        for k in range(0,len(new_ballots)):
            for key in lowest_candidates:
                new_ballots[k] = new_ballots[k].translate(None, str(lowest_candidates[key])).lstrip()
        #recursively call ballotCounter until a winner is determined
        ballotCounter(candidates_runoff, new_ballots) 
       

def main():
	myFile = open('input2.txt', 'r')
	numElections = int(myFile.readline())

	currentElection = 0 #counter for each election

	myFile.readline() #read blank line
	    
    #loop iterates through the number of elections
	while (currentElection < numElections):
		
		numCandidates = int(myFile.readline())
		candidates = {}

		for i in range(0,numCandidates):
			candidates[myFile.readline().strip()] = int(i+1)

		ballots = []
		line = myFile.readline()
		#loop iterates through ballet lines until there is a newline or blank line
		while(line != "" and line != "\n" and line != "\r"):
			ballots.append(line.strip())
			line = myFile.readline()

		ballotCounter(candidates, ballots)

		currentElection += 1 #increment election counter


	myFile.close()




if __name__=='__main__':
    main()