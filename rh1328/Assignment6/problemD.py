import csv
import numpy as np



def main():
	zipcodes = []
	population = []
	numIncidents = []
	unlabeledZip = []
	unlabeledPop = []
	predictedInc = []

	unlabeledData = open('unlabeled_data.csv', 'rb')
	unlabeledHolder = csv.reader(unlabeledData)
	next(unlabeledHolder, None)
	
	for info in unlabeledHolder:
		unlabeledZip.append(float(info[0]))
		unlabeledPop.append(float(info[1]))	


	data = open("labeled_data.csv", 'rb')  
	dataHolder = csv.reader(data)
	 #ignore headers
	next(dataHolder, None)
	for line in dataHolder:
		zipcodes.append(float(line[0]))
		population.append(float(line[1]))
		numIncidents.append(float(line[2]))
	
	polyEval = np.polyfit(population, numIncidents, 3)
	predictedInc.append(np.polyval(polyEval, unlabeledPop))	
	correctList = []
	correctList = predictedInc[0]
	zipsInc = {}
	
	for count, zipper in enumerate(unlabeledZip):
		zipsInc[zipper] = correctList[count]
	
	print zipsInc

	for el in zipsInc:
		print el, zipsInc[el]


if __name__ == "__main__":
	main()
