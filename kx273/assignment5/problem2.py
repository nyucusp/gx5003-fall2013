from datetime import datetime
from matplotlib import pyplot
from matplotlib import mlab

# read data form dat file
inputFile = open('Hw1data/actions-fall-2007.dat','r')
header = inputFile.readline()
date=[]
dayDiff=[]
ddline=[]

base=datetime.strptime("2007-09-09 12:00:00","%Y-%m-%d %H:%M:%S") #use the first day as the base
for line in inputFile:
    item=line[0:19]
    date.append(datetime.strptime(item,"%Y-%m-%d %H:%M:%S"))
    dayDiff.append((datetime.strptime(item,"%Y-%m-%d %H:%M:%S")-base).total_seconds()/(3600*24))#convert datetime variabe to number of days away from the base


dueDate=["2007-09-18 12:00:00","2007-10-04 12:00:00","2007-10-25 12:00:00","2007-11-27 12:00:00","2007-12-15 12:00:00","2007-12-11 12:00:00"]

for item in dueDate:
    ddline.append((datetime.strptime(item,"%Y-%m-%d %H:%M:%S")-base).total_seconds()/(3600*24))

#plot the histogram
fig = pyplot.figure(figsize=(4.5*3.13,2*3.13))
fig.suptitle("Actions of Scientific Visualization Course (2007 Fall)",fontsize=15)

graph = fig.add_subplot(1,1,1)
histo = graph.hist(dayDiff, bins=range(0,101,1), facecolor='b')
graph.set_xlabel('Time',fontweight='bold')
graph.set_ylabel('Action Frequency (per 24 hours)',fontweight='bold')
graph.set_xlim(-1,101)
graph.set_ylim(0,15000)
graph.xaxis.set_ticks_position('bottom')
graph.set_xticklabels(['Sep','Oct','Nov','Dec'])
pyplot.xticks([7,37,67,97])


i=0
for item in ddline: 
    graph.axvline(x=item,color='r',ls='--')
    i+=1
    graph.text(item+0.5,14500,"Asn."+str(i)+" Due",rotation='vertical',fontsize=8,fontweight="bold")

graph.axvline(x=0,color='g',ls='--') #base
graph.text(0.5,8000,"Base Time: 2007-09-09 12:00:00",rotation='vertical',fontsize=8,fontweight="bold")

#fig.autofmt_xdate()
fig.patch.set_facecolor('white')

#output
pyplot.savefig('problem 2.png', dpi=200)
pyplot.show()

"""
Answers to the questions:
(a)I select 24-hours(from noon to noon) as the bins for this anslysis.Since the due time of all the assignments are at noon, so it is reseanable to choose the time 12:00:00 as the cutoffs.
(b)From the plot we can see, the closeer to the due day, the higher action frequencies there are. Therefore, we can hypothesize that the action frequency around the due date obey the noraml distibution.    
(c)The action frequency increased dramatically when approching the due date. The acction frequency 24-hours after the due date is really high as well.
"""


