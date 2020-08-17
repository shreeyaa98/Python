from tkinter import *

class Login:
	def __init__(self,master):
		self.USERNAME=StringVar()
		self.PASSWORD=StringVar()
		self.master=master
		self.label1=Label(self.master,text="Username").grid(row=1,column=1)
		self.entry1=Entry(self.master,textvariable=self.USERNAME).grid(row=1,column=2,columnspan=2)
		self.label2=Label(self.master,text="Password").grid(row=3,column=1)
		self.entry2=Entry(self.master,textvariable=self.PASSWORD,show=*).grid(row=3,column=2,columnspan=2)
		self.button1=Button(self.master,text="Log In",command=self.login).grid(row=4,column=1)
		self.button2=Button(self.master,text="Clear",command=self.clear).grid(row=4,column=3)
		self.label4=Label(self.master,text=' ').grid(row=5,column=1)
		self.label5=Label(self.master,text=' ').grid(row=6,column=1)

	def login(self):
		self.user=self.USERNAME.get()
		self.pas=self.PASSWORD.get()
		self.label4=Label(self.master,text=self.user).grid(row=5,column=1)
		self.label5=Label(self.master,text=self.pas).grid(row=6,column=1)

	def clear(self):
		self.entry1=Entry(self.master,text=" ").grid(row=1,column=2,columnspan=2)
		self.entry2=Entry(self.master,text=" ").grid(row=3,column=2,columnspan=2)


root=Tk()
next=Login(root)
root.mainloop()