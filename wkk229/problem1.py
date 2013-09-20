import sys

print sys.argv

def  cycle(n):
	count =1
	while n!=1:
		if n%2==0:
			n=n/2
		else:
			n=n*3+1

		count +=1

	return count

def max_cycle(lower,upper):
	max=0
	for n in range(lower,upper+1):
		result=cycle(n)
		if result >max:
			max=result

	return max

print max_cycle(1,10)
