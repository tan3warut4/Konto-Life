from Tkinter import *
class Main():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Main")
          self.main.resizable(width=FALSE, height=FALSE)

          Label(self.main, text = 'Konto Acount Plan', font=("Helvetica", 40)).place(x=90, y=60)

          Button(self.main, text='New User', command = self.new).place(x=140,y=200)
          Button(self.main, text='Old User', command = self.old).place(x=280,y=200)
          
          self.main.mainloop()
     def new(self):
          self.main.destroy()
          New()
     def old(self):
          self.main.destroy()
          Old()

class New():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Welcome', font=("Helvetica", 40)).place(x=90, y=30)
          Label(self.main, text = 'please enter your name', font=("Helvetica", 40)).place(x=50, y=90)
          self.x = Entry(self.main)
          self.x.place(x=50, y=200)
          Button(self.main, text='Go', command = self.getslary).place(x=50, y = 250)

     def getslary(self):
          self.main.destroy()
          Getslary()
class Getslary():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Hello!', font=("Helvetica", 40)).place(x=90, y=30)
          Label(self.main, text = 'Let me know your slary', font=("Helvetica", 40)).place(x=50, y=90)
          self.x = Entry(self.main)
          self.x.place(x=50, y=200)
          Button(self.main, text='print').place(x=50, y = 250)

          

class Old():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Old")
          self.main.resizable(width=FALSE, height=FALSE)
          
Main()
