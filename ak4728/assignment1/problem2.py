import sys
if len(sys.argv[1:])-1 == int(sys.argv[1]):
    a=map(int,sys.argv[1:].pop(0))
    print('Not j','J')[len(set(map(lambda x,y:abs(x-y),a[1:],a[:-1])))>len(a)-2]+'olly'
else:
    print('The number of elements is wrong')




