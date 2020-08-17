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
	return(list)		
def GetKey(item):
	return item[0]
def getkey(item):
	return item[2]
def transcript(l1,l2,l3):
	r={}
	c={}
	l={}
	lst=[]
	cnt=0
	for i in l1:
		c[i[0]]=i[1]
	for i in l2:
		r[i[0]]=i[1]	
	for i in range(len(l3)):
		for j in r.keys():
			if l3[i][0]==j:
				if j not in l.keys():
  					l[j]=cnt
					lst.append((j,r[j],[(l3[i][1],c[l3[i][1]],l3[i][2])]))
					cnt+=1
				else:
					k=l[j]
					lst[k][2].append((l3[i][1],c[l3[i][1]],l3[i][2]))
	list=sorted(lst,key=GetKey)	
	list=sorted(list,key=getkey)
	print(list)

transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")],[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")])