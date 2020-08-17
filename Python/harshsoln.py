def alternating(l):
	if l[0]>l[1]:
		c=0
	else:
		c=1
	for i in range(1,len(l)):
		if c==0:
			if i%2==0:
				if l[i]<=l[i-1]:
					return(False)
			else:
				if l[i]>=l[i-1]:
					return(False)
		else:
			if i%2==0:
				if l[i]>=l[i-1]:
					return(False)
			else:
				if l[i]<=l[i-1]:
					return(False)
	return(True)
print(alternating([2]))
