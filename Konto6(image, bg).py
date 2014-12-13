from Tkinter import *
import sqlite3

class Main():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Main")
          self.main.resizable(width=FALSE, height=FALSE)
          x = PhotoImage(file= 'bg1.gif')
          Label(self.main, image = x).pack()

          Label(self.main, text = 'Konto Acount Plan', font=("Helvetica", 30)).place(x=100, y=60)

          Button(self.main, text='New User', command = self.new, font=("Helvetica", 15)).place(x=140,y=200)
          Button(self.main, text='Old User', command = self.old, font=("Helvetica", 15)).place(x=280,y=200)

          self.main.mainloop()
     def new(self):
          self.main.destroy()
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Welcome', font=("Helvetica", 30)).place(x=160, y=30)
          Label(self.main, text = 'please enter your name', font=("Helvetica", 25)).place(x=80, y=80)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go', command = self.getslary, font=("Helvetica", 18)).place(x=215, y = 200)

     def getslary(self):
          self.name = self.x.get()
          self.main.destroy()
          self.slary()

     def slary(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Hello!', font=("Helvetica", 30)).place(x=198, y=30)
          Label(self.main, text = 'Let me know your salary', font=("Helvetica", 25)).place(x=80, y=90)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go', command = self.getsave, font=("Helvetica", 18)).place(x=215, y = 200)
     def getsave(self):
          self.slary = self.x.get()
          self.main.destroy()
          self.save()
     def save(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'In the end of the month ', font=("Helvetica", 30)).place(x=60, y=30)
          Label(self.main, text = 'You want to safe', font=("Helvetica", 30)).place(x=110, y=90)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go next', command = self.proceed, font=("Helvetica", 18)).place(x=190, y = 200)

     def proceed(self):
          self.value = self.x.get()
          self.main.destroy()
          self.proceed2()
     def proceed2(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Let me Proceed ', font=("Helvetica", 40)).place(x=60, y=50)
          self.x = Entry(self.main)
          self.x.place(x=180 , y=150)
          Button(self.main, text='Go next', command = self.resultuse, font=("Helvetica", 18)).place(x=190, y = 200)
     def resultuse(self):
          self.value = self.x.get()
          self.main.destroy()
          self.run_resultuse()
     def run_resultuse(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'You need to Use', font=("Helvetica", 40)).place(x=50, y=50)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Let start save monney', command = self.getold, font=("Helvetica", 15)).place(x=130, y = 200)
     def getold(self):
          self.value = self.x.get()
          self.main.destroy()
          self.run_old()
          
     def run_old(self):
          c.execute("INSERT INTO stocks VALUES (1, 'test', 200, 200, 1)")
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Old")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Name ' + self.name , font=("Helvetica", 40)).place(x=50, y=30)
          Label(self.main, text = 'Day', font=("Helvetica", 40)).place(x=50, y=90)
          Label(self.main, text = 'Draft', font=("Helvetica", 40)).place(x=50, y=140)
          Label(self.main, text = 'You use', font=("Helvetica", 40)).place(x=50, y=200)

     def old(self):
          self.main.destroy()
          Old()
     

class New():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Welcome', font=("Helvetica", 30)).place(x=160, y=30)
          Label(self.main, text = 'please enter your name', font=("Helvetica", 25)).place(x=80, y=80)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go', command = self.getslary, font=("Helvetica", 18)).place(x=215, y = 200)

     def getslary(self):
          self.main.destroy()
          #Getslary()
class Getslary():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Hello!', font=("Helvetica", 30)).place(x=198, y=30)
          Label(self.main, text = 'Let me know your salary', font=("Helvetica", 25)).place(x=80, y=90)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go', command = self.getsave, font=("Helvetica", 18)).place(x=215, y = 200)
     def getsave(self):
          slary = self.x.get()
          self.main.destroy()
          #Getsave()

class Getsave():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'In the end of the month ', font=("Helvetica", 30)).place(x=60, y=30)
          Label(self.main, text = 'You want to safe', font=("Helvetica", 30)).place(x=110, y=90)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go next', command = self.proceed, font=("Helvetica", 18)).place(x=190, y = 200)

     def proceed(self):
          self.value = self.x.get()
          self.main.destroy()
          #Proceed()
class Proceed():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Let me Proceed ', font=("Helvetica", 40)).place(x=60, y=50)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Go next', command = self.resultuse, font=("Helvetica", 18)).place(x=190, y = 200)
     def resultuse(self):
          self.value = self.x.get()
          self.main.destroy()
          #Resultuse()
class Resultuse():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'You need to Use', font=("Helvetica", 40)).place(x=50, y=50)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, text='Let start save monney', command = self.old, font=("Helvetica", 15)).place(x=130, y = 200)
     def old(self):
          self.value = self.x.get()
          self.main.destroy()
          #Old()

class Old():
     def __init__(self):
          print name
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Old")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Name' + name , font=("Helvetica", 40)).place(x=50, y=30)
          Label(self.main, text = 'Day', font=("Helvetica", 40)).place(x=50, y=90)
          Label(self.main, text = 'Draft', font=("Helvetica", 40)).place(x=50, y=140)
          Label(self.main, text = 'You use', font=("Helvetica", 40)).place(x=50, y=200)

conn = sqlite3.connect('test.db')
c = conn.cursor()

def _init():
     #c.execute('''CREATE TABLE stocks
     #        (id, name, slary, save, month)''')
     c.execute("INSERT INTO stocks VALUES (1, 'test', 200, 200, 1)")
     conn.commit()
_init()
for row in c.execute('SELECT * FROM stocks'):
        print row
Main()
