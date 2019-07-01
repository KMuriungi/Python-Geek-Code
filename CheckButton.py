from Tkinter import *

def cb():
    print"Variable is",var.get()

win = Tk()
var = IntVar()
ckButton = Checkbutton(
    win, text = "Enable Tab",
    variable = var,
    command = (lambda:cb())
).pack()

mainloop()