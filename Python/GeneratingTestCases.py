import random
l = set()
ip = []
op = []
while(len(l) != 10):
    l.add(random.randint(1,20))
 
while(len(l) != 20):
    l.add( random.randint(10,(10**2)))
l = list(l)

for each in range(len(l)-10):
    temp = []
    for x in range(l[each]):
        temp.append(random.randint(0, 100))
    ip.append(temp)
     
for each in range(10,20,1):
    temp = []
    for x in range(l[each]):
        temp.append(random.randint(0, 10**2))
    ip.append(temp)    
 
print(l)
INT_MIN = -32767
def fn(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j]+val[i-j-1])
        val[i] = max_val
 
    return val[n]
         
for i in range(len(l)):
    op.append(fn(ip[i],l[i]))
    print(op)

 
for y in range(10):
    st = "input0"+str(y)+".txt"
    f = open(st, "a")
    s = ""
    for k in ip[y]:
        s += str(k)
        s += " "
    f.write(str(l[y])+"\n"+s)

for y in range(10,20):
    st = "input"+str(y)+".txt"
    f = open(st, "a")
    s = ""
    for k in ip[y]:
        s += str(k)
        s += " "
    f.write(str(l[y])+"\n"+s)
    
for y in range(10):
    st = "output0"+str(y)+".txt"
    f = open(st, "w")
    f.write(str(op[y]))
    
for y in range(10,20):
    st = "output"+str(y)+".txt"
    f = open(st, "w")
    f.write(str(op[y]))
    
 
print("Done")
