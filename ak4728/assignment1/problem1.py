#cycle
def cycle(nr):
 count=0;
 while nr!=1:
  if nr%2==1:
   nr=3*nr+1
  else:
   nr=nr/2
  count=count+1
 count=count+1
 return count
#interval
def interval(i,j):
 n=0
 max=cycle(i)
 for x in range (i+1,j):
  n=cycle(x)
  if max<=n:
   max=n
 print(i,j,max)
#main
sw=1
while sw==1:
 i=int(input())
 j=int(input())
 interval(i,j)
 print("Continue? 1=Yes 0=No")
 sw=int(input())