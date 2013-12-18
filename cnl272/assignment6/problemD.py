import numpy as np
import matplotlib.pyplot as plt
import csv

myflie = open('labeled_data.csv','r')
header = myflie.readline()
zipcodes = []
population = []
incidents = []

for line in myflie:
	temp_data = line.split(",")
	zipcodes.append(temp_data[0])
	population.append(int(float(temp_data[1])))
	incidents.append(int(float(temp_data[2])))
myflie.close()

myflie = open('unlabeled_data.csv','r')
header = myflie.readline()
population_predictor = []
for line in myflie:
	temp_data = line.split(",")
	population_predictor.append(int(float(temp_data[1])))
myflie.close

coefficient= np.polyfit(population,incidents,3)
fitting = np.poly1d(coefficient)
incidents_predictor=fitting(population_predictor) 

with open('output.csv', 'w') as f:
    rows = csv.writer(f, delimiter = ',')
    rows.writerow(['Zip Code', 'Population', 'Predicted Incidents'])
    rows.writerows(zip(zipcodes, population, incidents_predictor))

fig = plt.figure()
graph = fig.add_subplot(1,1,1)
plt.title("OSL in unlabeled Data", fontsize = 15, fontweight='bold')
#label the axes of x and y, add the title for the both graphs
graph.plot(population,incidents,'.',ms=5,color='blue', label = 'Observed Value')
graph.plot(population_predictor,incidents_predictor,'.',ms=5,color='red', label = 'Predicted Value')
plt.xlabel("Population", fontsize = 14)
plt.ylabel("Predicted Incidents", fontsize=14)
plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.legend(loc = 'upper left', prop={'size':11})

plt.savefig('problemD.png')
plt.show()
