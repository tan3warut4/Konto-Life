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
          Button(self.main, text='Go next', command = self.getsave).place(x=50, y = 250)
     def getsave(self):
          self.main.destroy()
          Getsave()

class Getsave():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'In the end of the month ', font=("Helvetica", 40)).place(x=50, y=30)
          Label(self.main, text = 'You want to safe', font=("Helvetica", 40)).place(x=50, y=90)
          self.x = Entry(self.main)
          self.x.place(x=50, y=200)
          Button(self.main, text='Go next', command = self.proceed).place(x=50, y = 250)

     def proceed(self):
          self.main.destroy()
          Proceed()
class Proceed():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Let me Proceed ', font=("Helvetica", 40)).place(x=50, y=30)
          self.x = Entry(self.main)
          self.x.place(x=50, y=200)
          Button(self.main, text='Go next', command = self.resultuse).place(x=50, y = 250)
     def resultuse(self):
          self.main.destroy()
          Resultuse()
class Resultuse():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'You need to Use', font=("Helvetica", 40)).place(x=50, y=30)
          self.x = Entry(self.main)
          self.x.place(x=50, y=200)
          Button(self.main, text='Let start save monney', command = self.old).place(x=50, y = 250)
     def old(self):
          self.main.destroy()
          Old()

class Old():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Old")
          self.main.resizable(width=FALSE, height=FALSE)
          
Main()
