'''s=input('Enter a string')
rev=s[-1::-1]
print(rev)
if s==rev:
	print('palindrome')
else:
	print("not a palindrome")

s='Hello I am Shreeyaa'
l=s.split(' ')
l=sorted(l,key=lambda s: s.lower())
print(l)


s='Hi,I am ? the express.value'
new=''
for i in s:
	c=ord(i)
	#print(c)
	if (c>=65 and c=<90) or (c>=97 and c=<122):
		new+=i
print(new)


s='Hi,I am ? the express.value'
a=j=e=o=0
for i in s:
	if i=='a' or i=='A':
		a+=1
	if i=='e' or i=='E':
		e+=1
	if i=='I' or i=="i":
		j+=1
	if i=='o' or i=='O':
		o+=1
print("A:{0}\n E:{1}\n I:{2}\n O:{3}".format(a,e,j,o))

'''

S={1,2,3,4,4}
Q={1,5,7,3,6}


print(S|Q)
print(S&Q)
print(S-Q)
print(S^Q)
s=set()
s.add(1)
s.add(2)
s.add(2)
print(s)
