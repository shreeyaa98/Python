n=int(input())
l=[int(i) for i in input().split(",")]
d=[]
cnt=0
for i in l:
	k=[]
	sum=0
	while i>0:
		k.append(i%6)
		# print(k)
		i=i//6
		# print(i)
	for j in k:
		sum+=j
	d.append(sum)
# print(d)
for i in range(n):
	for j in range(i+1,n):
		if d[j]<d[i]:
			cnt+=1
print(cnt)

