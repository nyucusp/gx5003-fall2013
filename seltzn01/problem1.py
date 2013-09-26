#Nathan Seltzer
#problem1.py

import sys
i = sys.argv[1]
j = sys.argv[2]

def something(n):
	for n in range(i,j):
		print n
	sequence = []
	if n % 2 == 0:
		return n/2
	else:
		return n * 3 + 1

	while n > 1:
		sequence.append(n)
	else:
		print n