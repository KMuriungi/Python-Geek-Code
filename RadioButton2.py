from Tkinter import *

def sel():
    selection = "You are a" + str(var.get())
    label.config(text = selection)

root = Tk()
var = IntVar()

RadioBn1 = Radiobutton(root, text = "New User", variable=var, value=1,command=sel).pack(anchor = W)

RadioBn2 = Radiobutton(root, text = "Old User", variable=var, value=2,command=sel).pack(anchor = W)

RadioBn3 = Radiobutton(root, text = "ReNew User", variable=var, value=3,command=sel).pack(anchor = W)

label = Label(root).pack()

root.mainloop()
