import csv
myFile = open('zipCodes.csv')
reader = csv.reader(myFile)
reader.next()
output = open('output2.txt', 'w')

pop_dense = []

for row in reader:
	if row[10] != '':
		zipcode = row[1]
		area = row[7]
		population = row[10]
		density = int(population)/float(area)
		outline = zipcode +" " +str(density)+"\n"
		pop_dense.append(outline)
		#output.write(outline)
pop_dense.sort()
for line in pop_dense:
	output.write(line)

myFile.close()
output.close()