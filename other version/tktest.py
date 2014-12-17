from Tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("NAME")
f = open("data.txt", "r")
lines = f.read().split('\n')
for i in xrange(len(lines)):
    lines[i] = lines[i].split()
f.close()
lis = []
for i in xrange(len(lines)-1):
    lis.append(lines[i][0])

def var():
    w = OptionMenu(master, variable, *tuple(lis)).pack()
var()
mainloop()
