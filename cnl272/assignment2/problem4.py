import sys
from Borough import Borough

from problem3 import getpopulation, borough
#import function from my problem3

borough_dict = borough()
population_dict = getpopulation()

borough_name = sys.argv[1]
borough_name =borough_name.split(' ')[0]
borough_name =borough_name.capitalize()
#let the all of the borough name be read

myborough=Borough(borough_name)
population = 0

for zip_code in borough_dict[borough_name]:
	if zip_code in population_dict:
		myborough.addZipcode(zip_code)
		population += population_dict[zip_code] 

myborough.count_average(population)

print myborough.average