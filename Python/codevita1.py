def sum(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


n=int(input())
l=[int(i) for i in input().split()]
while(len(l)>2):
	m=max(l)
	s=sum(l)-m
	if(s>m):
		ans=len(l)
		break
	else:
		l.remove(m)
	
if len(l)<3:
	print(0)
else:
	print(ans)
