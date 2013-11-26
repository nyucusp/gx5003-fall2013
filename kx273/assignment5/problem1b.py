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
fig = pyplot.figure()
fig.suptitle("Apple and Microsoft stock price relative to Jan 2006",fontsize=15)

graph = fig.add_subplot(1,1,1)
graph.plot_date(date,apstoAdj,'.',ms=7,color='#E41A1C',ls='--',dashes=(3,2),label="Apple")
graph.plot_date(date,msstoAdj,'.',ms=7,color='#377EB8',ls='--',dashes=(3,2),label="Microsoft")

#improve the plot
graph.set_ylim(-40,140)#Adjust the plot by setting the x axis limits
graph.set_xlim(datetime(2005,10,1,0,0),datetime(2008,10,30,0,0))#Adjust the plot by setting the y axis limits
graph.legend(loc="upper left",shadow=False)
fig.autofmt_xdate()#Automatically adjust the x tick labels to avoid overlap
graph.grid(True)#Add the gridlines to make the plot clearer 
graph.set_xlabel('Month',fontweight='bold')
graph.set_ylabel('US Dollars',fontweight='bold')
fig.patch.set_facecolor('white') 

#output
pyplot.savefig('problem 1b.png', dpi=200)
pyplot.show()

"""
Conclusion:
The Microsoft's stock price fluctuate around the price of Jan 2006.
However the Apple's stock price kept booming since Jan 2006,except a slight drop initially.
"""
