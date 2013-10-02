fzipcodes = open('zipCodes.csv','r')
fout = open('output_density_problem2.txt','w')
zipdict = {}
for line in fzipcodes:
	tokens = line.replace('\n','').split(',')
	if tokens[10].isdigit():
		zipdict[tokens[0]] = float(tokens[10])/float(tokens[7])
zips = zipdict.keys()
for z in sorted(zips):
	fout.write(z+"\t"+str(zipdict[z])+"\n")
