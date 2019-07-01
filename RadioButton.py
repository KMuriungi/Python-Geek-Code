from Tkinter import *

def change(): # Creating a function
    print'User =',var.get()

root = Tk() # Initialize class Tk in the module Tkinter

users = 'NEW',"OLD",'RENEW'

myFrame = Frame(relief=RAISED, borderwidth=5).pack(pady=10)

var = StringVar() # It will be holding a String Variables

for user in users:
    radio = Radiobutton(myFrame,text=user, variable=var,value=user).pack(side = TOP)

Button(root,text="Submit",command=(lambda:change())).pack()

var.set('NEW')# Initialize the set of radio buttons

mainloop()