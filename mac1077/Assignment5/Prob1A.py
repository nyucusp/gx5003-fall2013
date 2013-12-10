import matplotlib.pyplot as plt
from datetime import date

data = open('stocks.dat','r') #open file

mon = [] #month
app = [] #apple
for line in data:
    split_data = line.split(',')
    mon.append(split_data[0])
    app.append(split_data[1])

del mon[0]
del app[0]
dates = []
for element in mon:

    year = int(element.split('-')[0]) #Year 2006-2008
    month = int(element.split('-')[1]) #Months
    new_date = date(int(year),int(month),1)
    dates.append(new_date)

fig, ax = plt.subplots()
ax.plot(dates, app, 'o-')
fig.autofmt_xdate()

plt.xlabel('Date') #Label in X
plt.title("Apple's Stocks from Feb 2006 - Oct 2008") #Title
plt.ylabel("Stock") #Label in Y
ax.set_ylim(50,200) #limits of X & Y
datemin = date(2005, 12, 1) #Limits of minimum date
datemax = date(2008, 10, 1) #Limits of maximum date
ax.set_xlim(datemin, datemax)
plt.grid(which = 'both', color = '0.90', linestyle = '-')


plt.show()

#Didn't use pandas, instead I did it in matplotlib
# I removed the grids in a way that the graph seems better and reduced the scale of X and Y