import sys

myFile = open("input3.txt", "r")

nScenarios = int(myFile.readline())
PN = myFile.readline().split()
p = int(PN[0])
n = int(PN[1])

class Author():
    def __init__(self, name):
        self.name = name
        self.erdosNum = 1000

papers = []
for i in range (0, p):
    papers.append(myFile.readline())

authorDict = {}
citeList = []
for line in papers:
    newline = line.split('.:')
    for entry in newline:
        lines = entry.split('., ')
        if (lines[0][0] != ' '):
            citeList.append(lines)
            for i in range(0, len(lines)):
                newauthor = Author(lines[i])
                authorDict[newauthor.name] = newauthor.erdosNum

print 'Entries in papers:'
for line in citeList:
    print line
print ''


authors = []
for i in range (0, n):
    name = myFile.readline().strip('.\n')
    authors.append(name)

print 'Authors to find:'
for name in authors:
    print name
print ''


for line in citeList:
    if 'Erdos, P' in line:
        for x in range(0, len(line)):
            authorName = line[x]
            authorDict[authorName] = 1
    print ''

for y in range (0, p):
    for line in citeList:
        minErdos = authorDict[line[0]]
        for x in range(0, len(line)):
            if (authorDict[line[x]] < minErdos):
                minErdos = authorDict[line[x]]
        for x in range(0, len(line)):
            if (authorDict[line[x]] > minErdos):
                authorDict[line[x]] = minErdos + 1

for entry in authorDict:
    if (authorDict[entry] == 1000):
        authorDict[entry] = 'infinity'

'''print 'Entries in dictionary:'
for entry in authorDict:
    print entry, authorDict[entry]
print '''

print 'Scenario 1'
for name in authors:
    for entry in authorDict:
        if (str(entry) == str(name)):
            print entry, ". ", authorDict[entry]
