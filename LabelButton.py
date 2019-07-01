import Tkinter
top = Tkinter.Tk()
hello = Tkinter.Label(top, text='The Green-Grocery POS System')
hello.pack()
quit = Tkinter.Button(top, text='QUIT', command=top.quit, bg='green', fg='white')
quit.pack(fill=Tkinter.X, expand=0)# "expand" allows the text to move as
                                        #the window  expands or stay static 

Tkinter.mainloop()
