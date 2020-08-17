n=int(input())
for i in range(n):
	s=input()
	arr=[0 for j in range(len(s))]
	flag=0
	for j in range(len(s)):
		if s[j]=='.':
			continue
		else:
			k=int(s[j])
			if j-k<0:
				small=0
			else:
				small=j-k
			if j+k>len(s)-1:
				large=len(s)-1
			else:
				large=j+k
			for i in range(small,large+1):
				if arr[i]==0:
					arr[i]=1
				else:
					flag=1
					break
			if flag==1:
				break
	if flag==1:
		print("unsafe")
	else:
		print("safe")

