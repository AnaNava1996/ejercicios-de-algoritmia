class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
	
class Stack:
	def __init__(self):
		self.head=None
		self.end=None
	
	def insert(self,data):
		if(self.head==None):
			self.head=Node(data)
			self.end=self.head
		else:
			newNode=Node(data)
			self.end.next=newNode
			self.end=self.end.next
			
	def print_stack(self):
		node=self.head
		while(node):
			print(node.data)
			node=node.next

	def pop1(self):
		current=self.head
		while(current.next!=self.end):
			current=current.next
		self.end=current
		self.end.next=None



pila=Stack()

pila.insert(1)
pila.insert(2)
pila.insert(3)

pila.print_stack()

pila.pop1()

pila.print_stack()




	
