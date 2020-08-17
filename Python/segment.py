def creatree(inp,seg,low,high,pos):
	if(low==high):
		seg[pos]=inp[low]
		return
	mid=(low+high)/2
	creatree(inp,seg,low,mid,2*pos+1)
	creatree(inp,seg,mid+1,high,2*pos+2)
	seg[pos]=seg[2*pos+1]+seg[2*pos+2]
def findtree(seg,pl,ph,ql,qh,index):
	mid=(ph+pl)/2
	if(pl<=ql and ph>=qh):
		return seg[index]
	elif(pl>qh||ph<ql):
		return 1000000000
	return (findtree(seg,pl,mid,ql,qh,index)+findtree(seg,mid+1,ph,ql,qh,index))


a,b=map(int,input().split())
l=[bin(i) for i in input().split()]
f=[]
inp1=[0 for i in range(2**a)]
print(inp1)
for i in l:
    i=i[2:]
    if '11' in i:
        f.append(1)
    else:
        f.append(0)
creatree(f,inp1,0,a,0)
q=[]
for i in range(b):
    j,k=map(int,input().split())
    ans=findtree(inp1,j,k,0,a,0)
    #p=[j,k]
    #q.append(p)
    print(ans)