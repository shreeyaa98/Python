class Tree():
	def __init__(self,initval=None):
		self.value=initval
		if self.value:
			self.left=Tree()
			self.right=Tree()
		else:
			self.left=None
			self.right=None

	def isempty(self):
		return(self.value==None)


	def insert(self,x):

		if self.isempty():
			self.value=x
			self.left=Tree()
			self.right=Tree()
		elif self.value>x:
			self.left.insert(x)
		else:
			self.right.insert(x)

	def findmin(self):
		if self.isempty():
			return(None)
		else:
			if self.left.value==None:
				return(self.value)
			else:
				self.left.findmin()


	def delete(self,x):

		if self.isempty():
			return("value not found")
		if self.value==x:
			if self.left.value==None and self.right.value==None:
				self.value=None
				self.left=None
				self.right=None
			elif self.left.value==None:
				self.value=self.right.value
				self.right.delete(self.value)
			elif self.right.value==None:
				self.value=self.left.value
				self.left.delete(self.value)
			else:
				self.value=self.right.minval()
				self.right.delete(self.value)

		elif self.value>x:
			self.left.delete(x)
		else:
			self.right.delete(x)

	def inorder(self):
		if self.isempty():
			return([])
		else:
			return(self.left.inorder()+[self.value]+self.right.inorder())

	def __str__(self):
		return(str(self.inorder()))


a=Tree()
a.insert(5)
a.insert(10)
a.insert(13)
a.insert(4)
a.insert(6)
a.insert(12)
print(a)
a.delete(12)
print(a)

		

