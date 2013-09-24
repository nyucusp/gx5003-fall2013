import sys

MAXCYCLE = 0

def findMaxCycle(i, j):
	for x in range(i,j+1):
		threenplusone(x)
	print str(i)+" "+str(j)+" "+str(MAXCYCLE)	 
		

def threenplusone(i):
	count=0
	while (i>1):
		count += 1
		if (i%2==0):
			i=i/2
		elif (i%2==1):
			i=(i*3)+1
	if (i==1):
		count+=1
	global MAXCYCLE
	if (count>MAXCYCLE):
		MAXCYCLE=count


def main():
	try:
		i = int(sys.argv[1])
		j = int(sys.argv[2])
	except:
		print "that's not an int"
		sys.exit(0)
	if (i>0 and i< 1000000 and j<1000000 and j>0):
		findMaxCycle(i, j)
	else:	
		print "not valid input"

if __name__=="__main__":
	main()	
