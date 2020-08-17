# cook your dish here
n=int(input())
m=[]
t=[]
def check(a):
    if a=='L' or a=='R':
        return 1
    elif a=="S":
        return 2
    else:
        return 0
    
for i in range(n):
    m=[]
    d=[]
    d=[int(k) for k in input().split()]
    m.append(d)
    for j in range(d[0]):
        r=input()
        r=list(r)
        m.append(r)
    l=input()
    l=list(l)
    l.append("S")
    m.append(l)
    t.append(m)
print(t)
for i in t:
    print(i[i[0][0]+1])
    last=i[i[0][0]+1][0]
    for j in range(1,len(i[-1])+1):
        if check(i[i[0][0]+1][j])==check(last):
            last=i[i[0][0]+1][j]
            print("Verified")
            pass
        else:
            if last=="L":
                for r in range(1,i[0][0]+1):
                    cnt=i[r].count('1')
                    for h in range(cnt):
                        i[r][h]='1'
                    for q in range(cnt,i[0][1]):
                        i[r][q]='0'
            elif last=="R":
                for r in range(1,i[0][0]+1):
                    cnt=i[r].count('1')
                    for h in range(i[0][1]-cnt):
                        i[r][h]='0'
                    for q in range(i[0][1]-cnt,i[0][1]):
                        i[r][q]='1'
                for r in range(1,i[0][0]+1):
                    print(i[r])
                print("Done")
            elif last=="U":
                for col in range(i[0][1]):
                    cnt=0
                    for rw in range(1,i[0][0]+1):
                        if i[rw][col]=='1':
                            cnt+=1
                    for h in range(1,cnt+1):
                        i[h][col]='1'
                    for h in range(cnt,i[0][0]+1):
                        i[h][col]='0'
                print("Execute")
                for r in range(1,i[0][0]+1):
                    print(i[r])
                print("WHy")
            else:
                for col in range(i[0][1]):
                    cnt=0
                    for r in range(1,i[0][0]+1):
                        if i[r][col]=='1':
                            cnt+=1
                    for h in range(1,i[0][0]-cnt+1):
                        i[h][col]='0'
                    for h in range(i[0][0]-cnt+1,i[0][0]+1):
                        i[h][col]='1'

            last=i[i[0][0]+1][j]
    for r in range(1,i[0][0]+1):
        # for c in range(i[0][1]):
        #     print(i[r][c],endl="")
        print(i[r])
                        
            
        