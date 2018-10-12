'''No lo he probado pero hace esto
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. There-
fore, in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
Stacks should be composed of several stacks, and should create a new stack once
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
behave identically to a single stack (that is, pop() should return the same values as it
would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific
sub-stack.
'''

class stack_of_plates:
	def __init__(self):
		self.array=[]
		self.next
		self.last

class stack_of_stacks:
	def __init__(self):
		newStack=stack_of_plates()
		self.head=newStack
		self.head.next=None
		self.head.last=None
		self.top=self.head

	def push(self,num):
		if(len(self.top.array)==num):
			newPlates=stack_of_plates()
			self.top.next=newPlates
			newPlates.last=self.top
			self.top=self.top.next
			self.top.array.append("plate")
		else:
			self.top.array.append("plate")
	
	def pop(self):
		if(len(self.top.array)==1):
			self.top.array.pop()
			self.top.last=self.top
			self.top.next=None
		else:
			self.top.array.pop()


