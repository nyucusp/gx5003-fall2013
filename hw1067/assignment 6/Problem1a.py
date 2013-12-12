#Assignment 6 
#Problem 1a
#Hoazhe Wang
import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt
labeledfile = pd.read_csv('labeled_data.csv')

plotdata1 = labeledfile[['population','num_incidents']]
index = plotdata1.set_index('population')
first_plot = index.plot(legend = True, style = ".")
first_plot.set_title('Incidents vs. Population')
first_plot.xaxis.grid(True, which="minor")
first_plot.xaxis.grid(True, which="major")
first_plot.set_ylabel('Incidents')
first_plot.set_xlabel('Population')
plt.tight_layout()
plt.savefig('inc_vs_pop.png',dpi=300)