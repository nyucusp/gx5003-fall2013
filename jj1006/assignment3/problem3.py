def parsePaper(line):
#lines represents a paper
	authorlist = line.split(':')[0]
	atemp = authorlist.split(', ')
	#we guarantee there are always a first and last name
	authors = []
	for i in range(len(atemp)/2):
		authors.append(atemp[i*2]+", "+atemp[i*2+1])
	return authors

class authorGraph:
	neighbors={} #graphs wil be stored as a map to adjacency lists
	def addCoauthorList(self,authors):
		for a in authors:
			if not a in self.neighbors:
				self.neighbors[a]=[]
			for a2 in authors:
				if a2 not in self.neighbors[a] and not a2==a:
					self.neighbors[a].append(a2)
	
	def printNeighbors(self):
		print self.neighbors

	def distances(self, source):
		q = [source]
		d = {source:0} #distances
		color = {}
		for name in self.neighbors:
			color[name]=True
		color[source]=False
		while len(q)>0:
			u = q.pop(0)
			for v in self.neighbors[u]:
				if color[v]:
					color[v]=False
					q.append(v)
					d[v]=d[u]+1
		return d


finput = open('input3.txt')
nScenarios = int(finput.readline().rstrip())
for i in range(nScenarios):
	guide = finput.readline().split()
	nPapers = int(guide[0])
	nAuthors = int(guide[1])
	g = authorGraph()
	for p in range(nPapers):
		g.addCoauthorList(parsePaper(finput.readline()))
	print "Scenario "+str(i+1)
	enumbers = g.distances('Erdos, P.')
	for a in range(nAuthors):
		author = finput.readline().rstrip()
		if author in enumbers:
			print author+" "+str(enumbers[author])
		else:
			print author+" infinity"

