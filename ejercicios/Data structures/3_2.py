'''
How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.

'''

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.last=None
		self.min=data


class Double_linke_list_stack:
	def __init__(self):
		self.head=None
		self.top=None
	
	def insert(self,data):#time complexity O(1)
		newNode=Node(data)
		if(self.head is None):
			self.head=newNode
			self.top=self.head
		else:
			newNode.min=min(newNode.min,self.top.min)
			newNode.last=self.top
			self.top.next=newNode
			self.top=self.top.next

	def print_stack(self):
		if(self.head is None):
			print("empty")
		else:
			current=self.head
			while(current):
				print(current.data,end=" ")
				current=current.next
		print()

	def print_stack2(self):
		if(self.top is None):
			print("empty")
		else:
			current=self.top
			while(current):
				print(current.data,end=" ")
				current=current.last
		print()

	def dequeue(self):
		if(self.head==None):
			print("Error")
		else:
			self.head=self.head.next
			self.head.last=None
	
	def pop(self):
		if(self.top==None):
			print("error")
		else:
			self.top=self.top.last
			self.top.next=None

	def print_min(self):
		print("min value is: "+str(self.top.min))


stack= Double_linke_list_stack()
stack.insert(1)
stack.insert(2)
stack.insert(3)
stack.insert(4)
stack.insert(5)
stack.insert(-4)
stack.insert(1.5)

stack.print_stack()
#stack.print_stack2()
stack.print_min()

stack.pop()
stack.print_stack()
stack.print_min()

stack.pop()
stack.print_stack()
stack.print_min()

stack.pop()
stack.print_stack()
stack.print_min()

stack.pop()
stack.print_stack()
stack.print_min()

stack.pop()
stack.print_stack()
stack.print_min()













