'''
do all the posible sets of a set of numbers:
[1,2,3]

{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}

'''


dic=set('')

#recursive function
def getTheSet(atup):
	dic.add(atup)
	cont=0
	while(cont!=len(atup)):
		getTheSet(atup[:cont]+atup[cont+1:])
		cont+=1
	return



atup=('1','2','3','4','5','6')

getTheSet(atup)

print(dic)






