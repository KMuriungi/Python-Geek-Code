from Tkinter import *
import tkColorChooser

myColor = Tk()

def comColor():
    color = tkColorChooser.askcolor()
    myLabel = Label(text = "Your Choosen Color",bg = color[1]).pack()

myButton = Button(text = "Choose Color",width = 30, command = comColor).pack()

myColor.mainloop()