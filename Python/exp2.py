def alternating(lst):
	if lst[0]>lst[1]:
		c=0
	else:
		c=1
	for i in range(1,len(lst)-1):
		if c==0:
			if i%2==0:
				if lst[i]<=lst[i+1]:
					return(False)
      		else:
      			if lst[i]>=lst[i+1]:
      				return(False)
		else:
			if i%2==0:
				if lst[i]>=lst[i+1]:
					return(False)
      		else:
      			if lst[i]<=lst[i+1]:
      				return(False)
   	return(True) 
alternating([2,3,1,4])