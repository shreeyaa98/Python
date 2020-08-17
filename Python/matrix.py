n=int(input('Enter size of matrix'))
print("Enter row wise")
list2=[]
for i in range(n):
	list1=[]
	print("Enter row",i)
	for j in range(n):
		k=input()
		list1.append(k)
	list2.append(list1)
for j in list2:
	print(j)
l=[]
for j in range(n):
	l1=[]
	for k in range(n):
		l1.append(list2[k][j])
	l.append(l1)
for j in l:
	print(j)


