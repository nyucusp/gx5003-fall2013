import numpy as np
import matplotlib.pyplot as plt

myfile = open('genes.dat', 'r')
header = myfile.readline()
all_data = []
for line in myfile:
	temp_data = line.split(",")
	all_data.append([float(temp_data[0]),float(temp_data[1]),float(temp_data[2]),float(temp_data[3])])

inversed_data = zip(*all_data)
genes = ['A', 'B', 'C', 'D']
sequence = np.arange(0,1,0.01)

fig, graphArray = plt.subplots(4,4)

for i in range(0,4):
	for j in range(0,4):
		figure = graphArray[i,j]
		x = inversed_data[i]
		y = inversed_data[j]
		figure.plot(x,y,'.', color = 'grey', ms=5)
		figure.set_title("Gene "+genes[i]+" V.S. "+genes[j])

polycurve=graphArray[0,1]
x=inversed_data[0]
y=inversed_data[1]
coefficient = np.polyfit(x,y,5)
ycurve = np.polyval(coefficient, sequence)
polycurve.plot(sequence, ycurve, color = "red")

polycurve = graphArray[0,2]
x=inversed_data[0]
y=inversed_data[2]
coefficient = np.polyfit(x,y,1)
ycurve = np.polyval(coefficient, sequence)
polycurve.plot(sequence, ycurve, color = "red")

polycurve = graphArray[0,3]
x=inversed_data[0]
y=inversed_data[3]
coefficient = np.polyfit(x,y,3)
ycurve = np.polyval(coefficient, sequence)
polycurve.plot(sequence, ycurve, color = "red")
fig.tight_layout()
plt.savefig('Problem4.png')
plt.show()

