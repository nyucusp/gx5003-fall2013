#ugh, this is one of the worst scripts I've ever written. So sorry


ballots = open("input2.txt","r")
fileContents = ballots.readlines()
numOfCases = fileContents[0]
del fileContents[0]
choice = 0
numVoters = 0
numOfCands = 0
candidates = {}


def parseFile(ballotInfo):
    global numOfCands
    global candidates 
    #votes holds the candidate index as key and the number of votes as value
    votes = {}
    #test for is digit with a single index of 0
    numOfCands = int(ballotInfo[0])
    del ballotInfo[0]
    #add candidates and their corresponding voting index in the list to a dictionary
    #where key is the array index and value is its corresponding candidate
    for index in range(numOfCands):
    #increase the candidates index position by one to account for arrays starting
    #at 0 (since in the ballots, the votes are, for example, 1,2,3 not 0,1,2)
        temp = index+1
        #candidates relates names to candidate index
        candidates[temp] = ballotInfo[0]
        #votes holds candidate's index and their vote count
        votes[temp] = 0
        del ballotInfo[0]
    #go through votes and add up first choice for each candidate
    #holds on to the choice index
    tallyTotals = tallyInitialVotesPerCandidate(ballotInfo, votes, True)
    calculate(tallyTotals, ballotInfo)


def tallyInitialVotesPerCandidate(ballotInfo, votes, firstPass):
    #each time the function is called, tally the next choices of voters
    global choice
    global numVoters

    
    for ballot in ballotInfo:

        #makes sure that it is only checking ballots - if the first index in the list
        #is a space, then there is a ballot. This holds because if the loop hits an index
        #where the first index is not a ' ' , it will be a string containing an
        #integer signifying the number of candidates to follow (the start of a
        #new case).  
        if len(ballot)>1:
            #if line contains as many indexes as there are candidates
            #ballot info only consists of votes and other cases at this point, so will work
            if ballot[1] == ' ' and len(ballot) > choice+1:
        #only increment the number of voters for the first pass through of the
        #ballot list.                
                if firstPass == True:
                    numVoters += 1
                candidateIndex = ballot[choice]
            #increment the number of votes a candidate has if his index is present
                if int(candidateIndex) in votes:
                    votes[int(candidateIndex)] += 1
    return votes

    
def calculate(tallyTotals, ballotInfo):
    global numVoters
    lowestCand = []
    lowestNum = 0
    fiftyPerc = float(numVoters/2)
    #this can be reinitialized every time because the tallyvotes function
    #is only called if winners array is empty
    winners = []

    checkFirst = True
    count = 0
    lastElement = len(tallyTotals)
    #case when everyone ties
    if lastElement > 1:
        for candidate in tallyTotals:
            count += 1
            if checkFirst == True:
                comparison = tallyTotals[candidate]
                checkFirst = False
            if tallyTotals[candidate] != comparison:
                break;
            else:
                if count < lastElement:
                    continue
                else:
                    print "tie"
                    return 0


    
    enterInitialize = True
    for candidate in tallyTotals:
        if tallyTotals[candidate] > fiftyPerc:
            #use a list in case there are multiple tied winners
            winners.append(candidate)
        else:
            #if we already have a winner, don't need to test for more losers,
            #only need to find other potential winners
            if len(winners) == 0:
                if enterInitialize == True:
                    lowestNum = tallyTotals[candidate]
                    #lowestCand = []
                    lowestCand.append(candidate)
                    enterInitialize = False
                elif tallyTotals[candidate] < lowestNum:
                    #this numbers is less than all others potential losers that may have tied, so
                    #clear whole list
                    lowestNum = tallyTotals[candidate]
                    del lowestCand[:]
                    lowestCand = []
                    lowestCand.append(candidate)
                elif tallyTotals[candidate] == lowestNum:
                    #possible group of lowest candidates, so add to list
                    if candidate not in lowestCand:
                        lowestCand.append(candidate)

    if len(lowestCand)!=0:
        for personIndex in lowestCand:
            #test to make sure candidate is in tallyTotals just in case there were duplicates or a mishap
            if personIndex in tallyTotals:
                #remove candidate from list of candidates becuase they have the least number of votes
                del tallyTotals[personIndex]


    tempArr = []
    votesForRecount = []
    if len(winners) == 0:
        for line in ballotInfo:
            for num in lowestCand:
                #print "num " +str(num)
                if len(line)>1:
                 #   print "in if 1"
                    if line[1] == ' ':
                  #      print "in if 2"
                        if int(line[0]) == int(num):
                   #         print "in if 3 "
                            #holds ballots that need to be recounted
                            tempArr.append(line)

        
        for i in tempArr:
            #strip first vote from the array because already accounted for
            votesForRecount.append(i[2:])
        voteCount = tallyInitialVotesPerCandidate(votesForRecount, tallyTotals, False)
        #print "ballotInfo: " + str(ballotInfo)
        calculate(voteCount, ballotInfo)
 
        
    else: printWinner(winners)
    

def printWinner(winners):
    for index in winners:
        print candidates[index]        

    
def main():
    arr = []
    for i in fileContents:
        if i != "\n":
            #all items in list are now floats and \n characters are ommitted
            arr.append(i.rstrip('\n'))
    parseFile(arr)
    

if __name__ == "__main__":
    main()
