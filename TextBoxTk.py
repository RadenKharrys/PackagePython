from tkinter import

master = Tk()
label(master, text ='Nama :').grid(row=0)
label(master, text ='Alamat :').grid(row=1)
box1 = entry(master)
box2 = entry(master)
box1.grid(row=0, column=1)
box2.grid(row=1, column=1)
mainloop()