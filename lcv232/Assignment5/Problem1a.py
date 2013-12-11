import matplotlib.pyplot as plt
from datetime import date

data = open('stocks.dat','r') #open file

arr_app = [] #An array to maintain apple's stock values
arr_mon = [] #An array to maintainthe Month values of the stock
for plot1 in data:
    split_data = plot1.split(',')
    arr_mon.append(split_data[0])
    arr_app.append(split_data[1])

del arr_app[0]
del arr_mon[0]
arr_date1 = []          
for element in arr_mon:

    year = int(element.split('-')[0]) # To get the Years range from 2006 to 2008
    month = int(element.split('-')[1]) # For the values of Month
    new_date = date(int(year),int(month),1)
    arr_date1.append(new_date)

fig, ax = plt.subplots()  # Plotting values
ax.plot(arr_date1, arr_app, 'o-')
fig.autofmt_xdate()

plt.xlabel('Date') # To Display the Label in the X-axis
plt.title("Apple's Stocks from Feb 2006 - Oct 2008") # The Main Title of the Plot 
plt.ylabel("Stock") # To Display the Label in the Y-axis
ax.set_ylim(50,200) # Setting the limits of X - axis & Y - axis
min_date = date(2005, 12, 1) # Limiting data for the minimum date
max_date = date(2008, 10, 1) # Limiting data for the maximum date
ax.set_xlim(min_date, max_date)
plt.grid(which = 'both', color = '0.90', linestyle = '-')


plt.show()

# I have used Matplotlib to do the plotting.
# Have not used much of gridlines as they add confusion to the graph.
# I removed the grids in a way that the graph seems better interms of the scale of X and Y axis.
# The color used to display the plotting is Blue for Apple, as it is subtle to the eye. 