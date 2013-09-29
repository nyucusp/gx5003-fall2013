#problem2

#haozhe Wang
#it doesn't work!I tried my best.
#still learning when to take the user input as a variable, when not.

import csv

output_data={}#empty dict for later use
myfile=open('zipCodes.csv','r')#open file and read

outputfile=open('density2.txt','w')#open a new file and write in it

zip_area=csv.DictReader(myfile)#using csv module

for line in zip_area:

    if line['Total Population per ZIP Code']!= " ":#ignoring the blanks as suggested

           population = line['Total Population per ZIP Code']

           area = line['area']

           density = float(population)/float(area)#trying to keep the units consistant, not sure if it will work

           zipcode = line['name']

           output_data[zipcode] = density

           sorted(output_data)

           for den, zipcd in output_data:

               gen_data=str(zipcd)+ " "+str(den)+ "\n" #start in a new line each time

           outputfile.write(gen_data)

myfile.close()

outputfile.close()#it is empty, but i don't know how to fix it.



