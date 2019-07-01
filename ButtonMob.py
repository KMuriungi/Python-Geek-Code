from random import *
from sys import *
from os import *

from Tkinter import *
myGui = Tk() # Tk() is a class present in the Tkinter
myGui.title(" GREEN_TECH ")
myGui.geometry("700x500+400+100") # 500*500 - Window size (x,y)
                                    # 400+100 - displacement position(x,y)

labelTitle = Label(text='GREEN GROCERY POINT OF SALE SYSTEM',fg='green',bg="grey").pack()
#labelTitle.pack()# >>>> its a method belonging to the class Label()

#Button(font=('courier',10), text='CE',width=4,height=2, command=lambda: click('CE')).grid(row=0,column=4)
#Button(font=('courier',10), text='C',width=4,height=2, command=lambda: click('C')).grid(row=0,column=5)

def click():
    pass


bn3 = Button( font=('courier',10), text='7',width=4,height=2, command=lambda: click('7')).grid(row=5,column=4)
'''
bn4 = Button( font=('courier',10), text='8',width=4,height=2, command=lambda: click('8')).grid(row=1,column=2)
bn5 = Button( font=('courier',10), text='9',width=4,height=2, command=lambda: click('9')).grid(row=1,column=3)
bn6 = Button( font=('courier',10), text='4',width=4,height=2, command=lambda: click('4')).grid(row=2,column=1)
bn7 = Button( font=('courier',10), text='5',width=4,height=2, command=lambda: click('5')).grid(row=2,column=2)
bn8 = Button( font=('courier',10), text='6',width=4,height=2, command=lambda: click('6')).grid(row=2,column=3)
bn9 = Button( font=('courier',10), text='1',width=4,height=2, command=lambda: click('1')).grid(row=3,column=1)
bn10 = Button( font=('courier',10), text='2',width=4,height=2, command=lambda: click('2')).grid(row=3,column=2)
bn11 = Button( font=('courier',10), text='3',width=4,height=2, command=lambda: click('3')).grid(row=3,column=3)
bn12 = Button( font=('courier',10), text='0',width=4,height=2, command=lambda: click('0')).grid(row=4,column=1)
'''
#Button( font=('courier',10), text='+/‐',width=4,height=2, command=lambda: click('+/‐')).grid(row=4,column=2)
#Button( font=('courier',10), text='.',width=4,height=2, command=lambda: click('.')).grid(row=4,column=3)

labelNames = Label(text='By : KITHINJI A. MURIUNGI \nAND\nPETER K. NDUNG\'U',fg='blue',bg="yellow")
labelNames.place(x=270,y=450) # It moves the label in the position
                            # as defined by the x and y axis

myGui.mainloop()
