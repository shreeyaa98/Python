import sqlite3
from tkinter import *

conn=sqlite3.connect('Emp.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Emp (eid integer PRIMARY KEY,name text,salary integer NOT NULL,Dno integer)")
conn.commit()
a=4
n='Azoo'
p=1000
q=6
#cur.execute("INSERT INTO Emp VALUES (?,?,?,?)",(a,n,p,q))
l=[]
cur.execute("SELECT * FROM Emp")
rows=cur.fetchall()
print(rows)
for row in rows:
	dept=row[3]
	if dept not in l:
		l.append(dept)
	print(l)

for i in l: 
	cur.execute("SELECT * FROM Emp where Dno={}".format(i))
	l1=cur.fetchall()
	print("Department",i)
	print(l1)




#cur.execute("UPDATE Emp SET salary=? WHERE eid=?",(sal,id))
#conn.commit()
cur.execute("SELECT * FROM Emp")
rows=cur.fetchall()
print(rows)
cur.close()