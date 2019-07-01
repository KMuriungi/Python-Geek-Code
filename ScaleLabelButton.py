from Tkinter import *

def resize(ev = None):

    label.config(font='Helvetica -%d bold' % scale.get())
top = Tk()
top.geometry('250x150')
label = Label(top, text='Hello World!',font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)
scale = Scale(top, from_=0, to=50, orient=HORIZONTAL, command=resize)
scale.set(20)
scale.pack(fill=X, expand=1)
QuitButton = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red').pack()
mainloop()