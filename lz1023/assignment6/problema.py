import matplotlib.pyplot as plt
import pandas as pd

myfile=pd.read_csv('labeled_data.csv')
pop_inc=myfile[['population','num_incidents']]
pop_inc_index=pop_inc.set_index('population')
index1=pop_inc_index.sort()

plot1=index1.plot(legend=True, style="yo")
plot1.set_title("Number of Incidents and Population Size")
plot1.set_xlabel("Population")
plot1.set_ylabel("Incidents")
plt.xlim(-3000,123000)
plt.ylim(-3000,123000)



zip_inc=myfile[['# zipcode','num_incidents']]
zip_inc_index=zip_inc.set_index('# zipcode')
index2=zip_inc_index.sort()

plot2=index2.plot(legend=True, style="go")
plot2.set_title("Number of Incidents and Zipcode")
plot2.set_xlabel("Zipcode")
plot2.set_ylabel("Incidents")
plt.xlim(9800,15000)
plt.ylim(-3000,123000)

plt.show()