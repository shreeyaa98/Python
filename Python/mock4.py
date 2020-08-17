n=int(input())
l=[]
flag=True
for i in range(n):
	k=[]
	t=input()
	k=[int(j) for j in t.split(" ")]
	l.append(k)
for i in l:
	count=0
	if i[1]>i[2]:
		tot=-1
		print(tot,end=" ")
		pass
	while flag:
		i[0]+=i[1]
		count+=1
		if (i[0]%i[2]) == 0:
			if (i[0]/i[2])>=count:
				tot=(i[0]//i[2])
				print(tot,end=" ")
				break