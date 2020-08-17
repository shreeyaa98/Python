# from sys import stdin
# lines = stdin.read().splitlines()

n=[int(i) for i in input().split(" ")]
l=[int(i) for i in input().split(" ")]
r=[]
for i in range(n[1]):
	k=[]
	t=input()
	k=[int(j) for j in t.split(" ")]
	r.append(k)
def count(r1, r2):
    return len(list(x for x in l if r1 <= x <= r2))
for i in r:
	print(count(i[0],i[1]))