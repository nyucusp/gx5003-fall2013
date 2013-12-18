
import matplotlib.pyplot as plt
import numpy as np

myfile=open('genes.dat','r')
readdata=[]
for line in myfile:
    readdata.append(line)
gen=[[],[],[],[]]
for i in range(1,len(readdata)):
    gen[0].append(float(readdata[i].split(',')[0]))
    gen[1].append(float(readdata[i].split(',')[1]))
    gen[2].append(float(readdata[i].split(',')[2]))
    gen[3].append(float(readdata[i].split(',')[3]))
    
fig,chartarray=plt.subplots(4,4,figsize=(3*4,3*4))
for i in range(0,4):
    for j in range(0,4):
        chart=chartarray[i,j]
        x=gen[i]
        y=gen[j]
        chart.scatter(x,y,5)
        chart.set_xlim(-0.2,1.2)
        chart.set_ylim(-0.2,1.2)
        chart.xaxis.set_major_locator(plt.FixedLocator([0,0.25,0.5,0.75,1]))
        plt.setp(chart.get_xticklabels(), rotation=45,fontsize=10)
        chart.yaxis.set_major_locator(plt.FixedLocator([0,0.25,0.5,0.75,1]))
        plt.setp(chart.get_yticklabels(), fontsize=10)
        chart.grid()
chartarray[0,0].set_ylabel('A', rotation = 'horizontal')
chartarray[1,0].set_ylabel('B', rotation = 'horizontal')
chartarray[2,0].set_ylabel('C', rotation = 'horizontal')
chartarray[3,0].set_ylabel('D', rotation = 'horizontal')
chartarray[3,0].set_xlabel('A')
chartarray[3,1].set_xlabel('B')
chartarray[3,2].set_xlabel('C')
chartarray[3,3].set_xlabel('D') 


s=np.arange(0,1,0.01)


curve=chartarray[1,0]
coeff=np.polyfit(gen[1],gen[0],5)
ycurve=np.polyval(coeff,s)
curve.plot(s,ycurve,color='r')

curve=chartarray[2,0]
coeff=np.polyfit(gen[2],gen[0],1)
ycurve=np.polyval(coeff,s)
curve.plot(s,ycurve,color='r')

curve=chartarray[3,0]
coeff=np.polyfit(gen[3],gen[0],3)
ycurve=np.polyval(coeff,s)
curve.plot(s,ycurve,color='r')



plt.show()  