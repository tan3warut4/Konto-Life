from Tkinter import *
class Main():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Main")
          self.main.resizable(width=FALSE, height=FALSE)

          Label(self.main, text = 'Main', font=("Helvetica", 30)).place(x=110, y=30)

          Button(self.main, text='New', command = self.new).place(x=10,y=200)
          Button(self.main, text='Old', command = self.old).place(x=200,y=200)
          
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

          self.x = Entry(self.main)
          self.x.pack()
          Button(self.main, text='print', command = self.prin).pack()

     def prin(self):
          print self.x.get() 
          

class Old():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Old")
          self.main.resizable(width=FALSE, height=FALSE)
          
Main()
