#Katherine Elliott
#ke638
#Assignment 3 Problem 3

inputFile = open("input3.txt", "r")

num_scenarios = int(inputFile.readline())

for n in range (0, num_scenarios):

    PN = inputFile.readline().split()
    P = int(PN[0])
    N = int(PN[1])

    papers = []
    for i in range (0, P):
        papers.append(inputFile.readline())

#create dictionary of all authors
    author_dict = {}
    author_list = [] #authors with an Erdos number
    for line in papers:
        newline = line.split('.:')
        for entry in newline:
            lines = entry.split('., ')
            if (lines[0][0] != ' '):
                author_list.append(lines)
                for i in range(0, len(lines)):
                    newauthor = lines[i]
                    author_dict[newauthor] = 1000

    authors = []# authors to find Erdos number
    for i in range (0, N):
        name = inputFile.readline().strip('.\n')
        authors.append(name)

#set authors with Erdos number 1 as 1
    for line in author_list:
        if 'Erdos, P' in line:
            for x in range(0, len(line)):
                author_name = line[x]
                author_dict[author_name] = 1

#Determines lowest Erdos number of paper and adds 1 to other authors on that paper
    for y in range (0, P):
        for line in author_list:
            minErdos = author_dict[line[0]]
            for x in range(0, len(line)):
                if (author_dict[line[x]] < minErdos):
                    minErdos = author_dict[line[x]]
            for x in range(0, len(line)):
                if (author_dict[line[x]] > minErdos):
                    author_dict[line[x]] = minErdos + 1
                    
    for entry in author_dict:#loop if no erdos number
        if (author_dict[entry] == 1000):
            author_dict[entry] = 'infinity'

    print 'Scenario ', n + 1
    for name in authors:
        for entry in author_dict:
            if (str(entry) == str(name)):
                print entry, ". ", author_dict[entry]

inputFile.close()