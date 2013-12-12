#Assignment 6 
#Problem 1b
#Hoazhe Wang
import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt
labeledfile = pd.read_csv('labeled_data.csv')

plotdata2 = labeledfile[['# zipcode','num_incidents']]
index2 = plotdata2.set_index('# zipcode')
second_plot = index2.plot(legend = True, style = "y.")
second_plot.set_title('Incidents vs. Zipcode')
second_plot.xaxis.grid(True, which="minor")
second_plot.xaxis.grid(True, which="major")
second_plot.set_ylabel('Incidents')
second_plot.set_xlabel('Zipcode')
#plt.ylim(-1,120000)
plt.tight_layout()
plt.savefig('inc_vs_zip.png',dpi=300)