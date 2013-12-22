# Exercise 3: Dot plots for labeled data, generated after group tutoring session

import pandas 
import matplotlib.pyplot as pplt
import numpy as nmp

#Reading-in the file

mp = open('microprocessors.dat','r') #List of microprocessors with quantitative values
next(mp) # to delete first row of file, i.e. header "Processor,Year of Introduction,Transistors"

mpList = []
for i in mp:
    mpList.append(i)
#Loaded file content to a main list

#Going through the main list to populate separate lists for the Label ("name of a microprocessor"), 
#and for Quantitative Values 1 ("year of introduction") & 2 ("number of transistors")

mp2 = []
for i in mpList:
    mp2.append(i.split(','))    #Splitting each line of imported data into a list of three elements which make up the line (Label + two QV's)
                                #Split returns a list of the words in the line (line format is string) 
LabelList = []
QV1 = [] #list to load Year of Introduction
QV2 = [] #list to load Number of Transistors
for j in mp2: #Stripping respective data from main list
    LabelList.append(j[0])
    QV1.append(j[1]) 
    QV2.append(nmp.log10(float(j[2].strip())))
QV1 = sorted(QV1)

for x in range(0, len(QV1)):
    for y in mp2:
        if QV1[x] == y[1]:
            LabelList[x] = y[0]
            QV2[x] = nmp.log10(float((y[2])))

QV2 = sorted(QV2)

CountList = []
for i in range(1, len(QV1) + 1):
    CountList.append(i)

chart = pplt.figure(figsize = (25,10))
ax1 = chart.add_subplot(1,2,1)
ax1.plot(QV1, CountList, 'o')
ax1.grid(True,which='both')
ax1.set_xlabel("Year of Introduction")
pplt.yticks(range(len(LabelList)), LabelList)
ax2 = chart.add_subplot(122)
ax2.plot(QV2, CountList, 'o')
ax2.grid(True,which='both')
ax2.set_xlabel("Number of Transistors (log10)")
ax1.tick_params(axis='both', direction='out', labelsize=10)
ax2.tick_params(axis='both', direction='out', labelsize=10)
pplt.yticks(range(len(LabelList)), LabelList)
pplt.savefig('Problem_3.png')

