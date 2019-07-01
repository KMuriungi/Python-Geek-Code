from Tkinter import *

def cb():
    print"New User",var1.get()
    print"Old User",var2.get()
    print"Renew User",var3.get()

win = Tk()
myFrame = Frame(relief=RAISED, borderwidth=5).pack()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

ckButton1 = Checkbutton(myFrame, text="New",variable=var1,command=(lambda:cb())).pack(side = TOP)

ckButton2 = Checkbutton(myFrame, text="Old",variable=var2,command=(lambda:cb())).pack(side = TOP)

ckButton3 = Checkbutton(myFrame, text="Renew",variable=var3,command=(lambda:cb())).pack(side = TOP)

mainloop()