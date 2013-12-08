import numpy as np

finput = open('ML1Dataset/labeled_data.csv','r')
finput.readline()
zip = []
pop = []
inc = []
for line in finput:
	tokens = line.split(',')
	zip.append(float(tokens[0]))
	pop.append(float(tokens[1]))
	inc.append(float(tokens[2]))
p = 3
coeffs = np.polyfit(pop,inc,p)

#Now make predictions
finput2 = open('ML1Dataset/unlabeled_data.csv','r')
finput2.readline()
foutput = open('predictions.txt','w')
zip2 = []
pop2 = []
for line in finput2:
	tokens = line.split(',')
	zip2.append(float(tokens[0]))
	pop2.append(float(tokens[1]))
inc2 = np.polyval(coeffs,pop2)
foutput.write("zip,incidents\n")
for i in range(0,len(zip2)):
	foutput.write(str(zip2[i])+","+str(inc2[i])+"\n")
