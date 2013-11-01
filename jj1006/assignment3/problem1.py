import math

def change(costs):
	#COSTS MUST BE IN CENTS
	m = 0.0;
	for c in costs:
		m=m+c
	m=m/len(costs)
	val=0.0
	for c in costs:
		if c>=m:
			val=val+c-math.ceil(m)
		else:
			val=val+math.floor(m)-c
	return int(val/2)


finput = open('input1.txt','r')
n=-1
costs = []
while not n==0:
	line=finput.readline().rstrip()
	if not '.' in line:
		if n>0:
			cstr = str(change(costs))
			cents = cstr[(len(cstr)-2):len(cstr)]
			while len(cents)<2:
				cents = "0"+cents
			print "$"+cstr[0:(len(cstr)-2)]+"."+cents
			costs = []
		n = int(line)
	else:
		costs.append(100*float(line))
