class Node:
	def __init__(self,initial=None):
		self.x=initial
		self.next=None

	def isempty(self):
		if self.x==None:
			return(True)
		else:
			return(False)

	def append(self,value):
		if self.isempty():
			self.x=value
			return()
		temp=self
		if self.next==None:
			newnode=Node(value)
			self.next=newnode
			return()
		else:
			self.next.append(value)

	def delete(self,value):
		if self.isempty():
			return("the list is empty")

		elif self.x==value:
			if self.next==None:
				self.x=None
				return()
			else:
				self.x=self.next.x
				self.next=self.next.next
		elif self.next==None:
			return()
		else:
			self.next.delete(value)

an=Node(5)
an.append(10)
an.append(15)
an.delete(5)
an.delete(10)
print(an.x)



