t=int(input())
while t:
    n=int(input())
    l=[int(x) for x in input().split()]
    left=0
    right=n-1
    s,h=1,1
    dummy = 2*l[right]
    if n>1:
        while(left<right):
            if(l[left]<=dummy):
                dummy-=l[left]
                left+=1
                if(left<right):
                    s+=1    
            else:
                right-=1
                if (left<right):
                    dummy+=2*l[right]
                    h+=1         
        if s>h:
            print(s,end=" ")
            print(h)
            print("Sanjana")
        elif s==h:
            print(s,end=" ")
            print(h)
            print("Tie")
        else:
            print(s,end=" ")
            print(h)
            print("Henil")
    else:
        print('1',end=" ")
        print('0')
        print("Sanjana")

    t-=1