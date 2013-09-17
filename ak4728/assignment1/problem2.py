import sys
a=map(int,sys.argv[1:])
print('Not j','J')[len(set(map(lambda x,y:abs(x-y),a[1:],a[:-1])))>len(a)-2]+'olly'
