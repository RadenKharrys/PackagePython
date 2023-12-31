from tkinter import *

root = Tk()
menu = Menu(root)

root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

optionsmenu = Menu(menu)
menu.add_cascade(label='Options', menu=optionsmenu)
optionsmenu.add_command(label='Settings')
optionsmenu.add_command(label='Privacy')
optionsmenu.add_separator()
optionsmenu.add_command(label='Exit', command=root.quit)

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Tool Windows')
viewmenu.add_command(label='Appearance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Definiton')
viewmenu.add_command(label='Quick Type Definition')
viewmenu.add_command(label='Prameter Info')
viewmenu.add_command(label='Type Info')
viewmenu.add_command(label='Context Info')
viewmenu.add_command(label='Recent File')
viewmenu.add_command(label='Recently Changed Files')
viewmenu.add_separator()
viewmenu.add_command(label='Exit', command=root.quit)
mainloop()