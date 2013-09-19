import sys

#print sys.argv

jolly = True

n = int(sys.argv[1])

def absdiff(i,j):
	#print int(sys.argv[i]), int(sys.argv[j])
	return abs(int(sys.argv[i]) - int(sys.argv[j]))

diff = []

for i in range(2, len(sys.argv)-1):
	value = absdiff(i,i+1)
	diff.append(value)
	
for i in range(1,n):
	if i not in diff:
		jolly = False


if jolly == False:
	print "Not Jolly"
else: 
		print "Jolly"


