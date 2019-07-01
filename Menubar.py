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

myMenu = Menu()

list1 = Menu()
list1.add_command(label="New File")
list1.add_command(label="Open File")
list1.add_command(label="Import File")
list1.add_command(label="Search File")
list1.add_command(label="Save File")
list1.add_command(label="Save As File")
list1.add_command(label="Delete File")

list2 = Menu()
list2.add_command(label="Serial Number")
list2.add_command(label="Product ID")
list2.add_command(label="Product Name")
list2.add_command(label="Product Category")
list2.add_command(label="Amount")

list3 = Menu()
list3.add_command(label="Present Report")
list3.add_command(label="Past Report")
list3.add_command(label="Weekly Report")
list3.add_command(label="Monthly Report")
list3.add_command(label="Annual report")
list3.add_command(label="Present Product in the DB")

list4 = Menu()
list4.add_command(label="Cut")
list4.add_command(label="Copy")
list4.add_command(label="Paste")
list4.add_command(label="Undo")
list4.add_command(label="Redo")
list4.add_command(label="Delete")
list4.add_command(label="Find")

list5 = Menu()
list5.add_command(label="All System")
list5.add_command(label="Current Window")
list5.add_command(label="Current Table")

list6 = Menu()
list6.add_command(label="Find Action")
list6.add_command(label="Check for Updates")
list6.add_command(label="About")


myMenu.add_cascade(label = "File",menu=list1)
myMenu.add_cascade(label = "Manual Input",menu=list2)
myMenu.add_cascade(label = "Print",menu=list3)
myMenu.add_cascade(label = "Edit",menu=list4)
myMenu.add_cascade(label = "Refresh",menu=list5)
myMenu.add_cascade(label = "Help",menu=list6)
myGui.config(menu=myMenu)

myGui.mainloop()
