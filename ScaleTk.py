from tkinter import *

layout = Tk()
s = Scale(layout, from_=0, to=100)
s.pack()
s = Scale(layout, from_=0, to=100, orient=HORIZONTAL)
s.pack()
mainloop()