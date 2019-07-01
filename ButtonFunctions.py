from Tkinter import *

myGui = Tk()

def regLb():
    b = a.get()
    printLabel = Label(text = b, fg = "green",bg ='grey',font=12).pack()

def printLb():
    c = a.get()
    printLabel = Label(text = c, fg = "green",bg ='grey',font=12).pack()

a = StringVar()

myGui.title("GREEN-TECH <->Green Grocery Point Of Sale System")
myGui.geometry("500x350+400+200")

titleLabel = Label(text = "Green-Grocery Point Of Sale System", fg = "black",bg ='blue',font=12).pack()

bnReg = Button(text = "REGISTER",fg = "black",bg ='green',command = regLb,font=12).pack()

bnPrint = Button(text = "PRINT",fg = "black",bg ='green',command = printLb,font=12).pack()

text = Entry(textvariable = a).pack()

myGui.mainloop()
