class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.balance = 0
        self.credit = 30

        print("The name is {} and the age is {}".format(name,age))


'''
SHOWS THE WHOLE PROCESS OF INITIALIZING CLASS VALUES
WITH THE USE OF __INIT__()

>>> s = student('muriungi',22)
The name is muriungi and the age is 22
>>> s.name
'muriungi'
>>> s.age
22
>>> s.balance
0
>>> s.credit
30
>>> 

'''

