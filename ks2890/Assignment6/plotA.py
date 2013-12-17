import matplotlib.pyplot as plt
import numpy as np
import csv
import operator

# empty lists and the Counter for reading the file
pop = []
inc = []
zipcode = []
Counter = []
Number = 1

#opening the microprocessor data with csv
with open('labeled_data.csv', 'rb') as csvfile:
    incidents = csv.reader(csvfile, delimiter = ',') # separating out the file by the comma
    incidents.next() #skip the first line
    incidents = sorted(incidents, key = operator.itemgetter(1), reverse = False) # sort the results

    # reading through the file and appending items to the empty lists
    for row in incidents:
		zipcode.append(row[0])
		pop.append(float(row[1]))
		inc.append(float(row[2]))
		Counter.append(Number)
		Number = Number + 1

#print len(pop)
#print len(inc)

# creating the scatter plot
plt.scatter(pop, inc, marker = 'o', color = 'b')
plt.title('Incidents by Population per Zipcode',fontsize = 12)
plt.xlabel('Population', fontsize = 10)
plt.ylabel('Number of Incidents', fontsize = 10)

plt.show()