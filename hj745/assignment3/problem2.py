#      < algorithm >
#1. voter ranks all candidates
#2. gather the #1 candidates and elect candidates who get over half of ballots
#3. if there is no elected candidate, drop the candidates, who get the lowest ballots
#   (one or more candidates can be dropped)
#4. Among ballots that elected candidates who are already droppped as the top priority, if there are candidates who are elected by the ballots, then give ballots to those who are elected by the voters   
#5. Aggregate again, and if there are candidates who get more than half of ballots, then elect the candidates
#   But, if not, repeat the #3

LIMIT_NUM_OF_VOTE = 1000 # maximum number of voters
LIMIT_NUM_OF_CANDIDATE = 20 # maximum number of candidates

f = open('input2.txt', 'r') #open the input file
input = f.readlines() # read the whole file as a list of lines

def who_is_number_one(the_votes): #to find the candidate who get the most of ballots
    total_of_candidate = {} # this is for listing the gathered ballots
    for i, vote in ipairs( the_votes ): # to check the entire ballots
        if 0 != the_vote: # if there is any candidate who has not been dropped on the ballots
            if nil == total_of_candidate[vote[1]]: # then elect the first one
                total_of_candidate[vote[1]] = 1
            else:
                total_of_candidate[vote[1]] = total_of_candidate[vote[1]] + 1

    max_total_num_of_vote = 0
    index_of_best_candidate = 0
 
    for k, v in pairs( total_of_candidate ): # to find the candidates who get the most of ballots
        if v >= max_total_num_of_vote:
            max_total_num_of_vote = v
            index_of_best_candidate = k
        
        if max_total_num_of_vote > (the_votes/2): # if the candidates get more than half of ballots,
            return index_of_best_candidate # then, return
        else:
            min_total_num_of_vote = max_total_num_of_vote # if not, find the candidates who get the least of ballots
            index_of_worst_candidate = 0
            
    for k, v in pairs( total_of_candidate ):
        if v <= min_total_num_of_vote:
            max_total_num_of_vote = v
            index_of_worst_candidate = k
        
    if max_total_num_of_vote == min_total_num_of_vote: # if the least ballots and the most ballots are the same
        return 0 # then return to repeat the voting

    for i, vote in ipairs( the_votes ): #find the candidates who get the least of ballots among the entire ballots
        for i, index_of_candidate in ipairs( vote ):
            if index_of_worst_candidate == index_of_candidate: 
                table.remove( vote, i ) # then, remove the cadidates from the list
                break
    return who_is_number_one( the_votes ) # then, return
 
def main():
    f = open('input2.txt', 'r')
    vote_case_num = f.readlines() 
    vote_case_num = tonumber( vote_case_num )
 
    if nil == vote_case_num:
        return
    
    for i = 1, vote_case_num, 1: # to make the loop for processing ballots
        f = open('A3_P2_Input.txt', 'r')
        candidate_num = f.readlines() # get the number of candidate  
        candidate_num = tonumber( candidate_num )
        if nil == candidate_num or LIMIT_NUM_OF_CANDIDATE < candidate_num: #if the number is not integer or exceed the limit
            return

        candidate_name_pack = {} # it is to get the name of candidates
        
        for i = 1, candidate_num, 1: # get the names of entire cadidates
            candidate_name_pack[candidate_name_pack + 1] = candidate_num
       
        the_votes = {} #it is for getting ballots
 
        for i = 1, LIMIT_NUM_OF_CANDIDATE, 1: # it is for ordering every cadidate in the ballots
            vote_t = {}
            vote_str = the_votes # get the ballots as string
            if "" == vote_str: # if the ballot is empty, set the ballots as already received
                break

            for candidate_index in string.gmatch( vote_str, "%d+" ): #get the ballots according to the numbering on the ballots
                vote_t[ vote_t + 1] = tonumber( candidate_index )
                the_votes[the_votes +1] = vote_t # insert the ballots to the voting list
        number_one = who_is_number_one( the_votes ) # start counting

        print( candidate_name_pack[number_one] )
        
if __name__ == '__main__':
    main()
