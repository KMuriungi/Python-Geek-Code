from Tkinter import *

master = Tk()

w = Scale(master, from_=0, to=42).pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL).pack()

mainloop()