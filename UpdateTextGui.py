from Tkinter import *
root = Tk()
val = StringVar()
label = Label(root, textvariable = val).pack()
val.set("New input from the use!")

print val.get()

root.mainloop()
