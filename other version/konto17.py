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
          self.lis_name = []
          #--Background--#
          photo = PhotoImage(file= 'bg1.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img = PhotoImage(file= 'button01.gif')
          bt_img2 = PhotoImage(file= 'button02.gif')
          bt_img7 = PhotoImage(file= 'bt_reset.gif')

          Button(self.main, image = bt_img, bg = '#29a3a2', relief= 'flat', command = self.new).place(x=100,y=200)
          Button(self.main, image = bt_img2, bg = '#29a3a2', relief= 'flat', command = self.old).place(x=280,y=200)
          Button(self.main, image = bt_img7, bg = '#29a3a2', relief= 'flat', command = self.reset_all).place(x=190, y=300)
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
          bt_img6 = PhotoImage(file= 'back.gif')

          self.main.title("Enter Name")
          self.main.resizable(width=FALSE, height=FALSE)
          self.x = Entry(self.main)
          self.x.place(x=180, y=150)
          Button(self.main, image = bt_img3, bg = '#29a3a2', relief= 'flat', command = self.writename).place(x=215, y=200)
          Button(self.main, image = bt_img6, bg = '#29a3a2', relief= 'flat', command = self.ready__init__).place(x=360, y=300)
          self.main.mainloop()
          
     def old(self):
         self.main.destroy()
         self.run_old()
         
     def writename(self):
          self.name_1 = str(self.x.get())
          f = open('data.txt', 'a+')
          f.write( self.name_1 +' ')
          self.lis_name.append(str(self.x.get()))
          f.close()
          self.main.destroy()
          self.slary2()

     def ready__init__(self):
         self.main.destroy()
         self.__init__()

     def reset(self):
         f = open("data.txt", "r")
         lines = f.read().split('\n')
         f.close()
         f = open('data.txt', 'w').close()
         f = open("data.txt", "a+")
         for i in xrange(len(lines)-1):
             lines[i] = lines[i].split()
             print lines
             if lines[i][0] != self.name_1:
                 f.write(lines[i][0] + ' ' + lines[i][1] + ' ' + lines[i][2] + ' ' + lines[i][3] + "\n")
         f.close()
         self.new()
         
     def reset_all(self):
         f = open('data.txt', 'w').close()
         self.main.destroy()
         self.__init__()
         
     def slary2(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Salary")
          
          #--Background--#
          photo = PhotoImage(file= 'bg7.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img3 = PhotoImage(file= 'go_bt.gif')
          bt_img6 = PhotoImage(file= 'back.gif')
          
          self.main.resizable(width=FALSE, height=FALSE)
          self.y = Entry(self.main)
          self.y.place(x=180, y=160)
          Button(self.main, image = bt_img3, bg = '#29a3a2', relief= 'flat', command = self.getsave).place(x=215, y=200)
          Button(self.main, image = bt_img6, bg = '#29a3a2', relief= 'flat', command = self.reset).place(x=360, y=300)
          self.main.mainloop()
          
     def getsave(self):
          f = open('data.txt', 'a+')
          self.slary = float(self.y.get())
          f.close()
          self.main.destroy()
          self.savel()
          
     def savel(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          
          #--Background--#
          photo = PhotoImage(file= 'bg4.gif')
          Label(self.main, image = photo).pack()

          #--Button-Image--#
          bt_img3 = PhotoImage(file= 'go_bt.gif')
          bt_img6 = PhotoImage(file= 'back.gif')
          
          self.main.title("Save")
          self.main.resizable(width=FALSE, height=FALSE)
          self.z = Entry(self.main)
          self.z.place(x=180, y=150)
          Button(self.main, image = bt_img3, bg = '#29a3a2', relief= 'flat', command = self.proceed).place(x=215, y=200)
          Button(self.main, image = bt_img6, bg = '#29a3a2', relief= 'flat', command = self.reset).place(x=360, y=300)
          self.main.mainloop()
          

     def proceed(self):
          f = open('data.txt', 'a+')
          self.value = float(self.z.get())
          f.write(str(self.z.get())+' ')
          f.close()
          self.main.destroy()
          self.run_resultuse()
          
          
     def run_resultuse(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.result = '%.2f' % (float(self.slary - self.value)/remove())
          #--Background--#
          photo = PhotoImage(file= 'bg6.gif')
          Label(self.main, image = photo).pack()
          Label(self.main, text = self.result, bg = '#29a3a2', fg = 'white', font=("Helvetica", 30)).place(x=180, y=150)
          
          #--Button-Image--#
          bt_img4 = PhotoImage(file= 'button03.gif')
          bt_img6 = PhotoImage(file= 'back.gif')
          
          self.main.title("You need to use")
          self.main.resizable(width=FALSE, height=FALSE)
          Button(self.main, image = bt_img4, bg = '#29a3a2', relief= 'flat', command = self.getold).place(x=140, y=200)
          Button(self.main, image = bt_img6, bg = '#29a3a2', relief= 'flat', command = self.reset).place(x=360, y=300)
          self.main.mainloop()
          
     def getold(self):
          f = open('data.txt', 'a+')
          f.write(str(self.result)+' ')
          f.write(str(int(self.slary - self.value)) + "\n")
          f.close()
          self.main.destroy()
          self.run_old()
          
     def run_old(self):
          self.main = Tk()
          self.main.geometry("500x400+500+100")
          self.main.title("Select Name")
          self.main.resizable(width=FALSE, height=FALSE)
          self.variable = StringVar(self.main)
          self.variable.set("NAME")

          #--Background--#
          photo = PhotoImage(file= 'name_bg.gif')
          Label(self.main, image = photo).pack()
          
          #--Button-Image--#
          bt_img4 = PhotoImage(file= 'go_bt.gif')
          
          f = open("data.txt", "r")
          lines = f.read().split('\n')
          for i in xrange(len(lines)):
              lines[i] = lines[i].split()
          f.close()
          lis = []
          for i in xrange(len(lines)-1):
              lis.append(lines[i][0])
          self.w = OptionMenu(self.main, self.variable, *tuple(lis)).place(x=220, y=170)
          Button(self.main, image = bt_img4, bg = '#29a3a2', relief= 'flat', command = self.var).place(x=220, y=300)
          self.main.mainloop()
          
     def var(self):
         self.sent = str(self.variable.get())
         f = open("data.txt", "r")
         lines = f.read().split('\n')
         for i in xrange(len(lines)-1):
             lines[i] = lines[i].split()
         for i in xrange(len(lines)-1):
             if lines[i][0] == self.sent:
                 self.save = lines[i][1]
                 self.draft = lines[i][2]
                 self.left = lines[i][3]

         f.close()
         self.main.destroy()
         self.run_last()

     def run_last(self):
         self.main = Tk()
         self.main.geometry("500x400+500+100")
         self.main.title("Last")
         self.main.resizable(width=FALSE, height=FALSE)

         #--Background--#
         photo = PhotoImage(file= 'bg_account.gif')
         Label(self.main, image = photo).pack()
         
         #--Button-Image--#
         bt_img4 = PhotoImage(file= 'go_bt.gif')
          
         self.t = Entry(self.main)
         self.t.place(x=295, y=295)
         Button(self.main, image = bt_img4, bg = '#29a3a2', relief= 'flat', command = self.get_use).place(x=420, y=340)
         Label(self.main, text =  str(remove()), font=("Helvetica", 30), bg = '#29a3a2', fg = 'white').place(x=300, y=60)
         Label(self.main, text =  str(self.left) , font=("Helvetica", 30), bg = '#29a3a2', fg = 'white').place(x=300, y=120)
         Label(self.main, text =  str(self.save) , font=("Helvetica", 30), bg = '#29a3a2', fg = 'white').place(x=300, y=170)
         Label(self.main, text =  str(self.draft) ,font=("Helvetica", 30), bg = '#29a3a2', fg = 'white').place(x=300, y=220)
         self.main.mainloop()
         
     def get_use(self):
         self.got = self.t.get()
         self.main.destroy()
         self.use()

     def use(self):
         self.main = Tk()
         self.main.geometry("500x400+500+100")
         self.main.title("Last")
         self.main.resizable(width=FALSE, height=FALSE)

         #--Background--#
         photo = PhotoImage(file= 'bg_next.gif')
         Label(self.main, image = photo).pack()

         #--Button-Image--#
         bt_img5 = PhotoImage(file= 'bt_end.gif')
         
         self.leftupdate = '%.2f' % (float(self.left) - float(self.got))
         self.can = '%.2f' % ((float(self.left) - float(self.got))/(remove() - 1))
         Button(self.main, image = bt_img5, bg = '#29a3a2', relief= 'flat', command = self.get__init__).place(x=390, y=340)
         Label(self.main, text = str(self.can), font=("Helvetica", 30), bg = '#29a3a2', fg = 'white').place(x=190, y=170)

         self.main.mainloop()
     def get__init__(self):
         f = open("data.txt", "r")
         lines = f.read().split('\n')
         f.close()
         f = open('data.txt', 'w').close()
         f = open("data.txt", "a+")
         for i in xrange(len(lines)-1):
             lines[i] = lines[i].split()
             print lines
             if lines[i][0] != self.sent:
                 print "unchange"
                 f.write(lines[i][0] + ' ' + lines[i][1] + ' ' + lines[i][2] + ' ' + lines[i][3] + "\n")
             else:
                 print "change"
                 f.write((lines[i][0] + ' ' + lines[i][1] + ' ' + self.can +' ' + self.leftupdate) + "\n")
         f.close()
         
         self.main.destroy()
         self.__init__()

Main()
