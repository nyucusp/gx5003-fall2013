#Aliya Merali
#Assignment 3
#Problem 2

#Create a function to isolate the votes and clean up the data format
def get_votes(x):
    """The expected input is of the form: ['3\n', 'John Doe\n', 'Jane Smith\n', 'Jane Austen\n', '1 2 3\n', '2 1 3\n', '2 3 1\n', '1 2 3\n', '3 1 2\n', '\n']"""
    n = int(x[0]) #number of candidates
    ballots = x[(n+1):]
    parsed_ballots = []
    for ballot in ballots:
        temp = ballot.strip()
        if temp != "":
            parsed_ballots.append(temp.split(" "))
    return parsed_ballots

def get_names(x, winners):
    results = []
    for winner in winners:
        results.append(x[int(winner)].strip())
    return results


#Create a function tally the votes for each candidate into a dictionary       
def get_round_votes(ballot_info):
    """The expected input is of the form: [['1', '2', '3'], ['2', '1', '3'], ['2', '3', '1'], ['1', '2', '3'], ['3', '1', '2']]"""
    first_rank = {}
    for ballot in ballot_info:
        if len(ballot) == 0: #So we don't try to use ballots that are empty later on
            continue
        if ballot[0] in first_rank:
            first_rank[ballot[0]] = first_rank[ballot[0]] + 1
        else:
            first_rank[ballot[0]] = 1
    return first_rank

def get_winners(candidate_votes):#where input is a dictionary of candidates and votes
    if candidate_votes == {}:
        return []
    max_votes = max(candidate_votes.values())
    winners_list = []
    for k in candidate_votes:
        if candidate_votes[k] == max_votes:
            winners_list.append(k)
    return winners_list

def get_losers(candidate_votes):
    if candidate_votes == {}:
        return []
    min_votes = min(candidate_votes.values())
    losers_list = []
    for k in candidate_votes:
        if candidate_votes[k] == min_votes:
            losers_list.append(k)
    return losers_list

#adjust the ballots to get rid of the losers if they were first vote in ballot
def drop_min(ballots, losers):
    for ballot in ballots:
        for loser in losers:
            if loser in ballot:
                ballot.remove(loser)

def evaluate(ballots, votes):
     print 'Evaluate Input = ' + str(ballots)
     while True:
         min_to_win = len(ballots)/2 + 1
         round_votes = get_round_votes(ballots)
         winners = get_winners(round_votes)
         losers = get_losers(round_votes)
         vote_count = round_votes[winners[0]]
         winners.sort()
         losers.sort()
         if vote_count >=  min_to_win:
             return get_names(votes, winners)
         elif winners == losers:
             return get_names(votes, winners)
         else:
             drop_min(ballots, losers)
         
         

input = open('input2.txt','r')
data = input.readlines()
data = data[2:]

#Find out the range of data for each case
caseBreak = []
caseBreak.append(0)
i = 0
for line in data:
    if line == "\n":
        caseBreak.append(i+1)
    i = i + 1
caseBreak.append(len(data))


#Call the data in one case
j = 0
while j < (len(caseBreak) - 1):
    votes = []
    index = caseBreak[j]
    while ((caseBreak[j]) <= index < (caseBreak[j+1])):
        votes.append(data[index])
        index = index + 1
        #Now I need to go through the lists of data and do the problem....
#        n = votes[0] #number of candidates
#        x = 1
#    while ( 0 < x < len(votes) ):
#        print votes[x]
#        x = x + 1
    print 'Winner = ' + str(evaluate(get_votes(votes), votes))
    print
    j = j + 1



#defining a function to do problem
#n = votes[0] #number of candidates
#while ( n  < x < len(votes) ):
#    print votes[x]
#    x = x + 1

    
    


#Create a list with just voter values, and count the number of votes in this set
#index = 3 + int(n)
#i = 0 
#numVotes = 0
#while data[index] != "\n":
#    votes.append(data[index].split(" "))
#    index = index + 1
#    numVotes = numVotes + 1
