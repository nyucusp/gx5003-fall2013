"""
Requested annotations for this problem (i.e. answers to questions) are at the *bottom*
of this file, after the actual code.
"""

import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num, MonthLocator, DateFormatter


"""
First we open the text file and save the lines to the list input_lines
"""

inputfile = open('genes.dat', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()

#Here we make a list whose elements are the lists of values for Genes A, B, C, and D
#respectively.
Data_list = [[],[],[],[]]

for i in range(0,4):
    for j in range(1, len(input_lines)):
        Data_list[i].append(float(input_lines[j].split(',')[i]))


"""
Now we make the desired plots
"""
fig, axarray = plt.subplots(4,4)
for i in range(0,4):
    for j in range(0,4):
        ax = axarray[i, j]
        ax.scatter(Data_list[i], Data_list[j], color='blue',s=5,edgecolor='none')
        ax.xaxis.set_major_locator(plt.FixedLocator([0,0.5,1]))
        ax.yaxis.set_major_locator(plt.FixedLocator([0,0.5,1]))
        ax.set_xlim(-.2, 1.2)
        ax.set_ylim(-.2, 1.2)
        x0,x1 = ax.get_xlim()
        y0,y1 = ax.get_ylim()
        ax.set_aspect((x1-x0)/(y1-y0))
       
        #Here are are labelling the outer graphs and plotting the best fit curves
        #as explained in the annotations at the end of this code.  Note that we have to
        #be careful to sort our lists of points that we graph for the polynomial at the
        #same time to ensure the correct output.
        if i == 0:
            if j == 0:
                ax.set_xlabel('Gene A')    
                ax.xaxis.set_label_position('top')
            
            if j == 1:
                ax.set_xlabel('Gene B')    
                ax.xaxis.set_label_position('top')
                temp_listx = sorted(Data_list[i])
                temp_listy = []
                for k in range(0,len(temp_listx)):
                    temp_listy.append(Data_list[j][Data_list[i].index(temp_listx[k])])
                coefficients = numpy.polyfit(temp_listx, temp_listy, 5)
                y_vals = numpy.polyval(coefficients, temp_listx)
                ax.plot(temp_listx, y_vals, color = 'red')
                
            if j == 2:
                ax.set_xlabel('Gene C')    
                ax.xaxis.set_label_position('top')
                temp_listx = sorted(Data_list[i])
                temp_listy = []
                for k in range(0,len(temp_listx)):
                    temp_listy.append(Data_list[j][Data_list[i].index(temp_listx[k])])
                coefficients = numpy.polyfit(temp_listx, temp_listy, 1)
                y_vals = numpy.polyval(coefficients, temp_listx)
                ax.plot(temp_listx, y_vals, color = 'red')
            
            if j == 3:
                ax.set_xlabel('Gene D')    
                ax.xaxis.set_label_position('top')
                temp_listx = sorted(Data_list[i])
                temp_listy = []
                for k in range(0,len(temp_listx)):
                    temp_listy.append(Data_list[j][Data_list[i].index(temp_listx[k])])
                coefficients = numpy.polyfit(temp_listx, temp_listy, 3)
                y_vals = numpy.polyval(coefficients, temp_listx)
                ax.plot(temp_listx, y_vals, color = 'red')
        
        if j == 0:
            if i == 0:
                ax.set_ylabel('Gene A')    
                ax.yaxis.set_label_position('left')
                
            if i == 1:
                ax.set_ylabel('Gene B')    
                ax.yaxis.set_label_position('left')
                temp_listx = sorted(Data_list[i])
                temp_listy = []
                for k in range(0,len(temp_listx)):
                    temp_listy.append(Data_list[j][Data_list[i].index(temp_listx[k])])
                coefficients = numpy.polyfit(temp_listx, temp_listy, 5)
                y_vals = numpy.polyval(coefficients, temp_listx)
                ax.plot(temp_listx, y_vals, color = 'red')
                
            if i == 2:
                ax.set_ylabel('Gene C')    
                ax.yaxis.set_label_position('left')
                temp_listx = sorted(Data_list[i])
                temp_listy = []
                for k in range(0,len(temp_listx)):
                    temp_listy.append(Data_list[j][Data_list[i].index(temp_listx[k])])
                coefficients = numpy.polyfit(temp_listx, temp_listy, 1)
                y_vals = numpy.polyval(coefficients, temp_listx)
                ax.plot(temp_listx, y_vals, color = 'red')
                
            if i == 3:
                ax.set_ylabel('Gene D')    
                ax.yaxis.set_label_position('left')
                temp_listx = sorted(Data_list[i])
                temp_listy = []
                for k in range(0,len(temp_listx)):
                    temp_listy.append(Data_list[j][Data_list[i].index(temp_listx[k])])
              
                coefficients = numpy.polyfit(temp_listx, temp_listy, 3)
                y_vals = numpy.polyval(coefficients, temp_listx)
                ax.plot(temp_listx, y_vals, color = 'red')

#setting parameters for the graph and creating the plot
fig.set_size_inches(16,16)
fig.suptitle('Correlation Scatterplot of Four Genes')
fig.patch.set_facecolor('white')
plt.show()


"""
ANNOTATIONS (answers to questions and explanation of the graph):
-We see that C is most correlated with gene A, then D, then B.
-We have put a degree 5 curve for A vs. B *and* B vs. A, a degree 3 curve for
A vs. D *and* D vs. A, and a degree 1 curve for A vs. C *and* C vs. A.
"""