def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


'''
lista=[2,3,9,8,4,6,7,5,1]

def quicksort(array):
	if(len(array)==1):
		return array
		print(array)
	elif(len(array)==2):
		return min(array),max(array)
		print(array)
	else:
		tercio=len(array)//3;
		pivot=tercio
		left=0
		right=len(array)-1
		while(left!=right):
			if(array[left]<array[pivot]):
				left=left+1
			elif(array[right]<array[pivot]):
				if(array[left]==array[pivot]):
					array[left],array[right]=array[right],array[left]
					pivot=right
					break
				else:
					array[left],array[right]=array[right],array[left]
			else:
				right=right-1
			print(array)
		return merge(quicksort(array[0:pivot]),quicksort(array[pivot:len(array)]))

def merge(a,b):
	ab=[]
	for i in a:
		ab.append(i)
	for i in b:
		ab.append(i)
	return ab

print(quicksort(lista))
'''



