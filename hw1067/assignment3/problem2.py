#Problem 4
#Haozhe Wang
"""
#if no candidate receives more than 50%, all candidates tied for the lowest number of votes are eliminated.
Ballots ranking these candidates first are recounted in favor of their highest-ranked non-eliminated candidate.
This process of eliminating the weakest candidates and
counting their ballots in favor of the preferred non-eliminated candidate continues
until one candidate receives more than 50% of the vote,
or until all remaining candidates are tied.
"""

from sys import exit

case = False
def youwin(vote):
    winnercounts = max(vote)
    storage = []

    if winnercounts >= sum(vote)/2 and vote.count(winnercounts) == 1:
        return vote.index(winnercounts)
    if min(vote) == 0:
        return "CUSP"
    return None

def eliminate(vote):
    x = 0
    loser = 0
    losercounts = min(vote)
    loser = vote.index(losercounts)
    loser += 1

    ballot_count = len(ballot)
    while x < ballot_count:
        ballot[x].remove(loser)
        #print ballot[x]
        x += 1
    return ballot
#line = []
#open and read lines from the input file
line = open("input2.txt").readlines()
#for lns in line:
#    print line.strip()
#    print line
line = [ln.strip() for ln in line]

case_num = int(line.pop(0))
for case in range(case_num):
    line.pop(0) #this can help skipping blank lines

    candidatecounts = int(line.pop(0))
    candidates = line[:candidatecounts]
    line = line[candidatecounts:]

    ballot = []
    while line and line[0]:
        ballot = [int(x)  for x in line.pop(0).split()]
        ballot.append(ballot)
    #print ballots
    vote = [0 for candidate in candidates]
    for ball in ballot:
        vote[ballot[0]-1] += 1

    while youwin(vote) is None:
        ballot = eliminate(vote)

        for ballot in ballots:
            vote[ballot[0]-1] += 1

        youwin(vote)

    i = 0
    if youwin(vote) == "CUSP":
        while i < len(vote):
            if vote[i] > 0:
                print "%s" % candidates[i]
            i += 1

    else:
        print "%s" % candidates[youwin(vote)]
        
    print
