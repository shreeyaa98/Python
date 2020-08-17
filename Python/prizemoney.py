from math import gcd  
t=int(input())
for o in t:
	n=int(input())
	l=[int(j) for j in input().split()]
	lcm = l[0]
	for j in l[1:]:
  		lcm = lcm*j/gcd(lcm,j)
  	dp=[0 for i in range(lcm+1)]
  	for i in l:
		dp[i]=1
		for j in range(i+1,lcm+1):
			if dp[j]==0:
				if dp[j-i]==0:
					pass
				else:
					dp[j]=1+dp[j-i]
			else:
				s=min(dp[j],dp[i]+dp[j-i])
				if s!=dp[j]:
					dp[j]=s
	for i in range(max(l)+1,lcm+1):
		if dp[i]==0:
			print(i)
			break
	else:
		print("Fake Offer!")

