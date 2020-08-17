def swap(a,b):
	return(b,a)
class Outer:
	count=0
	def __init__(self):
		self.obj=self.Inner()
		self.obj.wel()
		Outer.count+=1
	def meth(self):
		print("Don't do meth")
	class Inner:
		def wel(self):
			print("Welcome")
obj2=Outer()
obj1=Outer()
obj3=Outer()
print(obj1.count)
obj.meth()






