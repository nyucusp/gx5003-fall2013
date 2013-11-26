from datetime import datetime
from matplotlib import pyplot


# read data form dat file
inputFile = open('Hw1data/stocks.dat','r')
header = inputFile.readline()
date=[]
apsto=[]
mssto=[]

for line in inputFile:
        term = line.split(",")
        date.append(datetime.strptime(term[0],"%Y-%m"))
        if datetime.strptime(term[0],"%Y-%m")==datetime(2006,1,1,0,0):
                apbase=float(term[1])
                msbase=float(term[2])
        apsto.append(float(term[1]))
        mssto.append(float(term[2]))

#adjust the stock price based on the price in Jan 2006
apstoAdj=[]
msstoAdj=[]
for term in apsto:
        apstoAdj.append(term-apbase)

for term in mssto:
        msstoAdj.append(term-msbase)

#plot
fig = pyplot.figure(figsize=(4.7*3.13,2*3.13))
graph1 = fig.add_subplot(1,2,1)
graph2 = fig.add_subplot(1,2,2)

graph1.plot_date(date,apstoAdj,'.',ms=7,color='#E41A1C',ls='--',dashes=(3,2),label="Apple")
graph2.plot_date(date,msstoAdj,'.',ms=7,color='#377EB8',ls='--',dashes=(3,2),label="Microsoft")

graph1.set_ylim(-40,140)#Adjust the plot by setting the x axis limits
graph1.set_xlim(datetime(2005,10,1,0,0),datetime(2008,10,30,0,0))#Adjust the plot by setting the y axis limits
graph2.set_ylim(-40,140)#Adjust the plot by setting the x axis limits
graph2.set_xlim(datetime(2005,10,1,0,0),datetime(2008,10,30,0,0))#Adjust the plot by setting the y axis limits

graph1.grid(True)#Add the gridlines to make the plot clearer 
graph1.set_xlabel('Month',fontweight='bold')
graph1.set_ylabel('US Dollars',fontweight='bold')
graph2.grid(True)#Add the gridlines to make the plot clearer 
graph2.set_xlabel('Month',fontweight='bold')
graph2.set_ylabel('US Dollars',fontweight='bold')

graph1.set_title("Apple stock price relative to Jan 2006",fontsize=15)
graph2.set_title("Microsoft stock price relative to Jan 2006",fontsize=15)

fig.autofmt_xdate()#Automatically adjust the x tick labels to avoid overlap
fig.patch.set_facecolor('white') 

#output
pyplot.savefig('problem 1c.png', dpi=200)
pyplot.show()

"""
Comment:
I prefer superpostion to juxtaposition. It can be clearer to see the different trends of Apple's and Microsoft's stock prices in superpostion.In addition, we can tell the difference between their prices easily when they are superposed in the same graph.
"""





