class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Single_Linked_List:
	def __init__(self):
		self.head=None
	
	def print_list(self):
		current=self.head
		while(current != None):
			print(current.data, end=" ")
			current=current.next
		
	def insert(self,data):
		NewNode = Node(data)
		if(self.head is None):
			self.head=NewNode
			return
			#self.next=None
		Aux = self.head
		while(Aux.next):
			Aux=Aux.next
		Aux.next=NewNode
	


MyList = Single_Linked_List()
MyList.insert(5)
MyList.insert(5)
MyList.insert(5)
MyList.insert(5)
MyList.print_list()














