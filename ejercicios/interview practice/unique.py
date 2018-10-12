#print the unique letters on the string

'''
arra=set("unique")

print(arra)

'''
#unique characters without a second data structure

#brute force
def solution1(string):
	for i in range(0,len(string)):
		for j in range (i+1,len(string)):
			if (string[i]==string[j]):
				return False
	return True



#extra data structure
def solution2(string):
	arr=[0]*128
	for i in string:
		arr[ ord(i) ]+=1
	cont=1
	for i in arr:
		if (cont<i):
			return False
	return True

#sorting...
def solution3(string):
	string=sorted(string)
	string="".join(string)
	for i in range(0,len(string)-1):
		if(string[i]==string[i+1]):
			return False
	return True


string="hoola"

print(solution1(string))

print(solution2(string))

print(solution3(string))

