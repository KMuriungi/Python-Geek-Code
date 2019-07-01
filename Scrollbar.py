from Tkinter import *

master = Tk()

scrollB = Scrollbar(master).pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollB.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)
scrollB.config(command=listbox.yview)
mainloop()