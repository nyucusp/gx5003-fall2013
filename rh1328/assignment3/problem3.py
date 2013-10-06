
def handleInput(readem, numCases):
#reusable for different cases
	newCaseP = []
	newCaseN = []
        numCases = readem[0]
        p, n = readem[1].split(" ")     
        p = int(p)
	n = int(n)
	num = 0
	q = 0
#deletes num of cases and p,n
        del readem[0:2]
	while num < p:
		num += 1	
		newCaseP.append(readem[0].split(':')[0])
		del readem[0]
	while q < n:
		q += 1
		newCaseN.append(readem[0])
		del readem[0]
	makeGraph(newCaseP, newCaseN)


def makeGraph(relations, names):
#make dictionary of authors to use as graph for bfs search 
	temp = []
	num = 0
	graph = {}

	for name in relations:
		temp.append(name.split(".,"))
	#print temp

	while num < len(temp):
		#gets at list inside larger list
		listy = temp[num]
		for index in listy:
		#gets at individual names inside nested list
		#and removes white space
			index = index.strip()
			#remove periods because some are removed and some aren't with strip
			if index.endswith("."):
				index = index[:-1]
			for secondLoop in listy:
				secondLoop = secondLoop.strip()		
				if secondLoop.endswith("."):
					secondLoop = secondLoop[:-1]
				if secondLoop != index:
					if index not in graph:
						graph[index] = []
						graph[index].append(secondLoop)
					elif index in graph:
						graph[index].append(secondLoop)				
		num += 1
	
	for ites in names:
		ites = ites.rstrip("\n")
		if ites.endswith("."):
			ites = ites[:-1]
		bfs(graph, ites, 'Erdos, P')

def bfs(graph, beg, end):
	branches = []
	node = None
	branches.append([beg])
	while branches:
    		path = branches.pop(0)
		node = path[-1]
        	if node == end:			
            		print beg + ". " + str(len(path)-1)
			return 0
        	for children in graph.get(node, []):
            		newBranch = list(path)
			if children not in newBranch:
				newBranch.append(children)
            			branches.append(newBranch)
	print beg + ". " + "infinity"	


def main():
	thefile = open("input3.txt", "r")        
	readem = thefile.readlines()
        numCases = readem[0]
	
	handleInput(readem, numCases)

if __name__ == "__main__":
	main()
