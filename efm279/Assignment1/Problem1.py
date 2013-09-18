import sys

maxcount=1
first = int(sys.argv[1])
last  = int(sys.argv[2])

for i in range (first,last):
	j=i
	counter=1
	while j>1:
		if j%2==0:
			j=j/2
			
		elif j%2!=0:
			j=(j*3+1)
		counter=counter+1
		
	if counter>maxcount:
		maxcount=counter

print first,last,maxcount
