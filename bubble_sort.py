a=[1,23,43,53,22,33]
for i in range(len(a)):
	for j in range(len(a)-i-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp

print a
