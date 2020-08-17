n=int(input())
t=[]
for i in range(n):
	l=[]
	l=[int(j) for j in input().split()]
	k=[int(j) for j in input().split()]
	l.append(k)
	t.append(l)
for i in t:
	s=[]
	x1=i[3][0]
	x2=i[3][1]
	x.append(x1)
	x.append(x2)
	s1=x1-i[3][6]
	s2=x2-i[3][6]
	s.append(s1)
	s.append(s2)
	if s1%2!=0:
		o.append(0)
		od.append(s1)
	if s2%2!=0:
		o.append(1)
		od.append(s2)
	for j in range(2,i[0]):
		xi=(i[3][2]*x[j-1]+i[3][3]*x[j-2]+i[3][4])%i[3][5]
		x.append(xi)
		si=xi-i[3][6]
		s.append(si)
		if si%2!=0:
			o.append(j)
			od.append(si)
	lo=[j for _,j in sorted(zip(od,o),reverse=True)]
	if i[1]>0:
		if sum+=



