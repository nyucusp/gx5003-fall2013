#Kara Leary
#Urban Informatics
#Assignment 3 - Problem 3

import sys

myFile = open("input3.txt", "r")

nScenarios = int(myFile.readline())

for nn in range (0, nScenarios):

    PN = myFile.readline().split()
    p = int(PN[0])
    n = int(PN[1])

    papers = []
    for i in range (0, p):
        papers.append(myFile.readline())

#authorDict holds a dictionary of all of the authors cited in the list of papers.  citeList holds a string of the names of authors who collaborated on a paper (i.e. Smith, M.N., Martin,G., and Erdos, P. in the sample input).  Finally, authors holds the names of the authors for whom we want to find the Erdos number.
    authorDict = {}
    citeList = []
    for line in papers:
        newline = line.split('.:')
        for entry in newline:
            lines = entry.split('., ')
            if (lines[0][0] != ' '):
                citeList.append(lines)
                for i in range(0, len(lines)):
                    newauthor = lines[i]
                    authorDict[newauthor] = 1000

    authors = []
    for i in range (0, n):
        name = myFile.readline().strip('.\n')
        authors.append(name)

#If authors collaborated directly with Erdos, set their Erdos number in the authorDict to 1:
    for line in citeList:
        if 'Erdos, P' in line:
            for x in range(0, len(line)):
                authorName = line[x]
                authorDict[authorName] = 1

#This loop determines the author with the lowest Erdos number who worked on any given paper.  It then sets all of the authors who worked with him to an Erdos number one greater than the lowest.  Because this depends on the order of papers read, I loop through it p times to ensure that the results are fully updated.
    for y in range (0, p):
        for line in citeList:
            minErdos = authorDict[line[0]]
            for x in range(0, len(line)):
                if (authorDict[line[x]] < minErdos):
                    minErdos = authorDict[line[x]]
            for x in range(0, len(line)):
                if (authorDict[line[x]] > minErdos):
                    authorDict[line[x]] = minErdos + 1
#If the author's erdos number has not been modified at all (is still 1000, as I set it initially), I set their Erdos number to 'infinity'
    for entry in authorDict:
        if (authorDict[entry] == 1000):
            authorDict[entry] = 'infinity'

    print 'Scenario ', nn + 1
    for name in authors:
        for entry in authorDict:
            if (str(entry) == str(name)):
                print entry, ". ", authorDict[entry]

myFile.close()
