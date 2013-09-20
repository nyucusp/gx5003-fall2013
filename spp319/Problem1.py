from sys import argv

i = int(argv[1])
j = int(argv[2])

def cycle_count(value):
	num_steps = 1

	while value != 1:
		num_steps += 1
		if value % 2 == 0:
			value = value / 2
		else:
		    value = value * 3 + 1

	return num_steps

counts = []

for value in range(i, j+1):
	count = cycle_count(value)
	counts.append(count)

print i, j, max(counts)