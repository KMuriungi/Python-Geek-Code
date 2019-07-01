import Tkinter
from Tkconstants import *
Green_Tech = Tkinter.Tk()
frame = Tkinter.Frame(Green_Tech, relief=RIDGE, borderwidth=5)
frame.pack(fill=BOTH,expand=5)
label = Tkinter.Label(frame, text="Hello, \n KIthinji \n Muriungi")
label.pack(fill=X, expand=5)
button = Tkinter.Button(frame,text="Exit",command=Green_Tech.destroy)
button.pack(side=BOTTOM)
Green_Tech.mainloop()

