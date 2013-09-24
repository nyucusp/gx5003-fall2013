import sys

i = sys.argv[1] #number i
j = sys.argv[2] #number j

def number(n):
		for n in range(i,j): #range i & j
			print n 
		sequence = []
		
		if n % 2 == 0:   #number even, divide by 2
				return n/2
		else:			
				return n * 3 +1  #number odd, multiply by 3, add 1.

		while n > 1:
				sequence.append (n)  #function returns data (I googled it)

		else: 
				print n
