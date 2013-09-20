import sys

n = int(sys.argv[1])

def full_list():
	full_list = []
	i = len(sys.argv) - 1 
	while i != 0:  
		full_list.append(int(sys.argv[i]))
		i = i - 1
	return full_list

def integer_list(n):
	integer_list = []
	while n != 0:
		integer_list.append(n)
		n = n - 1
	return integer_list

full_list = full_list() 
integer_list = integer_list(n)  

def jolly_jumper(full_list,integer_list):
	for val in full_list:
		if val in integer_list:
			return "Jolly! :)"
		return "Not jolly"

print jolly_jumper(full_list,integer_list)

