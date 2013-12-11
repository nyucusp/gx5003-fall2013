#Plot the data and reason about any phenomena
#of interest you see (you should report it in a short text).


import matplotlib.pyplot as plt
import numpy as np
import csv


def main():
	zipcodes = []
	population = []
	numIncidents = []
	data = open("labeled_data.csv", 'rb')
	dataHolder = csv.reader(data)
	#ignore headers
	next(dataHolder, None)
	for line in dataHolder:
		zipcodes.append(float(line[0]))
		population.append(float(line[1]))
		numIncidents.append(float(line[2]))

	##uncomment following code to show population vs incidents
	##plt.plot(population, numIncidents, 'o')
	##plt.title("Population Vs Incidents")   
	##plt.ylabel("Incidents")
	##plt.xlabel("Population")		
	##plt.show()

	
	##uncomment following code to show zip vs incidents
	##plt.plot(zipcodes, numIncidents, 'o')
	##plt.title("Zipcodes Vs Incidents")
	##plt.ylabel("Incidents")
	##plt.xlabel("Zicodes")
	##plt.show()
	
	#uncomment following code to show zip vs population
	#plt.plot(zipcodes, population, 'o')
	#plt.title("Zipcodes vs Population")
	#plt.ylabel("Population")
	#plt.xlabel("Zipcodes")
	#plt.show()

if __name__ == "__main__":
	main()
