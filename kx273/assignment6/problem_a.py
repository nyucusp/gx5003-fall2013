from matplotlib import pyplot

# read data form dat file
inputFile = open('labeled_data.csv','r')
header = inputFile.readline()
zip=[]
pop=[]
inci=[]

for line in inputFile:
        term = line.split(",")
        zip.append(term[0])
        pop.append(int(float(term[1])))
        inci.append(int(float(term[2])))
inputFile.close()

fig = pyplot.figure()
fig.suptitle("Incident vs Population",fontsize=15)
graph = fig.add_subplot(1,1,1)
graph.plot(pop,inci,'.',ms=9,color='0.3')

fig.autofmt_xdate()#Automatically adjust the x tick labels to avoid overlap
pyplot.grid(True)#Add the gridlines to make the plot clearer 
graph.set_xlabel('Population',fontweight='bold')
graph.set_ylabel('Incident',fontweight='bold')
fig.patch.set_facecolor('white') 

pyplot.savefig('problem_a.png', dpi=200)
pyplot.show()

"""
Observed phenomena
Generally, the number of incidents is positively related to the number of population. However, there are some regions which have really low incident number.The posible reseaon can be that residents in those regions are not used to makeing 311 calls or the relevant records are missed.   


"""
