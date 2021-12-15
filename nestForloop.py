n=5;
# Above Pattern
for i in range(0,n):
    for j in range(0,i):
        print ('* ', end="")
    print('')
    
# Below pattern
for i in range(n,0,-1):
    for j in range(0,i):
        print('* ', end="")
    print('')
