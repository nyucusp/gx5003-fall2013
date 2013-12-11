import matplotlib.pyplot as plt

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

# Scatter Diagram of Zip Code V.S. Incidents
fig, ax = plt.subplots()
graph = fig.add_subplot(1,1,1)
graph.plot(zipcodes,incidents,'.',ms=5,color='orange', label = 'Number of Incidents')
plt.xlabel("Zip Code", fontsize = 14)
plt.title("Zip Code V.S. Incidents", fontsize = 15)
plt.ylabel("Incidents", fontsize=14)

plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.legend(loc = 'upper right')
plt.savefig('ProblemA Zip Code V.S. Incidents.png')
plt.show()

#Scatter Diagram of Population V.S. Incidents
fig, ax = plt.subplots()
graph = fig.add_subplot(1,1,1)
graph.plot(population,incidents,'.',ms=5,color='Green', label = 'Number of Incidents')
plt.xlabel("Population", fontsize = 14)
plt.title("Population V.S. Incidents", fontsize = 15)
plt.ylabel("Incidents", fontsize=14)

plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.legend(loc = 'upper right')
plt.savefig('ProblemA Population V.S. Incidents.png')
plt.show()
