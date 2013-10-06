#Alex Chohlas-Wood (acw438). Assignment 3, Problem 2.

class Candidate:
    isRunning = True
    
    def __init__(self, ID, name):
        self.name = name
        self.ID = ID
        self.votes = []

    def addVote(self, vote):
        self.votes.append(vote)

    def eliminate(self):
        self.isRunning = False

    #Tally candidate's percentage of vote.
    def percentCalc(self, total):
        total = float(total)
        selfTally = len(self.votes)
        return selfTally/total

    #Distribute candidate's votes to other candidates, through canDict
    def distribute(self, canDict):
        for vote in self.votes:

            #Trim off the first vote (which is for an ineligible candidate)
            truncVote = vote[1:]
            
            #This keeps truncating the vote until it finds an eligible candidate
            #Then adds the vote to that eligible candidate
            keepLooping = True
            while keepLooping:
                if canDict[truncVote[0]].isRunning:
                    canDict[truncVote[0]].addVote(truncVote)
                    keepLooping = False
                else:
                    truncVote = truncVote[1:]
        return canDict

rawFile = open('input2.txt', 'r')
input2 = []
for line in rawFile:
    input2.append(line.strip())

#Discard number of scenarios at beginning of input:
input2 = input2[2:]


#Split scenarios into separate list entries:
scenarioList = [[]]
scenarioCounter = 0
for line in input2:
    if line != '':
        scenarioList[scenarioCounter].append(line)
    else:
        scenarioList.append([])
        scenarioCounter += 1


#Loop through scenarios:
for index, scenario in enumerate(scenarioList):

    #Make candidate instances, add to dictionary keyed to ID
    numCandidates = int(scenario[0])
    canDict = {}
    for i in range(1,numCandidates+1):
        canDict[str(i)] = Candidate(str(i), scenario[i]) #scenario[i]=candidate name
    
    #Create list of votes from remaining items in list:
    voteList = scenario[numCandidates+1:]

    #counting total # of voters
    voteTally = len(voteList)

    #Add votes to each voter's first choice candidate instance:
    for vote in voteList:
        voteSplit = vote.split(' ')
        canDict[voteSplit[0]].addVote(voteSplit)
    
    #Eliminate lowest-ranked candidates until a winner or tie is found
    keepRunning = True
    while keepRunning:
        voteShares = [] #Stores candidate voteshare and ID tuple

        #loop through ALL candidates, everytime:
        for ID, candidate in canDict.iteritems():
            
            #take only eligible candidates:
            if candidate.isRunning:

                #calculate their current voteshare
                voteShare = candidate.percentCalc(voteTally)

                #Add voteshare and ID tuple to voteShares list
                voteShares.append((voteShare, candidate.ID))

        #Find the lowest and highest voteshares:
        voteShares.sort()
        lowestShare = voteShares[0][0]
        highestShare = voteShares[-1][0]

        #Look for a >50% winner, OR
        if (highestShare > .5):
            print canDict[voteShares[-1][1]].name
            print ''
            keepRunning = False
        #A tie, in which there is no voteshare difference, OR
        elif (lowestShare == highestShare):
            for ID, candidate in canDict.iteritems():
                if candidate.isRunning:
                    print candidate.name
            print ''
            keepRunning = False
        #Eliminate loser.

        else:
            for candidates in voteShares:
                if candidates[0] == lowestShare:
                    canDict[candidates[1]].eliminate()
                    #Distribute their votes.
                    canDict = canDict[candidates[1]].distribute(canDict)

rawFile.close()
