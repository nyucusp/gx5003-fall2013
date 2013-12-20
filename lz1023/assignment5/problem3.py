import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

myfile=open('microprocessors.dat','r')
readdata=[]
for line in myfile:
    readdata.append(line)
processor=[]
year=[]
transistors=[]

for i in range(1,len(readdata)):
    processor.append(readdata[i].split(",")[0])
    year.append(readdata[i].split(",")[1])
    transistors.append(float(readdata[i].split(",")[2]))
    year=sorted(year)
    tran=np.log10(transistors)


for j in range(0,len(year)):
    for k in readdata:
        if year[j]==k.split(",")[1]:
            processor[j]=k.split(",")[0]
            tran1=float(k.split(",")[2])
            tran_log=np.log10(tran1)
            tran[j]=tran_log
count=[i for i in range(0,len(year))]
count1=[' 'for i in range(0,len(year))]

    
chart=plt.figure()

plot1=plt.subplot(1,2,1)
plot1.set_title('Year of Introduction',fontsize=12)
plot1.plot(year,count,'bo',color='g')
plot1.set_xlabel('Year')
plt.yticks(range(len(processor)),processor)
plot1.yaxis.grid()
plot1.tick_params(axis='both',direction='out')
plot1.axis([1965,2008,-1,13])
plt.setp(plot1.get_xticklabels(), rotation=45, fontsize=8)
plt.setp(plot1.get_yticklabels(), fontsize=8)

plot2=plt.subplot(1,2,2)
plot2.set_title('Number of Transistors',fontsize=12)
plot2.plot(tran,count,'bo',color='r')
plot2.set_xlabel('Transistors')
plt.yticks(range(len(count1)),count1)
plot2.yaxis.grid()
plot2.tick_params(axis='both',direction='out')
plot2.axis([2,10,-1,13])
plt.subplots_adjust(left =0.2)

    

plt.show()