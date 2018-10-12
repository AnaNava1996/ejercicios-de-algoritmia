'''
its about n steps and how many ways can i walk through a staircase...
the only steps i can take are in x

'''

x=[1,2]


def function(n):
	cont = 0
	for i in x:
		if(n-i==0):
			cont+=1
		elif(n-i>0):
			cont=cont+function(n-i)
	return cont



#x.remove(0)

print(function(4))

