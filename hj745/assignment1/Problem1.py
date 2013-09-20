i = int(input("Enter i : "))
j = int(input("Enter j : "))

def swap(a, b):
    return [b,a]

if i>j : (i, j) = swap(i, j)

MinVal = int(i)
MaxVal = int(j)
Big = 0

for x in range(i, j+1):
    cnt = 1
    tmp = int(x)
    while tmp!=1:
        if tmp%2 == 0 :
            tmp=int(tmp/2)
            cnt = cnt+1
        else :
            tmp=tmp*3+1
            cnt = cnt+1
    if cnt>Big : Big = cnt

print (MinVal, MaxVal, Big)