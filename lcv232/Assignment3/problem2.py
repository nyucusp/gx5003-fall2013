import sys
import math

input = open('input2.txt','r')
value1 = input.readlines()
value1 = value1[2:]


break_arr = []
break_arr.append(0)
z = 0
for call in value1:
    if call == "\n":
        break_arr.append(z+1)
    z = z + 1
break_arr.append(len(value1))


def candidates(x, win1):   # Getting the list of candidates.
    end_res = []
    for winner in win1:
        end_res.append(x[int(winner)].strip())
    return end_res


def votes_received(x):
    a = int(x[0])   # Number of Candidates in the election being listed in the array.
    put_vote = x[(a+1):]
    votes_array = []
    for num_votes in put_vote:
        val1 = num_votes.strip()
        if val1 != "":
            votes_array.append(val1.split(" "))
    return votes_array  # Returning the captured votes in the array.


def other_votes(abc):
    pref_1 = {}
    for num_votes in abc:
        if len(num_votes) == 0:
            continue
        if num_votes[0] in pref_1:
            pref_1[num_votes[0]] = pref_1[num_votes[0]] + 1
        else:
            pref_1[num_votes[0]] = 1
    return pref_1


def check(cast_ballots, put_vote):
     while True:
         win_mark = len(cast_ballots)/2 + 1
         nextvotes = other_votes(cast_ballots)
         win1 = win2(nextvotes)
         lost_1 = lost(nextvotes)
         count_vote_num = nextvotes[win1[0]]
         win1.sort()
         lost_1.sort()
         if count_vote_num >=  win_mark:
             return candidates(put_vote, win1)
         elif win1 == lost_1:      # Conditioning for the probability of a tie.
             return candidates(put_vote, win1)
         else:
             del_min(cast_ballots, lost_1)


def lost(votes_cand):   #Defining Losers.
    if votes_cand == {}:
        return []
    l_votes = min(votes_cand.values()) # using min() function to find the lowest number of votes given to the candidates.
    list_lost = []
    for k in votes_cand: # Having the candidates with the lowest number of votes.
        if votes_cand[k] == l_votes:
            list_lost.append(k)
    return list_lost


def win2(votes_cand): # Defining Winners.
    if votes_cand == {}:
        return []
    h_votes = max(votes_cand.values()) # Seeking the highest number of votes to the candidates.  
    list_win = []     
    for k in votes_cand:
        if votes_cand[k] == h_votes:
            list_win.append(k)
    return list_win

def del_min(cast_ballots, lost_1):    # Eliminating Losers in round of voting.
    for num_votes in cast_ballots:
        for bal_lost in lost_1:
            if bal_lost in num_votes:
                num_votes.remove(bal_lost)

         
cnt1 = 0     # Checking all cases of the functions mentioned in the program above.
while cnt1 < (len(break_arr) - 1):
    put_vote = []
    index = break_arr[cnt1]
    while ((break_arr[cnt1]) <= index < (break_arr[cnt1+1])):
        put_vote.append(value1[index])
        index = index + 1
    print (check(votes_received(put_vote), put_vote))
    cnt1 = cnt1 + 1

