import Queue 
import string
import itertools 

openFile = open("input3.txt","r") #read text input3
content= openFile.readlines()
raw_input=[]
for line in content:
	lines = line.strip('\n')
	raw_input.append(lines)
#will find rows
content = raw_input[2:]
numScenario = int(raw_input[0])
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
		authwork, articles = line.split(':')
		authors=authwork.split(', ')
		authors = map(', '.join,zip(authors[::2],authors[1::2]))
		curAuthor.append (authors)
		for author in authors:
			authortx[author]= 'infinity'
	authortx['Erdos,p.'] =0 
	for ca in curAuthor: #authors with no Erods
		minima = 'infinity'
		for x in ca:
			if authortx[x] != 'infinity' and (authortx[x]<minima or minima is 'infinity'):#we have erdos number
				minima = authortx[x]
		if minima!= 'infinity':
			for x in ca:
				if authortx [x] == 'infinity':
					authortx [x]==minima+1 #low score
	return  authortx,curAuthor,targets,f,author,authwork,articles
def results():
	for author in targets:
		if author == "Erdos,p.":
			print "Erdos,p.: 0"
		elif author not in list(itertools.chain.from_iterable(curAuthor)):
			print author,'not erdos number'
		else:
			print "%s: %s" % (author ,authortx[author])
i=0
while i<(temp_list) and numScenario > 0:
	print "scenario" ,i+1

	nums = [int(s) for s in raw_input[temp_list[i]+1].split() if s.isdigit()]
	num_papers =nums[0] # article numbers
	names= nums[1] # authors numbers
	(authortx, curAuthor, targets, f, author ,authwork, articles)=dicts()
	results()
	i=i+1
	numScenario = numScenario - 1




