def count(voters, names):
	#voters is sorted list of voter preferences
	counts = []
	for n in names:
		counts.append([0, n])
	for v in voters:
		#search for name and add one vote
		for n in counts:
			if v[0][1]==n[1]:
				n[0]=n[0]+1
	return sorted(counts)[::-1]

def pruned(voters, rname):
	#rname is name to be removed
	newvoters = []
	for v in voters:
		for i in range(len(v)):
			if v[i][1]==rname:
				v.pop(i)
				break
		newvoters.append(v)
	return newvoters

def vote(names, prefs):
	#names is array of names, prefs is matrix of preferences
	voters = []
	for p in prefs:
		vtemp = []
		for i in range(len(p)):
			vtemp.append([p[i],names[i]])
		voters.append(sorted(vtemp))
	while len(names)>1:
		rank = count(voters,names)
		voters = pruned(voters,rank[len(rank)-1][1])
		names.pop(names.index(rank[len(rank)-1][1]))
	return names[0]


finput = open('input2.txt','r')
ninputs = int(finput.readline().rstrip())
finput.readline() #get rid of blank line
for i in range(ninputs):
	ncandidates = int(finput.readline().rstrip())
	names = []
	for n in range(ncandidates):
		names.append(finput.readline().rstrip())
	votes = []
	line=finput.readline()
	while not line in ['\n','\r\n'] and not not line:
		votes.append([int(numeric_string) for numeric_string in line.split()])
		line=finput.readline()
	print vote(names,votes)
	print
