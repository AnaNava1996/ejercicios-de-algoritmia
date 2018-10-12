#! /usr/bin/python3
def rotLeft(a, d):
	for i in range(0,d):
		temp=a[0]
		for j in range(0,len(a)-1):
			a[j]=a[j+1]
		a[len(a)-1]=temp
	return a


a = [1,2,3,4,5]

print(rotLeft(a,4))
