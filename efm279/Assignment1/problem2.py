
import sys

def main(x,no):
  r = [];
  for i in range(1,len(x)):
	 a=abs(int(x[i])-int(x[i-1]))
         r.append(a)	 
	 if a==0:
		print "Not Jolly"
		return
	 elif a>len(x):
		print "Not Jolly"
		return
	 elif a not in range(1,int(n)):
		print "Not Jolly"
	 	return
 
  xx = map(int, x)
  print xx
  for k in range(1,len(r)):
  	for j in range(1,len(x)-1):
		if r[k] not in xx:
			print "Not Jolly d"
			return
  print "Jolly!"			  	 
  

n=sys.argv[1]
seq = sys.argv[2:len(sys.argv)]
main(seq,n)
