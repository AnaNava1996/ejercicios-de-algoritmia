lista=[2,3,9,8,4,6,7,5,1]

def bubble_sort(array):
	for i in range(len(array)-1,0,-1):
		for j in range(0,i):
			if(array[j]>array[j+1]):
				temp=array[j]
				array[j]=array[j+1]
				array[j+1]=temp
	print(array)


