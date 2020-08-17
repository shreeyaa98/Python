n=int(input("Enter no to make"))
l=[int(i) for i in input("Enter change").split()]
dp=[0 for i in range(n+1)]
dp[0]=0
track=[-1 for i in range(n+1)]
for i in l:
	dp[i]=1
	track[i]=i
	for j in range(i+1,n+1):
		if dp[j]==0:
			if dp[j-i]==0:
				pass
			else:
				dp[j]=1+dp[j-i]
				track[j]=i
		else:
			if dp[j-i]!=0:
				s=min(dp[j],dp[i]+dp[j-i])
				if s!=dp[j]:
					dp[j]=s
					track[j]=i

print(dp)
li=[]
print(track)
while(track[n]>0):
	li.append(track[n])
	n=n-track[n]
print(li)


