############################################################################
#PROBLEMS B AND C
########################################################################3


import matplotlib.pyplot as plt
import numpy as np
import csv
RMSE = {}
RR = {}
FOLDS = 10




def main():
        zipcodes = []
        population = []
        numIncidents = []
	polyValues = []
        data = open("labeled_data.csv", 'rb')
        dataHolder = csv.reader(data)


####################################################################################
#PROBLEM B
##################################################################################

	rsme = []
	rr = []
	rsmeIndivid = 0
        #ignore headers
        next(dataHolder, None)
        for line in dataHolder:
                zipcodes.append(float(line[0]))
                population.append(float(line[1]))
                numIncidents.append(float(line[2]))
	
	sectionLength = len(numIncidents)/FOLDS
	
	#runs 5 times for the 5 orders
	for i in range(5):
	#make trainers and validation arrays:
		for k in range(9):
			incidentTrainer = numIncidents[k*sectionLength:sectionLength*(k+1)] 	
			populationTrainer = population[ 
k*sectionLength:sectionLength*(k+1)]
			incidentTester = numIncidents[k:sectionLength]
			populationTester = population[k:sectionLength]
			polyEvaluated = np.poly1d(np.polyfit(populationTrainer, incidentTrainer, i))		
############################
#calculate RMSE
###########################
			for j in populationTester:
				polyVal = polyEvaluated(j)
				polyValues.append(polyVal)
			for r in range(0, len(incidentTester)):
				temp = (incidentTester[r] - polyValues[r])**2
				rsmeIndivid = rsmeIndivid+temp
			rsme.append(float(np.sqrt(rsmeIndivid/(len(incidentTester)-1))))
		avg = np.mean(rsme)
		RMSE[i]=avg

#############################
#calculate R squared
#############################
		tempTotal = 0
		polyEq = np.polyfit(population, numIncidents,i)	
		temp2 = np.poly1d(polyEq)
		solver = temp2(population)
		numInAvg = np.sum(numIncidents)/len(numIncidents)
		ti = np.sum((numIncidents-numInAvg)**2)
		tp = np.sum((solver-numInAvg)**2)
		RR[i] = tp/ti

	#print RR
	#print RMSE

#######################################################################################################
#PROBLEM C
#####################################################################################################
	#(y-axis RMSE, x-axis order of polynomial)
	order = [1,2,3,4,5]
	rsmeArr = []
	for el in RMSE:
		rsmeArr.append(RMSE[el])
	plt.plot(order, rsmeArr)
        plt.title("Order of Polynomial vs RMSE")   
        plt.ylabel("RMSE")
        plt.xlabel("Order")              
        plt.show()
	




if __name__ == "__main__":
	main()
