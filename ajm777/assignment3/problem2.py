#Aliya Merali
#Assignment 3
#Problem 2

#First, writing all teh functions you will need to evaluate the data

#Create a function to isolate the votes from the data and clean up the data format
def get_votes(x):
#The expected input is of the form: ['3\n', 'John Doe\n', 'Jane Smith\n', 'Jane Austen\n', '1 2 3\n', '2 1 3\n', '2 3 1\n', '1 2 3\n', '3 1 2\n', '\n'] 
    n = int(x[0]) #number of candidates
    ballots = x[(n+1):] #where the actual ballots start
    parsed_ballots = []
    for ballot in ballots:
        temp = ballot.strip() #getting rid of the \n at the end of each line
        if temp != "": #if there is something in this element, then split it by spaces
            parsed_ballots.append(temp.split(" "))
    return parsed_ballots #output a list of ballots in good format for get_round_votes function

#function to extract names from data by their corresponding numbers, inputs raw data and winners
def get_names(x, winners):
    results = []
    for winner in winners:
        results.append(x[int(winner)].strip())
    return results

#Create a function tally the votes for each candidate into a dictionary       
def get_round_votes(ballot_info):
#The expected input is of the form: [['1', '2', '3'], ['2', '1', '3'], ['2', '3', '1'], ['1', '2', '3'], ['3', '1', '2']]
    first_rank = {}
    for ballot in ballot_info:
        if len(ballot) == 0: #So we don't try to use ballots that are empty later on
            continue
        if ballot[0] in first_rank: #initializing -- if the ballot isn't in dict, add it, else add to it
            first_rank[ballot[0]] = first_rank[ballot[0]] + 1
        else:
            first_rank[ballot[0]] = 1
    return first_rank

def get_winners(candidate_votes):#where input is a dictionary of candidates and votes
    if candidate_votes == {}: #if there is nothing in the dictionary element (if we deleted them all) then, return an empty element
        return []
    max_votes = max(candidate_votes.values()) #find the highest no. of votes
    winners_list = []
    for k in candidate_votes: #See how many have that number, add them to the list of winners
        if candidate_votes[k] == max_votes:
            winners_list.append(k)
    return winners_list

def get_losers(candidate_votes):#input is dictionary of candidates and votes
    if candidate_votes == {}: #if there is nothing in the dictionary element (if we deleted them all) then, return an empty element
        return []
    min_votes = min(candidate_votes.values()) #find the lowest no. of votes
    losers_list = []
    for k in candidate_votes: #make a list of all the candidates with lowest no. of votes
        if candidate_votes[k] == min_votes:
            losers_list.append(k)
    return losers_list

#adjust the ballots to get rid of the losers if they were first vote in ballot
def drop_min(ballots, losers):
    for ballot in ballots:
        for loser in losers:
            if loser in ballot:
                ballot.remove(loser)

#function to call all others and evaluate the data
def evaluate(ballots, votes):
     while True:
         min_to_win = len(ballots)/2 + 1 #min amount of votes to win
         round_votes = get_round_votes(ballots)
         winners = get_winners(round_votes)
         losers = get_losers(round_votes)
         vote_count = round_votes[winners[0]]
         winners.sort()
         losers.sort()
         if vote_count >=  min_to_win:
             return get_names(votes, winners)
         elif winners == losers: #in the case of a tie, when both have highest and lowest votes
             return get_names(votes, winners)
         else:
             drop_min(ballots, losers)
         
#Now input the data that you will need to evaluate
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


#Loop through the cases, and in each case call the functions above to evaluate each scenario
j = 0
while j < (len(caseBreak) - 1):
    votes = []
    index = caseBreak[j]
    while ((caseBreak[j]) <= index < (caseBreak[j+1])):
        votes.append(data[index])
        index = index + 1
    print str(evaluate(get_votes(votes), votes))
    print
    j = j + 1
