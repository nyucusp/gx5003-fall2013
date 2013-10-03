myFile = open('zipCodes.csv','r')
zd = {} #create a dictionary

firstline = 0 #pass the first line
for line in myFile:
	if firstline == 0:
		firstline = 1
	else:
		a = line.split(",") # split the line contents
		if a[10] != "\n": # ignored the zip codes with no population	
			population = float(a[10][:-1])
			area = float(a[7])
			density = population / area
			zipcode = a[1]
			zd[zipcode]=density 

zdzd= [] #create an array
for k in zd:
	zdzd.append((k,zd[k])) #put key and value of zd into this array
	
x = sorted(zdzd) #sorted by key(zipcode)

outputFile = open("output_density_problem.txt","w") #output the result in a file
for item in x:
	outputline = item[0]+" "+str(item[1])+"\n"
	outputFile.write(outputline)
outputFile.close()
