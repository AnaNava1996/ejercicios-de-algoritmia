#tells if a string is a permutation of the other... also it deletes the spaces...

string1="cosa preshosha"
string2="preshosha cosa"
#string1=string1[0:4]+string1[5:len(string1)+1]
string1=string1.replace(' ','')
string2=string2.replace(' ','')

array=[0]*26

for i in string1:
	array[ ord(i)-ord('a') ] += 1
	

for i in string2:
	array[  ord(i)-ord('a')  ]-=1


print(array)



