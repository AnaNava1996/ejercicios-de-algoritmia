class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

class Tree:
	def __init__(self,data):
		self.root=Node(data)
	
	def insert(self,node,data):
		newNode=Node(data)
		if(data<node.data):
			if(node.left==None):
				node.left=newNode
				return
			self.insert(node.left,data)
		else:
			if(node.right==None):
				node.right==newNode
				return
			self.insert(node.right,data)








