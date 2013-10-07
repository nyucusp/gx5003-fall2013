import Queue
import itertools
import string

openFile = open("input3.txt","r")
data = openFile.readlines()

raw_input=[]
for line in data:
    lines = line.strip('\n')
    raw_input.append(lines)

#Find the rows of the cases
data = raw_input[2:]
lineOfSpace = []
lineOfSpace.append(0)
i = 0
for line in data:
    if line[0].isdigit():
        lineOfSpace.append(i+1)
    i = i + 1
lineOfSpace.append(len(data))
numOfScenarios = int(raw_input[0])
lineOfSpace[numOfScenarios] = lineOfSpace[numOfScenarios]+1

def dicts():
    f = raw_input[lineOfSpace[i]+2:lineOfSpace[i]+papers+2]
    author_en = {} # Dictionary for erdos points and author
    coauthors = [] # list of authors that are written paper with Erdos

    targets = raw_input[lineOfSpace[i]+papers+2:lineOfSpace[i]+papers+names+2]
    
    for line in f:
        authortext,articles = line.split(':')
        authors = authortext.split(', ')
        authors = map(', '.join, zip(authors[::2], authors[1::2]))
        coauthors.append( authors )
        for author in authors:
            author_en[ author ] = 'Infinity'

    author_en['Erdos, P.'] = 0 # Special case

    for ca in coauthors: #find the authors that didn't write a paper with Erdos and calculate scores
        minima = 'Infinity'
        for a in ca:
            if author_en[a] != 'Infinity' and ( author_en[a]<minima or minima is 'Infinity' ): # We have a score
                minima = author_en[a]
        if minima != 'Infinity':
            for a in ca:
                if author_en[a] == 'Infinity':
                    author_en[a] = minima+1 # Lowest score of co-authors + 1
                    
    return  author_en, coauthors, targets, f, authors, authortext, articles

def result():    
    for author in targets:
        if author == "Erdos, P.":
            print "Erdos, P.: 0"
        elif author not in list(itertools.chain.from_iterable(coauthors)): #if author is not in author list 
            print author,' is not in the list'
        else:
            print "%s: %s" % ( author, author_en[author] )  


##Does it for all the cases
i = 0
while i < (numOfScenarios):
    print 'Scenario ',i+1
    nums = [int(s) for s in raw_input[lineOfSpace[i]+1].split() if s.isdigit()] #find number of authors
    papers = nums[0] #number of articles
    names = nums[1] #number of authors
    (author_en, coauthors, targets, f, authors, authortext, articles)=dicts()
    result()
    i=i+1

# WARNINGS
# No author name can start with a number. (Sounds reasonable)




