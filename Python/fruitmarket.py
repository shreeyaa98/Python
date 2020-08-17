import math
n=int(input())
quant=[int(i) for i in input().split()]
quant=sorted(quant)
q=int(input())
l=[]
for i in range(q):
	j=int(input())
	l.append(j)
def tenzu(j):
	if quant[0]>=j:
			return j
	else:
		it=0
		s=0
		for k in quant:
			if k>=j:
				break
			else:
				it+=1
				s+=k
		if (n-it)*j+s>=i:
			return j 
		else:
			return tenzu(j+1)
for i in l:
	j=math.ceil(i/n)
	if sum(quant)<i:
		ans=-1
	else:
		ans=tenzu(j)
	print(ans)




