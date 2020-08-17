n=int(input())
l=[]
max=0
for j in range(n):
    k=[int(i) for i in input().split()]
    m=[int(i) for i in input().split()]
    k.append(m)
    l.append(k)
for i in l:
    m=i[1]
    sum=0
    for j in range(len(i[2])-m+1):
        if j==0:
            for k in range(m):
                sum+=i[2][k]
        else:
            sum=sum-i[2][j-1]+i[2][j+m-1]
        if sum>max:
            max=sum
    print(max)