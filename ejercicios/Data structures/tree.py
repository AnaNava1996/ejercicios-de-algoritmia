class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

class Tree:
	def __init__(self,data):
		self.root=Node(data)
		
	def insert(self,node,data):
		Newnode=Node(data)
		if(data>node.data):
			if(node.right==None):
				node.right=Newnode
				return
			self.insert(node.right,data)
		else:
			if(node.left==None):
				node.left=Newnode
				return
			self.insert(node.left,data)

	def print_inorder(self,node):
		if(node.left):
			self.print_inorder(node.left)
		elif(node.right):
			print(node.data)
			self.print_inorder(node.right)
		else:
			print(node.data)
	
	def print_preorder(self,node):
		print(node.data)
		if(node.left==None):
			pass
		else:
			self.print_preorder(node.left)
		if(node.right==None):
			pass
		else:
			self.print_preorder(node.right)
			
	def print_preorder2(self,node,string):
		if (node):
			string += (str(node.data)+" - ")
			string = self.print_preorder2(node.left,string)
			string = self.print_preorder2(node.right,string)
		return string

	def print_inorder2(self,node,string):
		if(node):
			string = self.print_inorder2(node.left,string)
			string += (str(node.data)+" - ")
			string = self.print_inorder2(node.right,string)
		return string

	def print_postorder(self,node,string):
		if(node):
			string = self.print_postorder(node.left,string)
			string = self.print_postorder(node.right,string)
			string += (str(node.data)+" - ")
		return string

Treee = Tree(5)

Treee.insert(Treee.root,4)
Treee.insert(Treee.root,1)
Treee.insert(Treee.root,6)
Treee.insert(Treee.root,7)
Treee.insert(Treee.root,2)
Treee.insert(Treee.root,3)
Treee.insert(Treee.root,10)
Treee.insert(Treee.root,8)
Treee.insert(Treee.root,11)

Treee.print_inorder(Treee.root)
string=""
print(Treee.print_preorder2(Treee.root,string))
string=""
print(Treee.print_inorder2(Treee.root,string))
string=""
print(Treee.print_postorder(Treee.root,string))


'''
print(Treee.root.data)
print(Treee.root.left.data)
print(Treee.root.left.left.data)	
print(Treee.root.left.left.right.data)
print(Treee.root.left.left.right.right.data)
print(Treee.root.right.data)
print(Treee.root.right.right.data)
'''
