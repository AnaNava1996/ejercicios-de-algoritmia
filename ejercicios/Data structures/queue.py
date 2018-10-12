class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Queue:
	def __init__(self):
		self.head=None
		self.top=None
	
	def push(self,data):
		newNode=Node(data)
		if(self.head is None):
			self.head=newNode
			self.top=self.head
		else:
			self.top.next=newNode
			self.top=self.top.next
			
	def dequeue(self):
		if(self.head is None):
			print("Error")
		elif(self.head==self.top):
			self.head=self.head.next
			self.top=self.head
		else:
			self.head=self.head.next
		
	def print_queue(self):
		current=self.head
		if(self.head is None):
			print("empty list")
		else:
			while(current):
				print(current.data,end=" ")
				current=current.next
		print("")
		
	def print_top(self):
		if(self.top is None):
			print("Error")
		else:
			print(self.top.data)

op=7
queue=Queue()
while(op!=0):
	op=int(input("\n1-Para push\n2-Para dequeue\n3-Para imprimir valores\n4-Para imprimir top\n0 para salir\n-->"))
	if(op==1):
		n=int(input("Introduzca en la pila: "))
		queue.push(n)
	elif(op==2):
		queue.dequeue()
	elif(op==3):
		queue.print_queue()
	elif(op==4):
		queue.print_top()
	else:
		print("opcion no valida")
		
		









