input_list,extract_list,manip_list,lst = [],[],[],[]
d={}
while True:
    input_str = input("Enter a string")
    if input_str == "":
        break
    else:
    	input_list.append(input_str)
for str in input_list:
	column,content=[],[]
	a=str.find(":")
	column.append(str[0:a])
	b=str.find(":",a+1,len(str))
	column.append(str[a+1:b])
	s=str[b+1:]
	content=s.split(",")
	column.append(content)
	extract_list.append(column)
print(extract_list)
for i in extract_list:
	a3,b3,a4,b4,a5,b5,a6,b6=0,0,0,0,0,0,0,0
	for j in i[2]:
		l=[]
		s=0
		l=j.split("-")
		a=int(l[0])
		b=int(l[1])
		if a>b:
			s+=1
			a3+=1
			b5+=1
		else:
			b3+=1
			a5+=1
		a4+=a
		b4+=b
		a6+=b
		b6+=a
	if s==3:
		a1=1
		a2=0
	else:
		a2=1
		a1=0
	if i[0] in d.keys():
		d[i[0]][0]+=a1
		d[i[0]][1]+=a2
		d[i[0]][2]+=a3
		d[i[0]][3]+=a4
		d[i[0]][4]+=a5
		d[i[0]][5]+=a6
	else:
		d[i[0]]=[a1,a2,a3,a4,a5,a6]
	if i[1] in d.keys():
		d[i[1]][2]+=b3
		d[i[1]][3]+=b4
		d[i[1]][4]+=b5
		d[i[1]][5]+=b6
	else:
		d[i[1]]=[0,0,b3,b4,b5,b6]
for i in d.keys():
	lst.append([i,d[i]])
print(lst)


