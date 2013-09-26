import csv

ifile  = open('zipCodes.csv', "rb")
reader = csv.reader(ifile)

store=[[0 for x in xrange(14)] for x in xrange(2451)] 
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            #print '%-8s: %s' % (header[colnum], col)
            #i=int(rownum)
            #j=int(colnum)
	    store[rownum][colnum]=str(col)
            colnum += 1
    #store[rownum][13]='0'        
    rownum += 1

ifile.close()

for index in range(1,len(store)-1):
	
	    if store[index][10] == '':
	    	store[index][11]=0
	    else: 
		store[index][11]=float(store[index][10])/float(store[index][7])

outputFile = open('output_density_problem2.txt','w')

for index in range(1,len(store)):
	    if ((store[index][1].find('H'))<0) and ((store[index][1].find('X'))<0):
	    	store[index][12]=int(store[index][1])
	    else:
		store[index][12]==0

def column(matrix, i):
    return [row[i] for row in matrix]


import numpy as np
count_array = np.array(store)
#count_array2=count_array[:][12].astype(int)

final=[0 for x in xrange(2451)] 
store_sorted=[0 for x in xrange(2451)] 
for t in range(0,len(np.argsort(column(store,12)))):
	final[t]=np.argsort(column(store,12))[t]

for y in range(0,len(final)):
	store_sorted[y] = store[final[y]]


for line in range(len(store)):
	    if store_sorted[line][11]!=0:
	    	zipden= str(store_sorted[line][1]) + " " + str(store_sorted[line][11]) + "\n"
	    	outputFile.write(zipden)
outputFile.close()

