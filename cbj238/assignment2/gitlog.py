from datetime import datetime
from dateutil.parser import parse

class LogEntry:
    commitHash = ""
    author = ""
    email = ""
    date = ""
    message = ""

    def parseCommit(self, line):
        self.commitHash = line[6:].strip()

    def parseAuthor(self, line):
        emailStart = line.find('<')
        emailEnd = line.find('>')
        authorStart = line.find(':')

        self.author = line[authorStart+1:emailStart-1].strip()
        self.email = line[emailStart+1:emailEnd-1].strip()

    def parseDate(self, line):
        dateStart = line.find(':')
        self.date = parse(line[dateStart+1:])

    def appendMessage(self, line):
        self.message += line

    def __str__(self):
        rStr = ""
        rStr += self.commitHash + " | "
        rStr += self.author + " : <" + self.email + "> | "
        rStr += str(self.date) + " | \n"
        rStr += self.message

        return rStr

class GitLog:
    entryList = []

    def __init__(self, path):
        ''' The constructor takes the path as a parameter. When constructed,
        reads in the file, and parses it.'''

        self.parseLog(path)

    def parseLog(self, filePath):
        logFile = open(filePath, 'r')

        '''
         Messages have Four states: [commit, author, date, message]
        '''
        thisEntry = None
        for line in logFile:
            if line[0:6] == "commit":
                if thisEntry is not None:
                    self.entryList.append(thisEntry)
                thisEntry = LogEntry()
                thisEntry.parseCommit(line)
            elif line[0:7] == "Author:":
                thisEntry.parseAuthor(line)
            elif line[0:5] == "Date:":
                thisEntry.parseDate(line)
            else:
                thisEntry.appendMessage(line)

        # make sure we add the last one
        if thisEntry is not None:
            self.entryList.append(thisEntry)
        logFile.close()

    def showLog(self):
        for entry in self.entryList:
            print "==============================="
            print entry

    def getAuthorEntryCount(self):
        ret = {}
        for entry in self.entryList:
            if entry.author in ret.keys():
                ret[entry.author] += 1
            else:
                ret[entry.author] = 1

        return ret

    def getEntriesAfterDate(self, date):
        entriesAfterDate = [x for x in self.entryList if date < x.date.replace(tzinfo=None)]
        return entriesAfterDate
            
'''state = 0
commitDateTimes = []
for line in myFile:
    if state == 0: # look for the author line
        indexOfCollab = line.find(collabName)
        if indexOfCollab != -1: # found a commit from Collab
            state = 1
    else:
        indexOfDate = line.find("Date:")
        if indexOfDate != -1: # found date from the previous commit
            commitDateTimes.append(line)
            state = 0
'''
