l=[int(i) for i in input().split(",")]
r=[]
flag=0
def find():
	for i in range(len(l)):
		if l[i]>=6:
			break
	i-=1
	r.append(l[i])
	l.remove(l[i])
	r.append(l[-1])
	l.pop()
def toprint():
	print(r[0],r[1],":",r[2],r[3],":",r[4],r[5],sep='')

if 2 in l:
	r.append(2)
	l.remove(2)
	if 4 in l:
		if count(0)==4:
			r=[2,4,0,0,0,0]
			flag=1
	if flag!=1:
		for i in range(len(l)):
			if l[i]>=4:
				break
		i-=1
		if i>0:
			r.append(l[i])
			l.remove(l[i])
			find()
			find()
		else:
			print("Impossible")
	toprint()
elif 1 in l:
	r.append(1)
	l.remove(1)
	r.append(l[-1])
	l.pop()
	find()
	find()
	toprint()
elif 0 in l:
	r.append(0)
	l.remove(0)
	r.append(l[-1])
	l.pop()
	find()
	find()
	toprint()
else:
	print("Impossible")


