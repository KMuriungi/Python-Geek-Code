from Tkinter import *
import tkMessageBox

myGui = Tk()

def regLb():
    b = a.get()
    printLabel = Label(text = b, fg = "green",bg ='grey',font=12).pack()

def printLb():
    c = a.get()
    printLabel = Label(text = c, fg = "green",bg ='grey',font=12).pack()

def newFile():
    newFileLabel = myGui, Label(text = "You've Created a New File\n Kithinji A. Muriungi ",font=("roman",22,'italic')).pack()

def msgBox():
    #tkMessageBox.showinfo(title='Save',message="You Have Saved the File")

    tkMessageBox.askyesno(title="Save Confirm",message="Are you Sure you want to save this file?")

    tkMessageBox.askokcancel(title="Save Confirm", message="Click OK to Save")

    tkMessageBox.showwarning(title="Save Warning",message="This is a READ-ONLY file!!!")

def quitMsgBox():
    quitMsg = tkMessageBox.askyesno(title="Quit Confirm",message="Are you Sure you want to QUIT?")
    if quitMsg == 1:
        myGui.destroy()


a = StringVar()

myGui.title("GREEN-TECH <->Green Grocery Point Of Sale System")
myGui.geometry("500x350+400+200")

titleLabel = Label(text = "Green-Grocery Point Of Sale System", fg = "black",bg ='blue',font=('times',20,'italic')).pack()

bnReg = Button(text = "REGISTER",fg = "black",bg ='green',command = regLb,font=('arial',20,'italic')).pack()

bnPrint = Button(text = "PRINT",fg = "black",bg ='green',command = printLb,font=('algerian',20,'bold')).pack()

text = Entry(textvariable = a).pack()

myMenu = Menu()

list1 = Menu()
list1.add_command(label="New File",command = newFile)
list1.add_command(label="Open File")
#list1.add_command(label="Import File")
#list1.add_command(label="Search File")
list1.add_command(label="Save File",command = msgBox)
#list1.add_command(label="Save As File")
#list1.add_command(label="Delete File")
list1.add_command(label="Quit",command = quitMsgBox)

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
