import sys

def isJolly(x):
	targets = (len(x)-1)*[False]

	for i in range(1,len(x)):
		diff = abs(int(x[i-1])-int(x[i]))
		if diff<len(x) and diff>0 and not targets[diff-1]: #will not crash because first clause will evaluate first
			targets[diff-1]=True
		else:
			print "Not jolly"
			return
	print "Jolly"
	return


x = sys.argv[2:len(sys.argv)]
isJolly(x)
