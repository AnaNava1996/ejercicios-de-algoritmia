'''
array=[[0]*2 for i in range(0,4)]


for i in range(0,len(array)):
	for j in range(0,len(array[i])+1):
		try:
			print(array[j][i])
		except IndexError:
			print("List index out of range: array["+str(j)+"]["+str(i)+"]")
'''
string="hello world hola perro como estaaaaas"

string=string.replace(" ","")

print(string)

n=10
t_col=(n-1)*(1+len(string)//(n+n-2))
print(t_col)


array=[ [' ']*t_col for i in range(0,n) ]

#string=string.replace(string[0],"")
j=-1
while(len(string)!=0):
	j+=1
	for i in range(0,n):
		if(len(string)!=0):
			array[i][j]=string[0]
			string=string[1:]
		else:
			break
	for i in range(n-2,0,-1):
		j+=1
		if(len(string)!=0):
			array[i][j]=string[0]
			string=string[1:]
		else:
			break
for i in array:
	print(i)








