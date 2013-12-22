import sys
lines = sys.argv[1]
lnspl = lines.split('\\n')

#defining a function 'cellcount' to count the mines around a given cell
def cellcount(i,j):
	if i<(1+p) or j<0 or i>(m+p) or j>=n:
		return 0
	if 	lnspl[i][j] == '*':
		return 1
	else:
		return 0

#writing 'Field #' before the output comes out 
#if (lnspl[x][0]=='.' or lnspl[x][0]=='*'):
#	x = x+1
#else:

# spliting the input into lines and taking the first line to be the size of the matrix
# a=0
# for line in lnspl:
# 	size = lnspl[a]. split(' ')	
# 	m = int(size[0])
# 	n = int(size[1])

#print m,n
x=0
y=1
p=x
c = 1

while (lnspl[x][0]!='.' or lnspl[x][0]!='*' or lnspl[p][0]!='0'):
	#print "hi"
	print 'Field # ' + str(c)
	a=0+int(p)
	#print p
	for line in lnspl:
		size = lnspl[a]. split(' ')	
		#print "hi"
		#print lnspl[a]
		m = int(size[0])
		n = int(size[1])
	y=y+1
	x=x+1

	#Now you need to loop through each cell and apply the given function to that cell.
	#If there is a mine around that cell it will add one to the count, 
	#so that when it returns the count it will have the number of mines around that cell
	#and if it is a mine it will return a mine.
	#used the print count after each line to test where my program was going wrong

	x = 1 + int(p)
	#print x,m,y,n
	while x<=m+p:
		y = 0
		while y<n:
			#print x,y
			count = 0
			count = count + cellcount(x-1,y-1)
			#print count
			count = count + cellcount(x-1,y)
			#print count
			count = count + cellcount(x-1,y+1)
			#print count
			count = count + cellcount(x,y+1)
			#print count
			count = count + cellcount(x+1,y+1)
			#print count
			count = count + cellcount(x+1,y)
			#print count
			count = count + cellcount(x+1,y-1)
			#print count
			count = count + cellcount(x,y-1)
			if lnspl[x][y]=='*':
				print '*',
			else:
				print count,
			y = y+1
		print
		x = x+1
	print
	x=x+1
	#print x
	p=x-1
	#print p
	c = c +1
	for line in lnspl:
		#print p
		size = lnspl[p]. split(' ')	
		if size[0]=='0':
			sys.exit(1)
		# if x>n:
		# 	#x = x+1
		# 	a = x
		# 	for line in lnspl:
		# 		size = lnspl[a]. split(' ')	
		# 		m = int(size[0])
		# 		n = int(size[1])
		# 		print "hi"