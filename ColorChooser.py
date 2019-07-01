from Tkinter import *
import tkColorChooser

myColor = Tk()

color = tkColorChooser.askcolor()
mylabel = Label(text = color).pack()

myColor.mainloop()