#Aliya Merali
#Assignment 3
#Problem 3

def get_authors(x):#expected input is raw data
    pass


#Find out the range of data for each case, given the raw data
def find_scenarios(x):
    caseBreak = []
    i = 0
    for line in x:
        if len(line) == 4:
            caseBreak.append(i)
        i = i + 1
    caseBreak.append(len(x))
    return caseBreak

#Loop through the cases, and in each case call the functions above to evaluate each scenario
 
input = open('input3.txt','r')
data = input.readlines()

cases = find_scenarios(data)
del(data[0])
j = 0
while j < (len(cases)-1):
    index = cases[j]
    papers = []
    P = data[index-1][0] #Number of papers listed
    papers_end = int(index) + int(P)  #end of  list of papers (# papers)
    authors_to_search = []
    N = data[index-1][2] #number of authors to search
    authors_end = int(papers_end)+ int(N) #end list of authors to search
    while ((cases[j]) <= index < papers_end):
        papers.append(data[index])
        index = index + 1
    while (papers_end <= index < authors_end):
        authors_to_search.append(data[index])
        index = index + 1
    #Created data in the form of 1 list of all papers, 1 list of authors to search for in papers
    j = j + 1
    print 'Scenario ' + str(j)
    print
    print 'Papers = ' + str(papers)
    print
    print 'Authors to Search = ' + str(authors_to_search)
    print
    print
