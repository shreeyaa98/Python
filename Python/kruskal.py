edges=[['A',1,'C'],['A',8,'B'],['B',5,'C'],['B',2,'D'],['C',7,'E'],['D',2,'E'],['D',3,'F'],['E',15,'F']]
l=['A','B','C','D','E','F']
components=[ x for x in l]

def heapify(edges,start,size):
	if start > int(size//2 - 1):
		return
	else:
		if 2 * start +2 >= size:
			


