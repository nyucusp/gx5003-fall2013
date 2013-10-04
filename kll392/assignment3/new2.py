import sys

myFile = open("input2.txt", "r")
n = int(myFile.readline())
myFile.readline()

nCand = int(myFile.readline())

class Candidate():
    totalvotes = None
    votelist = []
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.totalvotes = 0
    def addvote(self):
        self.totalvotes += 1

class Ballot():
    votelist = []
    def __init__(self, nCand):
        self.votelist = nCand*0

candidates = []

count = 0
while count < nCand:
    count += 1
    line = myFile.readline().strip('\n')
    tempperson = Candidate(line, count)
    candidates.append(tempperson)

i = 0

while (i <= (nCand*2 - 1)):
    for line in myFile:
        if (i != 0):
            print "you are here!"
        vote = int(line[i])
        print 'vote is ', vote
        j = 0
        for item in candidates:
            if (int(candidates[j].index) == vote):
                candidates[j].addvote()
                print candidates[j].name, " got a vote!"
            j += 1
    
    maxvotes = 0
    leaders = []
    num_deleted = 0
    for entry in candidates:
        if (entry.totalvotes >= maxvotes):
            maxvotes  = entry.totalvotes
            leaders.append(entry)
        elif (entry.totalvotes < maxvotes):
            b = candidates.index(entry)
            del candidates[b]
            num_deleted += 1

    i += 2
    nCand = nCand - num_deleted

for entry in candidates:
    print entry.name, entry.totalvotes
for line in leaders:
    print line.name, line.totalvotes

#print 'new line'


