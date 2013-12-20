import matplotlib.pyplot as plt

cfile = open('labeled_data.csv','r')
header = cfile.readline()

popl = []
incd = []
zipc = []     graph

for line in cfile:
	cd_data = line.split(",")
	zipc.append(cd_data[0])
	popl.append(int(float(cd_data[1])))
	incd.append(int(float(cd_data[2])))
cfile.close()

# Zip Code vs Incidents Plotting
fig, ax = plt.subplots()
cdplot = fig.add_subplot(1,1,1)
cdplot.plot(zipc,incd,'.',ms=5,color='orange', label = 'No. of Incidents')
plt.title("Zip Code Vs Incidents", fontsize = 15)
plt.xlabel("Zip Code", fontsize = 15)
plt.ylabel("Incidents", fontsize=15)

plt.legend(loc = 'upper right')
plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.savefig('problemA1.png')
plt.show()

# Population Vs Incidents Plotting
fig, ax = plt.subplots()
cdplot = fig.add_subplot(1,1,1)
cdplot.plot(popl,incd,'.',ms=5,color='Green', label = 'No. of Incidents')
plt.title("Population Vs Incidents", fontsize = 15)
plt.xlabel("Population", fontsize = 15)
plt.ylabel("Incidents", fontsize=15)

plt.legend(loc = 'upper right')
plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.savefig('problemA2.png')
plt.show()
