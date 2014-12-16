from Tkinter import *
import datetime
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def remove():
    """
    Return current date
    """
    day = int(datetime.date.today().strftime("%d"))
    month = datetime.date.today().strftime("%B")
    year = datetime.date.today().strftime("%Y")
    date_now = "%s %s %s" % (day, month, year)
    date_now = date_now.split()
    if is_leap_year(int(date_now[2])) == True:
        feb = 29
    elif is_leap_year(int(date_now[2])) == False:
        feb = 28
    month = {'January':31, 'February':feb, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31,\
            'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
    return abs(int(date_now[0]) - month.get(date_now[1]))

def date():
    """
    Return current date
    """
    day = int(datetime.date.today().strftime("%d"))
    month = datetime.date.today().strftime("%B")
    year = datetime.date.today().strftime("%Y")
    date_now = "%s %s %s" % (day, month, year)
    return date_now

class Main():
     def __init__(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Main")
          self.main.resizable(width=FALSE, height=FALSE)
          
          #--Background--#
          photo = PhotoImage(file= 'bg1.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img = PhotoImage(file= 'start.gif')

          Button(self.main, image = bt_img, bg = '#29a3a2', relief= 'flat', command = self.new).place(x=190,y=200)

          self.main.mainloop()
     def new(self):
          self.main.destroy()
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          
          #--Background--#
          photo = PhotoImage(file= 'bg2.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img3 = PhotoImage(file= 'go_bt.gif')

          self.main.title("Enter Name")
          self.main.resizable(width=FALSE, height=FALSE)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, image = bt_img3, bg = '#29a3a2', relief= 'flat', command = self.getslary).place(x=215, y=200)
          self.main.mainloop()
          
     def getslary(self):
          self.name = self.x.get()
          self.main.destroy()
          self.slary()

     def slary(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Salary")
          
          #--Background--#
          photo = PhotoImage(file= 'bg7.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img3 = PhotoImage(file= 'go_bt.gif')
          
          self.main.resizable(width=FALSE, height=FALSE)
          self.y = Entry(self.main)
          self.y.place(x=180, y=160)
          Button(self.main, image = bt_img3, bg = '#29a3a2', relief= 'flat', command = self.getsave).place(x=215, y=200)
          self.main.mainloop()
          
     def getsave(self):
          self.slary = float(self.y.get())
          self.main.destroy()
          self.save()
          
     def save(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          
          #--Background--#
          photo = PhotoImage(file= 'bg4.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img3 = PhotoImage(file= 'go_bt.gif')
          
          self.main.title("Save")
          self.main.resizable(width=FALSE, height=FALSE)
          self.z = Entry(self.main)
          self.z.place(x=180, y=150)
          Button(self.main, image = bt_img3, bg = '#29a3a2', relief= 'flat', command = self.proceed).place(x=215, y=200)
          self.main.mainloop()

     def proceed(self):
          self.value = float(self.z.get())
          self.main.destroy()
          self.run_resultuse()
          
     '''def proceed2(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          
          #--Background--#
          photo = PhotoImage(file= 'bg5.gif')
          Label(self.main, image = photo).pack()
          
          self.main.title("New")
          self.main.resizable(width=FALSE, height=FALSE)
          self.x = Entry(self.main)
          self.x.place(x=180 , y=150)
          Button(self.main, text='Go next', command = self.resultuse, font=("Helvetica", 18)).place(x=190, y = 200)
          self.main.mainloop()
          
     def resultuse(self):
          self.value = self.x.get()
          self.main.destroy()
          self.run_resultuse()'''
          
     def run_resultuse(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.result = float(self.slary - self.value)/remove()
          #--Background--#
          photo = PhotoImage(file= 'bg6.gif')
          Label(self.main, image = photo).pack()
          Label(self.main, text = self.result, font=("Helvetica", 30)).place(x=180, y=150)
          
          #--Button-Image--#
          bt_img4 = PhotoImage(file= 'button03.gif')
          
          self.main.title("You need to use")
          self.main.resizable(width=FALSE, height=FALSE)
          Button(self.main, image = bt_img4, bg = '#29a3a2', relief= 'flat', command = self.getold).place(x=140, y=200)
          self.main.mainloop()
          
     def getold(self):
          self.value = self.x.get()
          self.main.destroy()
          self.run_old()
          
     def run_old(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          #photo = PhotoImage(file= 'bg1.gif')
          #Label(self.main, image = photo).pack()
          self.main.title("Old")
          self.main.resizable(width=FALSE, height=FALSE)
          Label(self.main, text = 'Name ' + self.name , font=("Helvetica", 30)).place(x=50, y=30)
          Label(self.main, text = 'Day' + date(), font=("Helvetica", 30)).place(x=50, y=90)
          Label(self.main, text = 'Draft', font=("Helvetica", 30)).place(x=50, y=140)
          Label(self.main, text = 'You use', font=("Helvetica", 30)).place(x=50, y=200)
          self.main.mainloop()

Main()
