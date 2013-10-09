import sys


"""
First we open the text file and save the lines to the list input_lines.  Please note
this program is NOT robust enough to handle input that differs even slightly from
the format in the problem (e.g. if there are TWO blank lines between cases, as opposed
to ONE, there will be an error).  Also, if there is more than ONE blank line at the
end of input2.txt, there will be an error.
"""
inputfile = open('input2.txt', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()


"""
Now we parse the file and save each case as a list in case_list (so case_list is a list
of lists).  Here, a case starts with an integer (the number of candidates), followed by
the candidate names, then the ballot information.  Note that we don't make use of
the number of cases (the first line of input2.txt).
"""
case_list = []
newline_markers=[]
for i in range(1,len(input_lines)):
    if input_lines[i] == '\n':
        newline_markers.append(i)
newline_markers.append(len(input_lines))
 
for k in range(0,len(newline_markers)-1):
    case_list.append(input_lines[newline_markers[k]+1:newline_markers[k+1]]) 

"""
Now we define a function election_results, that takes a case as input, and outputs
the winning candidates.  We will (eventually) call this function for each case in
case_list.  In this function, we first split the case into two structures.  The first is
candidate_dict, a dictionary whose keys are the names of the candidates and whose
values are 1,...,n, depending on the order they appear in the case (this integer is
their identifier in the ballot).  The second is votes_list, which is just a list of
all ballots cast.  We will pass this information to another function called 
election_solver, which will take candidate_dict and votes_list as input, then run
recursively and solve the election.
"""

def election_results(current_case):
    candidate_dict = {}
    for i in range(1,int(current_case[0])+1):
        candidate_dict[current_case[i][:-1]]=i
    
    votes_list = current_case[int(current_case[0])+1:]
    election_solver(candidate_dict, votes_list)
    
"""
We now define election_solver, the most important function of this assignment. In brief,
it totals up candidate votes, gives a winner or winners if appropriate, and otherwise
eliminates the losing candidate(s) and amends the list of votes to remove their identifiers.
Then it is called again, until the election is solved. 
"""

def election_solver(candidates, votes):
    
    """
    First we make a new dict, candidates_votes, with the candidate names as keys
    and the tally of their votes as values.  We also define a "state checker" called
    case_ender which will be either 0 or 1.  If a candidate has more than 50% of the 
    votes or all candidates are tied, we change case_ender to 1.  Otherwise, we 
    remove the lowest ranked candidate(s) and run election_solver again.
    """
    candidates_votes = candidates.copy()
    num_votes = len(votes)
    case_ender = 0
    
    for key in candidates_votes:
        vote_count = 0
        for j in range(0,num_votes):
            if candidates_votes[key] == int(votes[j].split()[0]):
                vote_count += 1
        candidates_votes[key] = vote_count
        
    """
    Here we deal with the scenario that one candidate has
    more than 50% of the votes. We must cast either candidates_votes[key]
    or num_votes as a float to do the division properly.
    """
    for key in candidates_votes:
        if float(candidates_votes[key])/num_votes > .5:
            case_ender += 1
            print key
            
    """
    Here we deal with the scenario where all candidates are tied. We invert
    candidates_votes and check if the max and min key are the same (meaning all remaining
    candidates are tied).  If so, and if there is more than one candidate (to avoid
    duplicating the candidate name in case there is just one candidate left),
    we print out all keys.  
    """
    tally_list = [(tally, name) for name, tally in candidates_votes.items()]
    if max(tally_list)[0] == min(tally_list)[0] and len(tally_list) > 1:
        case_ender += 1
        for key in candidates_votes:
            print key
            
    """
    Here we need to do the recursive part, i.e. removing the lowest ranked candidate
    from candidates, and amending the votes list to take into account the second
    or third preference.  To avoid changing the dictionary while we iterate over it,
    we create a new_candidates, a copy of candidates from which we have
    removed the lowest ranked candidates.  Similarly, we create a new copy of 
    votes which we amend, and name new_votes_list.  
    
    We also create a new dict called lowest_candidates whose keys are the names of those 
    candidates who are to be removed, and values are their identifier in the ballot 
    (just like with candidates or new_candidates).  This will aid us in 
    determining how to amend the votes for the next round of election_solver.
    
    Finally, we call election_solver with new_candidates and new_votes_list as
    arguments.
    """
    new_candidates = candidates.copy()
    new_votes_list = votes[:]
    lowest_candidates = {}
    if case_ender == 0:
        for key in candidates_votes:
            if candidates_votes[key] == min(tally_list)[0]:
                lowest_candidates[key] = candidates[key]
                del new_candidates[key]
        
        """
        Now we iterate through new_votes_list and then iterate through
        the candidates in lowest_candidates.  We remove all identifiers in every 
        vote that match the identifier of a candidate in lowest_candidates (so we 
        decrease the length of every vote by exactly the number of keys
        in lowest_candidates).  We use the lstrip() function to remove leading
        whitespace in a vote (after the previous identifier removal) if necessary.
        """    
        for i in range(0,len(new_votes_list)):
            for key in lowest_candidates:
                new_votes_list[i] = new_votes_list[i].translate(None, str(lowest_candidates[key])).lstrip()
                
        election_solver(new_candidates, new_votes_list)

"""
Finally, we iterate through all cases and print the results.
"""    
for case in case_list:
    election_results(case)
    print ""
