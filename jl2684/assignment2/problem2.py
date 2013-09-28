
import csv
import sys


zipFile = open('/home/jeongki/Documents/zipCodes.csv', 'rb')
zipLine = csv.reader(zipFile)

ziplist =[]
arealist = []
poplist = []

for row in zipLine:
	zipcode = row[1]
	area = row[7]
	pop = row[10]
	ziplist.append(row[1].rstrip('\n'))
	arealist.append(row[7].rstrip('\n'))
	poplist.append(row[10].rstrip('\n'))

del ziplist[0]
del arealist[0]
del poplist[0]

arealistfloat = []
for item in arealist:
	float(item)
	floated = float(item)
	arealistfloat.append(floated)

poplistfloat = []


f = open("//home/jeongki/gx5003-fall2013/jl2684/assignment2/output_density_problem2.txt", 'w')
sys.stdout = f


i = 0
densitylist = []
while i < len(poplist):
	if poplist[i] != '':
		densityitem = float(poplist[i])/arealistfloat[i]
		densitylist.append(str(str(ziplist[i]) + ' ' + str(densityitem)))
		i += 1 
	else: 
		i += 1 

sorteddensitylist = sorted(densitylist, reverse=False)
print "\n".join(sorteddensitylist)


zipFile.close()