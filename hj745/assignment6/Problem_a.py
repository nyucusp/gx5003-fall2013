import pandas as pd
import matplotlib.pyplot as plt

#import data file and set the delimiter in the data file
data1 = pd.read_table('labeled_data.csv', sep=',',usecols=[0, 1, 2], index_col=['# zipcode'])
data2 = pd.read_table('unlabeled_data.csv', sep=',',usecols=[0, 1], index_col=['# zipcode'])
#sort data with ascending order  
result1 = data1.sort(ascending=True)
result2 = data2.sort(ascending=True)

#plot the data
result1.plot(title='Problem a_labeled')
result2.plot(title='Problem a_unlabeled')
plt.show()
