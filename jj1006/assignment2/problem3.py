zip2bor = {}
fboroughs = open('boroughs.csv')
for line in fboroughs:
	tokens = line.replace('\n','').split(',')
	zip2bor[tokens[0]]=tokens[1]

fzipcodes = open('zipCodes.csv','r')
bor2pop = {'Bronx':0,'Staten':0,'Manhattan':0,'Brooklyn':0,'Queens':0}
for line in fzipcodes:
	tokens = line.replace('\n','').split(',')
	if tokens[10].isdigit() and tokens[0] in zip2bor:
		bor2pop[zip2bor[tokens[0]]] = bor2pop[zip2bor[tokens[0]]]+int(tokens[10])

print bor2pop

bor2inc = {'Bronx':0,'Staten':0,'Manhattan':0,'Brooklyn':0,'Queens':0}
finc = open('Incidents_grouped_by_Address_and_Zip.csv','r')
for line in finc:
	z = line.split(',')[1]
	if len(z)>0 and z in zip2bor:
		bor2inc[zip2bor[z]] = bor2inc[zip2bor[z]]+1
print bor2inc	
	
fout = open('output_problem3.txt','w')
bors = bor2inc.keys()
for b in sorted(bors):
	fout.write(b+"\t"+str(bor2inc[b]/float(bor2pop[b]))+"\n")
