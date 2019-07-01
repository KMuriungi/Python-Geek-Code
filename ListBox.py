from Tkinter import *

master = Tk()

listb = Listbox(master).pack()
listb.insert(END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listb.insert(END, item)
mainloop()