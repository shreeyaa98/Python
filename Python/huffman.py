from collections import defaultdict
d={}
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


	def insert(self,x,y):
		self.left=x
		self.right=y

	def inorder(self, temp):
		if self.left.value == None and self.right.value ==None:
			d[self.value]=temp
			print(temp)	
		else:
			temp.append(0)
			self.left.inorder(temp)
			del temp[-1]
			temp.append(1)
			self.right.inorder(temp)
			del temp[-1]

	def __str__(self):
		return(str(self.inorder())) 

l=[Tree(6),Tree(7),Tree(5),Tree(4),Tree(3)]
l.sort(key=lambda x: x.value)

def addinlist(sum):
	if len(l)==0:
		l.append(sum)
	else:
		for i in range(len(l)):
			if(l[i].value>sum.value):
				l.insert(i,sum)
				return
		else:
			l.append(sum)
while len(l)!=1:
	i=0;
	j=1;
	sum=l[i].value+l[j].value
	root = Tree(sum)
	root.insert(l[i],l[j])
	if len(l) != 1:
		l.pop(0)
		l.pop(0)
	addinlist(root)
	
	# for i in l:
	# 	print(i.value, end=" ")
	# print()
temp=[]
l[0].inorder(temp)
print(d)

