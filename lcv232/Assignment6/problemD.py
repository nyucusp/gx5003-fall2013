import matplotlib.pyplot as plt
import numpy as np
import csv


cfile = open('labeled_data.csv','r')
header = cfile.readline()

popl = []
zipc = []
incd = []

for line in cfile:
	cd_data = line.split(",")
	zipc.append(cd_data[0])
	popl.append(int(float(cd_data[1])))
	incd.append(int(float(cd_data[2])))
cfile.close()

cfile = open('unlabeled_data.csv','r')
header = cfile.readline()

popl_pred = []
for line in cfile:
	cd_data = line.split(",")
	popl_pred.append(int(float(cd_data[1])))
cfile.close

coeff = np.polyfit(popl,incd,3)
cfit = np.poly1d(coeff)
incd_pred = cfit(popl_pred)

with open('output.csv', 'w') as f:
    rows = csv.writer(f, delimiter = ',')
    rows.writerow(['Zip Code', 'Population', 'Predicted Incidents'])
    rows.writerows(zip(zipc, popl, incd_pred))

fig = plt.figure()
graph = fig.add_subplot(1,1,1)
plt.title("OSL - unlabeled Data", fontsize = 15, fontweight='bold')

# Plotting & nomenclature of the x & y axes of the data that is plotted
graph.plot(popl,incd,'.',ms=5,color='blue', label = 'Observed')
graph.plot(popl_pred,incd_pred,'.',ms=5,color='red', label = 'Predicted')

plt.xlabel("Population", fontsize = 15)
plt.ylabel("Predicted Incidents", fontsize=15)

plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.legend(loc = 'upper left', prop={'size':12})

plt.savefig('problemD.png')
plt.show()
