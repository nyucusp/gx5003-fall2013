#Alex Chohlas-Wood (acw438). Assignment 2, Problem 1.

import sys

#import dateutil module, which allows date strings to be parsed
from dateutil.parser import parse

#this Commit class helps collect information about each commit
class Commit:
    comHash = ""
    comTime = ""
    comAuth = ""

    #triggered when a commit is first found, which happens on the hash line
    def __init__(self, comHash):
        self.comHash = comHash

    #after finding a commit, this adds the time of the commit to the object
    def setTime(self, comTime):
        self.comTime = parse(comTime)
    
    #after finding a commit, this adds the author of the commit to the object
    def setAuth(self, comAuth):
        self.comAuth = comAuth

    #this allows comparison of the commmit time to a cutoff date
    def isAfter(self, cutoff):
        return self.comTime > cutoff

#open commit log
comLog = open("logAfterAssignment1.txt", 'r')

#acquire cutoff date, convert to datetime object
cutoff = parse(sys.argv[1])

#if input does not have timezone, assume -0400 displacement
from datetime import datetime
try:
    cutoff < datetime.now()
    cutoff = parse(sys.argv[1] + ' -0400')
except:
    pass

#lookCom says whether we are looking for a commit (1=yes, 0=no)
lookCom = 1

#set up list to collect overdue commit objects
lateTimes = []

#pass through lines in comLog:
for line in comLog:
    if lookCom == 1: #true if we are looking for commits
        indexOfCommit = line.find("commit")
        if indexOfCommit == 0: #true if "commit" is first word in line
            tempCom = Commit(line[:-1]) #create a new temporary Commit object
            lookCom = 0 #subsequent lines will not look for a commit
    else:
        indexOfTime = line.find("Date:")
        indexOfAuthor = line.find("Author:")
        if indexOfAuthor != -1: #if we find an author, add it to temp object
            tempCom.setAuth(line[:-1])
        if indexOfTime == 0: #if we find a time, add it to temp object
            tempCom.setTime(line[8:])
            #if this commit's time is after the cutoff:
            if tempCom.isAfter(cutoff):
                #add the temp Commit object to the list of overdue commits
                lateTimes.append(tempCom)
            #look for the next commit, and effectively discard tempCom
            lookCom = 1 

for line in lateTimes:
    print "Late submission:"
    print "-", line.comHash
    print "-", line.comAuth
    print "-", line.comTime
    print " "

comLog.close()
