def recfinder(word,grid,x,y,dx,dy):
	if word=='':
		return True
	if x>=0 and y>=0 and x<len(grid[0]) and y<len(grid) and word[0]==grid[y][x]:
		return recfinder(word[1:len(word)],grid,x+dx,y+dy,dx,dy)
	return False

def finder(word,grid):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if recfinder(word,grid,x,y,1,0) or \
			   recfinder(word,grid,x,y,-1,0) or \
			   recfinder(word,grid,x,y,0,1) or \
			   recfinder(word,grid,x,y,0,-1) or \
			   recfinder(word,grid,x,y,1,1) or \
			   recfinder(word,grid,x,y,-1,1) or \
			   recfinder(word,grid,x,y,1,-1) or \
			   recfinder(word,grid,x,y,-1,-1):
				return (y+1,x+1)
	return (0,0)


finput = open('input4.txt','r')
numPuzzles = int(finput.readline().rstrip())
for i in range(numPuzzles):
	finput.readline() #blank line
	nrows = int(finput.readline().split()[0])
	grid = []
	for r in range(nrows):
		grid.append(finput.readline().lower().rstrip())
	nwords = int(finput.readline().rstrip())
	for w in range(nwords):
		loc = finder(finput.readline().lower().rstrip(),grid)
		print str(loc[0])+" "+str(loc[1])
	print
