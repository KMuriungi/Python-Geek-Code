from Tkinter import *
master = Tk()

EnterData = Entry(master).pack()
def callback():
    print EnterData.get()

