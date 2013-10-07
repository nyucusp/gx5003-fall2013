# Awais Malik
# Assignment 3
# Problem 2

input = open('input2.txt','r')

ballots = []


for line in input:
    ballots.append(line.strip())
    
ballots = ballots[2:]

ballot_list = [[]]
ballot_index = 0

for line in ballots:
    if not(line == ''):
        ballot_list[ballot_index].append(line)
    else:
        ballot_list.append([])
        ballot_index += 1

for ballot in ballot_list:        
    candidates = {}
    votes = []
    candidateID = 1
    
    num_cands = int(ballot[0])
    
    for line in ballot[1:num_cands+1]:
        candidates[str(candidateID)] = [line, 0, True]
        candidateID += 1
    
    for line in ballot[num_cands+1:]:
        votes.append(line.split(' '))
        
    permission = True    
    while(permission):
        for i in candidates:
            candidates[i][1] = 0
        
        for i in votes:    
            candidates[i[0]][1] += 1
    
        vote_tally = []
        for i in candidates:
            if candidates[i][2]:
                vote_tally.append([i,candidates[i][1]])
        
        vote_tally.sort(key = lambda x: x[1])
        
        if(vote_tally[-1][1] > (len(votes)/2)):
            print candidates[vote_tally[-1][0]][0]
            print ''
            permission = False
            
        elif(vote_tally[0][1] == vote_tally[-1][1]):
            for i in candidates:
                if candidates[i][2]:
                    print candidates[i][0]
            permission = False
            print ''
        else:
            min_votes = vote_tally[0][1]
            for i in vote_tally:
                if(i[1] == min_votes):
                    candidates[i[0]][2] = False
                    for index, x in enumerate(votes):
                        while not(candidates[votes[index][0]][2]):                    
                            if(x[0] == i[0]):
                                votes[index] = x[1:]
                        
input.close()