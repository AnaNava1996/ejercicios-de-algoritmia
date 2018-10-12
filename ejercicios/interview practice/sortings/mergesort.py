
def mergesort(alist):
	lar=len(alist)
	if(lar==1):
		return alist
	else:
		half=lar//2
		return merge(mergesort(alist[0:half])  ,  mergesort(alist[half:lar]))

def merge(a,b):
	ab=[]
	while(len(a)!=0 and len(b)!=0):
		if(len(a)==0  or len(b)==0):
			break
		elif(a[0]<b[0]):
			ab.append(a[0])
			del(a[0])
		else:
			ab.append(b[0])
			del(b[0])
	while(len(a)>0):
		ab.append(a[0])
		del(a[0])
	while(len(b)>0):
		ab.append(b[0])
		del(b[0])
	return ab


alist=[1,2,8,4,6,2,9,4,7,22]
print(mergesort(alist))
		
