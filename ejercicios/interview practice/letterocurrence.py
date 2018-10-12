#the program print the most common letter in the string

string="hola como estas"

array=[0]*128

for i in string:
	array[ord(i)]+=1

maxi=0
index=0
for i in range(0,len(array)):
	if (maxi<array[i]):
		maxi=array[i]
		index=i
print("'"+chr(index)+"'")
