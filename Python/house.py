from tkinter import *
root=Tk()

c=Canvas(root,height=500,width=500,cursor='pencil')
id1=c.create_rectangle(50,250,150,50)
id6=c.create_line(50,50,100,25)
c.pack()

root.mainloop()