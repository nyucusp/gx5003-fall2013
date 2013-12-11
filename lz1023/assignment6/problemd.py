import matplotlib.pyplot as plt 
import numpy as np

readdata=[]
myfile = open('labeled_data.csv','r')
for line in myfile:
    readdata.append(line)
zip=[]
pop=[]
inc=[]

for i in range(1,len(readdata)):
    zip.append(readdata[i].split(",")[0])
    pop.append(float(readdata[i].split(",")[1]))
    inc.append(float(readdata[i].split(",")[2]))       
myfile.close()


readdata1=[]
myfile = open('unlabeled_data.csv','r')
for line in myfile:
    readdata1.append(line)
pop1=[]
for i in range(1,len(readdata1)):
    pop1.append(float(readdata1[i].split(",")[1]))
myfile.close()

# using degree 3 polynomial as the model
coeffs=np.polyfit(pop,inc,3)
p=np.poly1d(coeffs)
inc_predict=p(pop1)


chart=plt.figure()
chart=plt.subplot(1,1,1)
chart.set_title('Predicted incidents in unlabled data')
chart.plot(pop1,inc_predict,'o',label='predicted')
chart.plot(pop,inc,'o',color='y',label='observed')
chart.set_xlabel('Population')
chart.set_ylabel('Incidents')
chart.set_ylim(-10000,125000)
chart.set_xlim(-10000,120000)
chart.legend(loc='best')
chart.grid()

plt.show()
