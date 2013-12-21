import csv
import numpy as np
import matplotlib.pylab as plt

zips = []
pop = []
incidents = []
with open("labeled_data.csv", 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        zipCode = float(row[0])
        population = float(row[1])
        numIncidents = float(row[2])
        zips.append(int(zipCode))
        pop.append(int(population))
        incidents.append(int(numIncidents))

p3 = np.poly1d(np.polyfit(pop, incidents, 3))
predictedValues = []

zipsUL = []
popUL = []
with open("unlabeled_data.csv", 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        zipCode = float(row[0])
        population = float(row[1])
        zipsUL.append(int(zipCode))
        popUL.append(int(population))

for row in popUL:
    prediction = p3(row)
    predictedValues.append(prediction)

with open('output.csv', 'w') as f:
    rows = csv.writer(f, delimiter = ',')
    rows.writerow(['zip', 'population', 'predicted value'])
    rows.writerows(zip(zipsUL, popUL, predictedValues))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(popUL, predictedValues, label = 'Predicted Values', marker = 's', s=1)
plt.xlabel('Population')
plt.ylabel('Predicted Number of Incidents')
fig.suptitle('Final OLS Model', size=16)
plt.legend()
plt.show()

'''The number of predicted incidents can be found in the file 'output.csv' '''
