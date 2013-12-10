import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

zips = []
pop = []
incidents = []
with open("labeled_data.csv", 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        zipCode = float(row[0])
        population = float(row[1])
        numIncidents = float(row[2])
        zips.append(int(zipCode))
        pop.append(int(population))
        incidents.append(int(numIncidents))

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.scatter(pop, incidents, marker = 's', color = 'k', s = 1)
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation('30')
plt.xlabel('Population')
plt.ylabel('Number of Incidents')
plt.tick_params(axis='both', which='major', labelsize=8)

ax2 = fig.add_subplot(222)
ax2.scatter(pop, incidents, marker = "s", color = 'k', s = 1)
ax2.set_yscale('log')
plt.xlabel('Population')
plt.ylabel('Log(Number of Incidents)')
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation('30')
plt.tick_params(axis='both', which='major', labelsize=8)

ax3 = fig.add_subplot(223)
ax3.bar(zips, incidents)
plt.xlabel('Zip Code')
plt.ylabel('Number of Incidents')
for label in ax3.yaxis.get_ticklabels():
    label.set_rotation('30')
plt.tick_params(axis='both', which='major', labelsize=8)

ax4 = fig.add_subplot(224)
ax4.bar(zips, pop)
plt.xlabel('Zip Code')
plt.ylabel('Population')
for label in ax4.yaxis.get_ticklabels():
    label.set_rotation('30')
plt.tick_params(axis='both', which='major', labelsize=8)

plt.suptitle('311 Incidents by ZIP Code and Population', size = '20')

plt.show()

'''The four graphs I plotted for this part of the assignment show some interesting phenomena regarding the number of incidents and populations of a zip code.  The first plot shows a simple relationship between population and total number of incidents.  The data is split into two categories here.  One group shows a clear relationship between population and number of incidents.  As the population of a zip code increases, so does the number of incidents reported within that zip code.  The second group is comprised of all of the data points that lie at or near the level of zero incidents reported.  These locations do not seem to show any relationshp between the size of the population of a zip code and the number of incidents.  My first guess would be that these points represent zip codes that lie away from the city center, where there are very few complaints to begin with.  In these quieter neighborhoods, there are very few complaints regardless of the presence of larger populations.  The second graph shows the same phenomenon but on a logarithmic scale.  This plot shows even more clearly the difference between the two groups of data.  The third graph plots the numeric zip code against the total number of incidents in that zip code.  Although a zip code numerically does not hold much value, it is worth noting that the zip codes of New York City are sorted numerically by borough, and so it is possible to learn a bit about the data by examining this graph.  The first cluster of incidents occurs within the 10000-10500 range, which correlates to zip codes within Manhattan.  The second cluster seems to lie primarily in the 11200-11400 range, which correlates largely to zip codes in Brooklyn.  Finally, the fourth plot shows the same range of zip codes on the x axis but with population of each zip code on the y axis.  This plot proves that there are populations in these zip codes, even though they show no complaints on the previous graph.  The majority of these lines probably correlate to the areas with zero or close to zero complaints that we saw in the earlier plots.'''
