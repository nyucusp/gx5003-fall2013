import pandas as pd
import matplotlib.pyplot as plt

#import data file and set the delimiter in the data file
data = pd.read_table('microprocessors.dat', sep=',', usecols=[0, 1, 2], index_col=['Processor'])

#For juxtaposition, I set the subplot as True
#To plot the data for 'microprocessors' vs 'year of introduction' and for 'microprocessors' vs LOG'number of transistors'
#,I use the logy=[True] for making LOG plot
# there are 2 output in the Problem 3. One is 'Problem_3a.png' and the other is 'Problem_3b.png'
# 'Problem_3a.png' is without LOG in Y variable, 'Problem_3b.png' is with LOG in Y variable
data.plot(subplots=True,style=['o','rx'],logy=[True],title='Problem_3')
data.plot(subplots=True,style=['o','rx'],title='Problem_3')

plt.show()

#this line is to save figure as *.png format, but the image file comes as white without any graph so that I don't use this code 
#plt.savefig('Problem_3.png')


