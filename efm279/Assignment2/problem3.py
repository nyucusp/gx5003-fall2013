import csv

boro=csv.reader(open("boroughs.csv","rb"),delimiter=',')
b1=list(boro)
inci=csv.reader(open("Incidents_grouped_by_Address_and_Zip.csv","rb"),delimiter=',')
i2=list(inci)
zips=csv.reader(open("zipCodes.csv","rb"),delimiter=',')
z3=list(zips)

from collections import defaultdict

d1 = defaultdict(list)

for k, v in b1:
    d1[v].append(k)

d = dict((k, tuple(v)) for k, v in d1.iteritems())

incident={'Manhattan':0,'Bronx':0,'Brooklyn':0,'Queens':0,'Staten':0}
count=0
for u in d.keys():
    count=count+1
    incidentcount={}
    for w in d.values()[count-1]:
	temp=w
	for line in range(0,len(i2)):
		if i2[line][1]==temp:
			incident[u]=incident[u]+1


population={'Manhattan':0,'Bronx':0,'Brooklyn':0,'Queens':0,'Staten':0}
count=0
for u in d.keys():
    count=count+1
    incidentcount={}
    for w in d.values()[count-1]:
	temp=w
	for line in range(0,len(z3)):
		if z3[line][1]==temp:
			if (z3[line][10])!='':
				population[u]=population[u]+int(z3[line][10])



outputFile = open('output_problem3.txt','w')
for line in range(0,len(d.keys())):
		ratio=float(incident[d.keys()[line]])/float(population[d.keys()[line]])
	    	zipden= str(d.keys()[line]) + " " + str(ratio) + "\n"
	    	outputFile.write(zipden)
outputFile.close()




