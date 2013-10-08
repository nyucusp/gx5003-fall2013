from sys import exit

needRunOff = False

def getWinner(votes):
    highest_count = max(votes)
    indexes = []

    if min(votes) == 0:
        return 2000

    if highest_count >= sum(votes) / 2 and votes.count(highest_count) == 1:
        return votes.index(highest_count)

    return None

def eliminate(votes):
    x = 0
    loser = 0
    lowest_count = min(votes)
    loser = votes.index(lowest_count)
    loser = loser + 1




    num_ballots = len(ballots)
    # if min(votes) == 0:
    #     needRunOff = True

    #     print needRunOff
    #     return needRunOff
    # else:
    while x < num_ballots:
        #print ballots[x]
        ballots[x].remove(loser)
        #print ballots[x]
        x = x + 1

    return ballots


lines = open('input2.txt').readlines()
lines = [line.strip() for line in lines]

cases = int(lines.pop(0))
for case in range(cases):

    # ignore blank line between cases
    lines.pop(0)

    # read candidates
    num_cand = int(lines.pop(0))
    candidates = lines[:num_cand]
    lines = lines[num_cand:]
    #print candidates

    # read ballots
    ballots = []
    while lines and lines[0]:
        ballot = [int(x) for x in lines.pop(0).split()]
        ballots.append(ballot)
    #print ballots

    # count ballots
    votes = [0 for candidate in candidates]
    for ballot in ballots:
        votes[ballot[0]-1] += 1
    #print votes

    # until 50%, do the elimination thing
    while getWinner(votes) is None:
        # do elimination round
        ballot = eliminate(votes)

        # if ballot == True:
        #     print candidates


        for ballot in ballots:
            votes[ballot[0]-1] += 1

        getWinner(votes)
    i = 0
    if getWinner(votes) == 2000:
        while i < len(votes):
            if votes[i] > 0:
                print "%s" % candidates[i]
            i = i + 1
    else:
        print "%s" % candidates[getWinner(votes)]
    print


    # def applyBallots()
