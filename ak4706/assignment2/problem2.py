import csv
file = open('zipCodes.csv')
csvreader = csv.reader(file, delimiter= ',')
count =0
for line in csvreader:
	if count > 0 and line[10] != '':
		print float(line[10])/float(line[7])
	count = count + 1