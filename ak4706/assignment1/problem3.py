import sys
lines = sys.argv[1]
lnspl = lines.split('\\n')

#spliting the input into lines and taking the first line to be the size of the matrix
size = lnspl[0]. split(' ')
m = int(size[0])
n = int(size[1])

x=0
y=1

#writing 'Field #' before the output comes out 
if (lnspl[x][0]=='.' or lnspl[x][0]=='*'):
	x = x+1
else:
	print 'Field # ' + str(y)
	y=y+1
	x=x+1

#defining a function 'cellcount' to count the mines around a given cell
def cellcount(i,j):
	if i<1 or j<0 or i>n or j>=m:
		return 0
	if 	lnspl[i][j] == '*':
		return 1
	else:
		return 0

#Now you need to loop through each cell and apply the given function to that cell.
#If there is a mine around that cell it will add one to the count, 
#so that when it returns the count it will have the number of mines around that cell
#and if it is a mine it will return a mine.
#used the print count after each line to test where my program was going wrong

x = 1
while x<=n:
	y = 0
	while y<m:
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