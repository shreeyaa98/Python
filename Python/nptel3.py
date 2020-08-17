def countX(l,x):
	return l.count(x)
def getKey(item):
	return item[1]

def histogram(l):
	lst=[]
	for i in l:
		for t in lst:
			if i==t[0]:
				break
		else:
			lst.append((i,countX(l,i)))
	list=sorted(lst,key=getKey)
	for i in range(0,len(list)):
		for j in range(0,len(list)-1):
			if list[j][1]==list[j+1][1]:
				if list[j]>list[j+1]:
					a=list[j]
					list[j]=list[j+1]
					list[j+1]=a
	print(list)				
histogram([13,12,11,13,14,13,7,7,13,14,12])
