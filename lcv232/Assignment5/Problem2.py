import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import matplotlib.dates as date
from matplotlib.dates import date2num, MonthLocator, DateFormatter

# Checking the dat file
arr_check = []
actions = open('actions-fall-2007.dat','r')
for x in actions:
    arr_check.append(x)
del arr_check[0]

# Converting Calendar time into Days for plotting
arr_day = []
for x in arr_check:
    val1 = dt.datetime.strptime(x.strip(),'%Y-%m-%d %H:%M:%S') # Formatting
    val2 = date.date2num(val1)
    arr_day.append(val2)
# Finding the number of bins present; allocating it to 'slot1'
val1 = max(arr_day)-min(arr_day)
slot1 = int(val1)+1

# Formatting & Plotting the values in a Histogram
start = date.date2num(dt.datetime.strptime('2007-09-10 12:00:00','%Y-%m-%d %H:%M:%S'))
end = date.date2num(dt.datetime.strptime('2007-12-18 12:00:00','%Y-%m-%d %H:%M:%S'))
plt.hist(arr_day, bins = slot1, color = 'g', range = (start ,end )) # Defining Histogram Attributes
plt.gca().xaxis.set_major_locator(MonthLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter('%B'))
plt.ylabel('Number of Actions')
plt.title('Count of student actions in Fall 2007 Scientific Visualization Course')

# Plotting the values of the Due Date in the output
arr_due = ['2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-11 12:00:00','2007-12-15 12:00:00']
arr_due_time = []
for x in arr_due:
    arr_due_time.append(dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
labels = ['Assin0 and 1 due', 'Assin2 due', 'Assin3 due', 'Assin4 due', 'Assin6 due', 'Assin5 due']
for i in range(0, 6):
    plt.text(arr_due_time[i],10000 + 1000*i,labels[i],rotation=0, size='small')
plt.vlines(date2num(arr_due_time), 0, 16000, color = 'k',linestyle = 'dashed' )
plt.savefig("Problem2.png")

# Answer 1 : I selected my bins by slotting them on a 24-hour basis (between 12:00 - 12:00) as the duetime for every assignment is 12:00.
# Answer 2 : Assignments 3, 5, 6 seem to have a lot of activities going-on; I assume they might have been either tough / complex / or needed more activities to complete. 
# Answer 3 : I find that there are more late submissions for Assignments 3, 4 & 6.