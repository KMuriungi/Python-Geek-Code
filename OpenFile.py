from Tkinter import *
import tkFileDialog
a = Tk()

def myFileOpen():
    storeFile = tkFileDialog.askopenfile()
    myLabel = Label(text=storeFile).pack()

myButton = Button(text = "Open File",width = 40,command = myFileOpen).pack()

a.mainloop()