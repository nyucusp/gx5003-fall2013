import numpy as np
import matplotlib.pyplot as plt

finput = open('ML1Dataset/labeled_data.csv','r')
finput.readline()
zip = []
pop = []
inc = []
for line in finput:
	tokens = line.split(',')
	zip.append(float(tokens[0]))
	pop.append(float(tokens[1]))
	inc.append(float(tokens[2]))

fig = plt.figure()
graph = fig.add_axes((.1,.3,.8,.6))
plt.plot(pop,inc,'kx')
graph.set_xlabel('population')
graph.set_ylabel('# incidents')

text = '''
Interesting features: There is an array of points with 0 incidents even for a large population.
This suggests that it is reasonable for a large zip code to have no incidents, perhaps even by 
chance. Of course, it could be that safer districts have more money and police resources, but it
could also be that the noise is Poisson distributed and not normally distributed. There also,
predictably, appears to be a generally positive correlation between population size and number of
incidents.'''

fig.text(.1,0.01,text)
plt.show()
fig.savefig('a.png')
