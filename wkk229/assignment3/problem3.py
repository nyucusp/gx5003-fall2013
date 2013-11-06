#problems - extracting the data (names and authors) from the text 
# problem2-calculating  the Erdos number.
import Queue 
import string
import itertools 
#I am going to use queue data structure to store intermediate results asI transverse th egraph as follows:
#Enqueue the root node
#dequeue a node to examine it
#if the author sought is found in the node,I will quite and return the results
#otherwise enqueue any successors
#-if the queue is empty , every node on the graph has been examines-I will quite the reserach and return"not found"
#if the queue is not empty ,I will repeat step2.
openFile = open("input3.txt","r")
content= openFile.readlines()
raw_input=[]
for line in content:
	lines = line.strip('\n')
	raw_input.append(lines)
#finding the rows of  the case
content = raw_input[2:]
numScens = int(raw_input[0])
temp_list= []
temp_list.append(0)
i=0

for line in content:
	if line[0].isdigit():
		temp_list.append(i+1)
		i = i+1
	temp_list.append(len(content))
	num_scenario= int(raw_input[0])
	temp_list[num_scenario] = temp_list [num_scenario]+1

def dicts():
	f = raw_input[temp_list[i]+2:temp_list[i]+num_papers+2]
	authortx= {}
	curAuthor=[]

	targets = raw_input[temp_list[i]+num_papers+2:temp_list[i]+num_papers+names+2]

	for line in f:
		authorwork, articles = line.split(':')
		authors=authorwork.split(', ')
		authors = map(', '.join,zip(authors[::2],authors[1::2]))
		curAuthor.append (authors)
		for author in authors:
			authortx[author]= 'infinity'
	authortx['Erdos,p.'] =0 # when you what to be effecient
	for ca in curAuthor: #finding authors who did not write anything with Erdos
		minima = 'infinity'
		for x in ca:
			if authortx[x] != 'infinity' and (authortx[x]<minima or minima is 'infinity'):#we have erdos number
				minima = authortx[x]
		if minima!= 'infinity':
			for x in ca:
				if authortx [x] == 'infinity':
					authortx [x]==minima+1#lowest score
	return  authortx,curAuthor,targets,f,author,authorwork,articles
def results():
	for author in targets:
		if author == "Erdos,p.":
			print "Erdos,p.: 0"
		elif author not in list(itertools.chain.from_iterable(curAuthor)):
			print author,'not erdos number'
		else:
			print "%s: %s" % (author ,authortx[author])
i=0
while i<(temp_list) and numScens > 0:
	print "scenario" ,i+1

	nums = [int(s) for s in raw_input[temp_list[i]+1].split() if s.isdigit()]
	num_papers =nums[0] #number of articles
	names= nums[1] # number of authors
	(authortx, curAuthor, targets, f, author ,authorwork, articles)=dicts()
	results()
	i=i+1
	numScens = numScens - 1




