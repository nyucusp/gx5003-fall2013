import sys

inputFile = open('input2.txt', 'r')                       # open .txt file

inputLines = []                                           # save lines in a list
for line in inputFile:
  inputLines.append(line)
inputFile.close()

"""
Parse through inputLines and save each case (ie. each ballot) in a list ballotsList. 
Each ballot starts with an integer that identifies the number of candidates, followed 
by the candidates' names, followed by the ballot information, ie. the values 1,...,n 
that denote the order or "place" of each candidate.
"""

ballotList = []
newLine=[]
for i in range(1,len(inputLines)):
  if inputLines[i] == '\n':
    newLine.append(i)
newLine.append(len(inputLines))
 
for k in range(0,len(newLine)-1):
  ballotList.append(inputLines[newLine[k]+1:newLine[k+1]])

"""
Define a function electionResults that takes a ballot currentBallot as input and 
outputs the winning candidate(s). Create candidateDict dictionary where they keys 
are candidate names and the values are where they "place" 1,...,n on each ballot. 
The function then takes a list ballotsList of each case (ie. all ballots cast) 
which will be fed into another function electionSolve which takes candidateDict 
and ballotsList as input and iterates recursively to solve for the winner(s).
"""

def electionResults(currentBallot):
  candidateDict = {}                                    # create dictionary of candidates
  for i in range(1,int(currentBallot[0])+1):        
    candidateDict[currentBallot[i][:-1]]=i
    
  ballotList = currentBallot[int(currentBallot[0])+1:]
  electionSolve(candidateDict, ballotList)
    
"""
Define a function electionSolve that takes candidateDict and ballotsList as input
and outputs winningCadndiate. The function will add up the votes for each candidate
and output the winner(s), winner being defined as having >50% of the botes. If no 
candidate has >50% of the votes, the function will eliminate the candidate with the 
least votes from candidateDict and repeat until at least one candidate has >50% of 
the votes.
"""

def electionSolve(candidates, votes)                    
  votesCandidates = candidates.copy()                   # create a new dictionary with key = candidate names, value = votes count
  votesCount = len(votes)
  endRace = 0                                           # endRace will change to 1 when a winner or a tie results
    
  for key in votesCandidates:      
    votesCount = 0
    for j in range(0,votesCount):
      if votesCandidates[key] == int(votes[j].split()[0]):
        votesCount += 1
    votesCandidates[key] = votesCount
    
  for key in votesCandidates:
    if float(votesCandidates[key])/votesCount > .5:     # if a candidate has more than 50% of the vote
        endRace += 1                                    # the race ends
        print key                                       # print the winning candidate's name
        
  votesTally = [(votes, candidates) for candidates, votes in votesCandidates.items()]
    if max(votesTally)[0] == min(votesTally)[0] and len(votesTally) > 1:     # if all candidates are tied
        endRace += 1                                                      
        for key in votesCandidates:
            print key
            
"""
If no candidate has >50% of the vote, and the candidates are not all tied, the 
function will elminate the candidate with the least votes from candidateDict and 
repeat until at least one candidate has >50% of the votes.
"""

  newCandidates = candidates.copy()
    newVotes = votes[:]
    losingCandidates = {}                               # create a new dictionary for candidates with lowest tally
    if endRace == 0:                                    # if the race is still on (ie. there is no winner and the candidates are not all tied
        for key in votesCandidates:
          if votesCandidates[key] == min(votesTally)[0]:
            losingCandidates[key] = candidates[key]
            del newCandidates[key]

"""
After losingCandidates has been removed from newCandidates, we iterate through newVotes
and elminate the votes associated with the losingCandidates.
"""

        for i in range(0,len(newVotes)):
          for key in losingCandidates:
            newVotes[i] = newVotes[i].translate(None, str(losingCandidates[key])).lstrip()    # remove leading whitespace
                
        electionSolve(newCandidates, newVotes)          # iterate through electionSolve again with newCandidates and newVotes

for currentBallot in ballotList:
    electionResults(currentBallot)
    print ""
