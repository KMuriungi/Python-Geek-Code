from Tkinter import *
root = Tk()

topFrame = Frame(root).pack()
bottomFrame = Frame(root).pack()

bnRefresh = Button(topFrame,text = "Refresh",fg = "red",width=10,height=2).pack(side = LEFT)
bnCancel = Button(topFrame, text = "Cancel",fg = "Brown",width=10,height=2).pack(side = LEFT)
bnPrint = Button(topFrame, text = "Print",fg = "blue",width=10,height=2).pack(side = LEFT)

bnDelete = Button(bottomFrame, text = "Delete",fg = "green",width=10,height=2).pack(side = LEFT)
bnNew = Button(bottomFrame, text = "New Transaction",fg = "cyan",width=15,height=2).pack(side =LEFT)
root.mainloop()