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
        apsto.append(float(term[1]))
        mssto.append(float(term[2]))
      
#plot
fig = pyplot.figure()
fig.suptitle("Apple stock price (Jan 2006-Sep 2008)",fontsize=15)
graph = fig.add_subplot(1,1,1)
graph.plot_date(date,apsto,'.',ms=9,color='#E41A1C',ls='--',dashes=(3,2))

#improve the plot
graph.set_ylim(40,220)#Adjust the plot by setting the x axis limits
graph.set_xlim(datetime(2005,10,1,0,0),datetime(2008,10,30,0,0))#Adjust the plot by setting the y axis limits
fig.autofmt_xdate()#Automatically adjust the x tick labels to avoid overlap
pyplot.grid(True)#Add the gridlines to make the plot clearer 
graph.set_xlabel('Month',fontweight='bold')
graph.set_ylabel('US Dollars',fontweight='bold')
fig.patch.set_facecolor('white') 

#output
pyplot.savefig('problem 1a.png', dpi=200)
pyplot.show()





