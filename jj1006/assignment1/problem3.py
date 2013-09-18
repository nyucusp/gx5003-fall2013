import sys
from copy import deepcopy

def sweep(lines, findex): #takes in a field input (no header) an array of strings
	numrows = len(lines)
	numcols = len(lines[0])

	#stick lines into a bigger field with .s around the edges
	field = [(numcols+2)*'.']
	for line in lines:
		field.append('.'+line+'.')
	field.append((numcols+2)*'.')

	counts=deepcopy(lines)
	for i in range(0,numrows):
		counts[i]=list(counts[i])

	for i in range(1,numrows+1):
		for j in range(1,numcols+1):
			if not field[i][j]=='*':
				ctemp = 0
				ctemp = ctemp+int(field[i-1][j-1]=='*')
				ctemp = ctemp+int(field[i-1][j]=='*')
				ctemp = ctemp+int(field[i-1][j+1]=='*')
				ctemp = ctemp+int(field[i][j-1]=='*')
				ctemp = ctemp+int(field[i][j+1]=='*')
				ctemp = ctemp+int(field[i+1][j-1]=='*')
				ctemp = ctemp+int(field[i+1][j]=='*')
				ctemp = ctemp+int(field[i+1][j+1]=='*')
				counts[i-1][j-1]=str(ctemp)

	print "Field #"+str(findex)+":"
	for i in range(0,numrows):
		print ''.join(counts[i])
	print

raw = sys.argv[1]
lines = raw.split('\\n')
findex = 1 #field index number
while lines:
	header=lines.pop(0) #get rid of the header line
	numrows = int(header.split()[0])
	input = []
	for i in range(numrows):
		input.append(lines.pop(0))
	if numrows>0:
		sweep(input, findex)
	else:
		break
	findex = findex+1

