def getKey(item):
	return item[1]
n=int(input())
l=[]
last=0
profit=0
seq=[0]*3
for i in range(n):
	t=[int(x) for x in input().split()]
	t.insert(0,i+1)
	l.append(t)
l.sort(key=lambda x:x[1],reverse=True)
print(l)
time=3
for i in l:
	if i[2]>time:
		continue
	else:
		for j in range(i[2]-1,-1,-1):
			if seq[j]==0:
				seq[j]=i[0]
				profit+=i[1]
				last=i[2]
				break
print(seq)
print(profit)



