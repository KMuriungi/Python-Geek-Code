from Tkinter import *
myGui = Tk() # Tk() is a class present in the Tkinter
myGui.title(" GREEN_TECH ")
myGui.geometry("700x500+400+100") # 500*500 - Window size (x,y)
                                    # 400+100 - displacement position(x,y)

labelTitle = Label(text='GREEN GROCERY POINT OF SALE SYSTEM',fg='green',bg="grey").pack()
#labelTitle.pack()# >>>> its a method belonging to the class Label()


#bnRefresh = Button(text='Refresh',fg='black',bg="green").pack()
bnRefresh = Button(text='Refresh',fg='black',bg="green").place(x=0,y=20)#.pack()

#bnRefresh.grid(row=1,column=0)
bnDelete = Button(text='Delete the Selected Items',fg='black',bg="green").place(x=60,y=20)#.pack()#.grid(row=1,column=1)
bnCancel = Button(text='Cancel',fg='black',bg="green").place(x=230,y=20)#.pack()#.grid(row=1,column=2)
bnEnter = Button(text='Enter',fg='black',bg="green").place(x=260,y=20)#.pack()#.grid(row=1,column=3)
bnPrint = Button(text='Print',fg='black',bg="green").place(x=340,y=20)#.pack()#.grid(row=1,column=4)

labelNames = Label(text='By : KITHINJI A. MURIUNGI \nAND\nPETER K. NDUNG\'U',fg='blue',bg="yellow")
labelNames.place(x=270,y=450) # It moves the label in the position
                            # as defined by the x and y axis

myGui.mainloop()
