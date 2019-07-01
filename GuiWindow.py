from Tkinter import *
myGui = Tk() # Tk() is a class present in the Tkinter
myGui.title(" GREEN_TECH ")
myGui.geometry("700x500+400+100") # 500*500 - Window size (x,y)
                                    # 400+100 - displacement position(x,y)

myLabel1 = Label(text='GREEN GROCERY POINT OF SALE SYSTEM',fg='green',bg="grey").pack()
#myLabel1.pack()# >>>> its a method belonging to the class Label()


myButton1 = Button(text='Refresh',fg='black',bg="green").grid(row=1,column=0)
myButton2 = Button(text='Delete the Selected Items',fg='black',bg="green").grid(row=1,column=1)
myButton3 = Button(text='Cancel',fg='black',bg="green").grid(row=1,column=2)
myButton4 = Button(text='Enter',fg='black',bg="green").grid(row=1,column=3)
myButton5 = Button(text='Print',fg='black',bg="green").grid(row=1,column=4)


myLabel2 = Label(text='By : KITHINJI A. MURIUNGI \nAND\nPETER K. NDUNG\'U',fg='blue',bg="yellow")
myLabel2.place(x=270,y=450) # It moves the label in the position
                            # as defined by the x and y axis

'''
<<<<<<<grid(row=1, column=2)>>>>>>>>>>>>

it can be used in the same way as place()


<<<<<<<<<<<<<,sticky='w'>>>>>>>>>>>>>>

it can be used as in east - 'e' or west - 'w'

'''

myGui.mainloop()

'''it ensures the window stays
displayed when the program is executed.
its similar to the user input in the text setup
as it is in GUI'''

