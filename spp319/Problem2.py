from sys import argv

#ask for sequence
#create list from sequence
#determine if jolly
#print jolly or not


def is_jolly(seq):
	absolute_values = []
	for i in range(len(seq)-1):
		diff = abs(seq[i] - seq[(i+1)])
		absolute_values.append(diff)
	absolute_values.sort()
	
	if absolute_values == range(1, len(seq)):
		return True
	else:
		return False

	

# get number of things in sequence
length = int(argv[1])

# get the sequence
seq = []
for i in range(2, length + 2):
	seq.append(int(argv[i]))


# determine if sequence is jolly
status = is_jolly(seq)


# if jolly, print jolly
if status:
	print "Jolly"
else:
	print "Not Jolly"