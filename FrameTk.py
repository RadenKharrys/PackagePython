from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)

greenbutton = Button(frame,text='GREEN', fg='GREEN')
greenbutton.pack(side=BOTTOM)

redbutton = Button(frame,text='RED', fg='RED')
redbutton.pack(side=BOTTOM)

brownbutton = Button(frame,text='BROWN', fg='BROWN')
brownbutton.pack(side=BOTTOM)

blackbutton = Button(frame, text='BLACK', fg='BLACK')
blackbutton.pack(side=BOTTOM)
mainloop()