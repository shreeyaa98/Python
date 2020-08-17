def check(a):
    if a=='M':
        return 1
    elif a=="R" or a=="A":
        return 2
    elif a=="D":
        return 3
    else:
        return 4

n=int(input())
m=[]
for j in range(n):
    m.append([i for i in range(n)])
for i in range(n):
    d=[]
    d=input()
    d=d.split()
    for j in range(n):
        m[i][j]=d[j]
tt=0
final=[]
last=[0,0]
i=0
j=0
l=[[i,j+1],[i+1,j],[i+1,j+1]]
for k in l:
    z=check(m[k[0]][k[1]])
    # print(m[k[0]][k[1]])
    if z==2:
        i=k[0]
        j=k[1]
        break
num=7
while(True):
    # print(last)
    # print(i,j)
    arr=[]
    if i==0:
        if j==0:
            l=[[i,j+1],[i+1,j],[i+1,j+1]]
        elif j==n-1:
            l=[[i,j-1],[i+1,j],[i+1,j-1]]
        else:
            l=[[i,j-1],[i+1,j-1],[i+1,j],[i+1,j+1],[i,j+1]]
    elif i==n-1:
        if j==0:
            l=[[i,j+1],[i-1,j],[i-1,j+1]]
        elif j==n-1:
            l=[[i,j-1],[i-1,j],[i-1,j-1]]
        else:
            l=[[i,j-1],[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1]]
    elif j==0:
        l=[[i-1,j],[i-1,j+1],[i,j+1],[i+1,j],[i+1,j+1]]
    elif j==n-1:
        l=[[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j]]
    else:
        l=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
    changed=0
    for k in l:
        if k[0]==0 and k[1]==0:
            continue
        z=check(m[k[0]][k[1]])
        if z>1:
            if last[0]==k[0] and last[1]==k[1]:
                continue
            elif z==2:
                if changed==1:
                    continue
                else:
                    last[0]=i
                    last[1]=j
                    i=k[0]
                    j=k[1]
                    changed=1
            elif z==3:
                tt=1
            else:
                arr.append(m[k[0]][k[1]])
    final.append(arr)
    if tt==1:
        break
for j in range(len(final)):
    final[j]=sorted(final[j])
    for k in final[j]:
        print(k,end=" ")
    print()
print("DESTINATION")






