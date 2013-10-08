#Katherine Elliott
#ke638
#Assignment 3 Problem 2

inputfile = open('input2.txt', 'r')

file_lines = []
for line in inputfile:
    file_lines.append(line)
inputfile.close()

#Parse file to identify election
election_list = []
next_line=[]
for i in range(1,len(file_lines)):
    if file_lines[i] == '\n':
        next_line.append(i)
next_line.append(len(file_lines))
 
for j in range(0,len(next_line)-1):
    election_list.append(file_lines[next_line[j]+1:next_line[j+1]]) 


#Define function to output results. Election is split into candidate dictionary
#assigning integers to candidate names and a list of ballots

def results(given_election):
    candidate_dict = {}
    for i in range(1,int(given_election[0])+1):
        candidate_dict[given_election[i][:-1]]=i
    
    ballots = given_election[int(given_election[0])+1:]
    election_results(candidate_dict, ballots)
    
#This function is repeated eliminating candidates tied for last, computing winner with remaining
def election_results(candidates, votes):
    candidates_votes = candidates.copy()
    num_votes = len(votes)
    election_end = 0
    
    for key in candidates_votes:
        vote_count = 0
        for k in range(0,num_votes):
            if candidates_votes[key] == int(votes[k].split()[0]):
                vote_count += 1
        candidates_votes[key] = vote_count
        
        #if candidate has over 50% wins first round
    for key in candidates_votes:
        if float(candidates_votes[key])/num_votes > .5:
            election_end += 1
            print key
        #other wise tally votes
    tally_list = [(tally, name) for name, tally in candidates_votes.items()]
    if max(tally_list)[0] == min(tally_list)[0] and len(tally_list) > 1:
        election_end += 1
        for key in candidates_votes:
            print key
            
    remaining_candidates = candidates.copy()
    new_ballots = votes[:]
    eliminated_candidates = {}
    if election_end == 0:
        for key in candidates_votes:
            if candidates_votes[key] == min(tally_list)[0]:
                eliminated_candidates[key] = candidates[key]
                del remaining_candidates[key]
        #removes eliminated candidates    
        for i in range(0,len(new_ballots)):
            for key in eliminated_candidates:
                new_ballots[i] = new_ballots[i].translate(None, str(eliminated_candidates[key])).lstrip()
                
        election_results(remaining_candidates, new_ballots)
    
for case in election_list:
    results(case)
    print ""