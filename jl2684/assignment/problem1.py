import sys

i = int(sys.argv[1])
j = int(sys.argv[2])

def collatz_cycle_length(n):
	collatz_list = [n]	
	while n != 1: 
		if n%2 == 0:
			n = n/2 
		else: 
			n = 3*n + 1
		collatz_list.append(n)
	cycle_length = len(collatz_list)
	return cycle_length

def max_cycle_length (i,j):
	collatz_cycle_list = [collatz_cycle_length(i)]
	while i != j:
		i = i + 1
		collatz_cycle_list.append(collatz_cycle_length(i))
	return max(collatz_cycle_list)


print str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' ' + str(max_cycle_length (i,j)) 
