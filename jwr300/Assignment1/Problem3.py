import sys

def main(argv):
	
	#print sys.argv[1]
	lines = sys.argv[1]
	M = int(lines[0][0])
	print M #development tracker for rows
	N = int(lines[2][0])
	print N #development tracker for columns

	inputList = lines.split('\\n')
	print inputList

	#pass the multi-input single array into a dictionary with key value pair as index
	i = 1
	values = []
	keys = []
	while i < (M+1):
		j = 0
		while j < N:
			print inputList[i][j]
			values.append(inputList[i][j])
			print i,j
			keys.append((i,j))
			j = j + 1
		i = i + 1


	print keys
	print values

	#build dictionary using dict function
	dictionary = dict(zip(keys, values))

	print dictionary

if __name__ == "__main__":
	main(sys.argv)
