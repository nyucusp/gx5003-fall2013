import sys
print sys.argv

def absvalue(i,j):
	return abs(int(sys.argv[i])-int(sys.argv[j]))

n = int(sys.argv[1])

diff = []

for i in range(2, len(sys.argv)-1):
	value =  absvalue(i, i+1)
	diff.append(value)


for i in range(1, n):
	found = False
	for element in diff:
		if(i == element):
			found = True
	if(found == False):
		print "Not jolly"
		exit()

print "Jolly"
