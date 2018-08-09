# the given program is defined to replace odd places with even and vice-versa

a=[1,2,3,4,5,6,7,8,9,10]
dd=[]
for i in range(0,len(a)-1):
    if a[i]%2==1:
        dd.insert(i+1,a[i])
    else:
        dd.insert(i-1,a[i])

