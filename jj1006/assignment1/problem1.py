import sys

pathdict = {}

def rec(x):
	global pathdict
	#print x
	if x in pathdict:
		return pathdict[x]

	if x==1:
		pathdict[x]=1
	elif x%2==1: #x is odd
		pathdict[x] = 1+rec(3*x+1)
	else: #x is even
		pathdict[x] = 1+rec(x/2)
	return pathdict[x]


mini = int(sys.argv[1])
maxi = int(sys.argv[2])

pathlens = (maxi-mini+1)*[0]
for i in range(mini,maxi+1):
    pathlens[i-mini]=rec(i)

print sys.argv[1]+" "+sys.argv[2]+" "+str(max(pathlens))
