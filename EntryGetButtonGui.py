from Tkinter import *

master = Tk()

e = Entry(master).pack()

def callback():
    print e.get()

b = Button(master, text = "Get Data", width = 10, command = callback).pack()

master.mainloop()