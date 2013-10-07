#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 3
"""
For every scenario this script prints a line containing a string "Scenario i" 
(where i is the number of the scenario) and the author names together with their 
Erdos number of all authors in the list of names. The authors appears in 
the same order as they appear in the list of names. The Erdos number is based on 
the papers in the paper database of this scenario. Authors which do not have any
 relation to Erdos via the papers in the database have Erdos number "infinity."
"""

import Queue

"""
method calcualtes thre erdos number and returns a dictionary with the author as 
key erdos number as value
"""
def erdosNum_calc(adjacent_list):
    erdosNum = {}
    queue = Queue.Queue()
    queue.put(('Erdos, P.', 0))
    while not queue.empty():
        (current_author, distance) = queue.get()
        if current_author not in erdosNum:
            erdosNum[current_author] = distance
        for author in adjacent_list[current_author]:
            if author not in erdosNum:
                queue.put((author, distance+1))
    return erdosNum

def main():
    myFile = open('input3.txt','r')
    numScenarios = int(myFile.readline())
    for current_scenario in range(1, numScenarios+1):
        [num_papers, numQueries] = [int(num) for num in myFile.readline().split()]
        adjacent_list = {}
        for _ in range(num_papers): #splits the papers into respective authos and joins on first and last name
            paper = myFile.readline()
            [authors, title] = paper.split(':')
            authors = [author.strip() for author in authors.split(',')]
            authors = [', '.join(first_last) for first_last in zip(authors[::2], authors[1::2])]

            # Build the adjacenct list of all the authors
            for author in authors:
                author_neighbors = adjacent_list.get(author,set())
                for coauthor in authors:
                    if coauthor == author:
                        continue
                    author_neighbors.add(coauthor)
                adjacent_list[author] = author_neighbors #create a list of lists for each author

        erdosNum = erdosNum_calc(adjacent_list)

        print 'Scenario %d' % current_scenario
        for i in range(numQueries):
            author = myFile.readline().strip()
            print "%s %s" % (author,erdosNum.get(author,'infinity'))
    myFile.close()


if __name__=='__main__':
    main()