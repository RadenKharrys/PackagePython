from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
mainloop()

from tkinter import *
master = Tk()
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=0, sticky=W)