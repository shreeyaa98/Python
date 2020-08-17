class Animal:
	msg='hello'
	class Inner:
		def msg():
			print(Animal.msg)

m=Animal()
m.Inner.msg()
