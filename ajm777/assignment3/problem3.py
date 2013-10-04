#Aliya Merali
#Assignment 3
#Problem 3

#Create a function to extract the authors in a better format from lists
def get_paper_authors(papers): #expected input format: ['Smith, M.N., Martin, G., Erdos, P.: Title Name\n', 'Erdos, P., Reisig, W.: Title Name\n']
    authors_in_papers = []
    for paper in papers:
        temp = []
        temp = (paper.split('.:')[0])
        authors_in_papers.append(temp.split("., "))
    return authors_in_papers
        

#create a function to make lists of authors with each ergos number
def get_erdos(papers):#expected input is of format: ['Smith, M.N., Martin, G., Erdos, P.: Title Name\n', 'Erdos, P., Reisig, W.: Title Name\n']
    author_list = get_paper_authors(papers)
    erdos_1 = []
    erdos = {}
    for author in author_list:
        x = 0
        while x < len(author):
            if author[x] == 'Erdos, P':
                 erdos_1.append(author)
                 author_list.remove(author)
                 author_list.insert(0,[])
                 x = len(author)
            x = x + 1  
    for author in author_list:
        for erdos1 in erdos_1: #going through the elements with erdos num 1
            n = 1
            x = 0
            while x < len(author):
                if author[x] in erdos1: #If the author is in the list with EN 1
                    if n in erdos: #then create a spot for it in the dict under 1
                        erdos[n].append(author[x])
                    else:
                        erdos[n] = []
                        erdos[n].append(author[x])
                    author.remove(author[x])
                    if (n+1) in erdos: #and put the rest of the authors in EN 2
                        erdos[n+1].append(author)
                    else:
                        erdos[n+1] = []
                        erdos[n+1].append(author)
                    author_list.remove(author)
                    author_list.insert(x,[])
                    x = len(author) + 1
                    n = n + 1
                x = x + 1   
    erdos[1].append(erdos_1)#Add all values from erdos_1 into dict key 1
    n = 2
    for author in author_list: #now do total loop through rest of authors to see who is in bracket 3 on and infinity
        x = 0
        i = 0
        while x < len(author):
            if author[x] in erdos[n][i]:
                author.remove(author[x])
                if (n+1) in erdos:
                    erdos[n+1].append(author)
                else:
                    erdos[n+1] = []
                    erdos[n+1].append(author)
                author_list.remove(author)
                author_list.insert(x,[])
                x = len(author) + 1
                n = n + 1
            x = x + 1
        i = i + 1
    #now, all the elements left in the list of authors have edos number infinity
    erdos['infinity'] = author_list
    return erdos #dictionary of all authors and their Erdos numbers as keys


#Create a function to correlate the input names with their erdos num
def output(authors_to_search, erdos):
    for author in authors_to_search:
        name = author.strip()[:-1]
        enum = 0
        for n, vals in erdos.items():
            for elem in vals:
                if name in elem:
                    enum = n
                elif enum == 0:
                    for elem2 in elem:
                       if name in elem2:
                           enum = n 
        print str(name) + '. ' + str(enum)  


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
#Created data in the form of list of  papers, list of authors to search
    print 'Scenario ' + str(j+1)
    output(authors_to_search, get_erdos(papers))
    j = j + 1

