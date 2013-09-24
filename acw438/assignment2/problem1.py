import sys
from datetime import datetime

class Commit:
    comHash = ""
    comTime = ""
    comAuth = ""

    def __init__(self, comHash):
        self.comHash = comHash

    def setTime(self, comTime):
        self.comTime = datetime.strptime(comTime, "%a %b %d %H:%M:%S %Y")
    
    def setAuth(self, comAuth):
        self.comAuth = comAuth

    def isAfter(self, cutoff):
        return self.comTime > cutoff

cutoff = datetime.strptime(sys.argv[1], "%m/%d/%Y %H:%M:%S")

comLog = open("logAfterAssignment1.txt", 'r')

lookCom = 1
lateTimes = []
for line in comLog:
    if lookCom == 1:
        indexOfCommit = line.find("commit")
        if indexOfCommit == 0:
            tempCom = Commit(line[:-1])
            lookCom = 0
    else:
        indexOfTime = line.find("Date:")
        indexOfAuthor = line.find("Author:")
        if indexOfTime == 0:
            tempCom.setTime(line[8:-7])
            if tempCom.isAfter(cutoff):
                #print "Found a late submission"
                lateTimes.append(tempCom)
            lookCom = 1
        if indexOfAuthor != -1:
            tempCom.setAuth(line[:-1])

#print tempCom.comTime
#print cutoff
for line in lateTimes:
    print "Late submission:"
    print "-", line.comHash
    print "-", line.comAuth
    print "-", line.comTime
    print " "

comLog.close()
