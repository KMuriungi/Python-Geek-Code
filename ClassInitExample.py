class student:
    def __init__(self,name):
        self.name = name # Initializes the name of the user
        self.attend = 0 # Initial value is always zero
        self.marks = [] # Contains empty list
        print("Welcome {} into the system.".format(name))

    def addmarks(self,mak):
        self.marks.append(mak) # By appending you are allowed to add details in the list

    def attenddays(self):
        self.attend += 1 # the value of attendance INCREMENTS by one 

    def getavg(self):
        return sum(self.marks) / len(self.marks) # getavg = GET AVERAGE



'''

>>> 
>>> s1 = student("kithinji")
Welcome kithinji into the system.
>>> s2 = student("muriungi")
Welcome muriungi into the system.
>>> s1.attend
0
>>> s1.attenddays()
>>> s1.attend
1
>>> s1.attenddays()
>>> s1.attend
2
>>> s1.marks
[]
>>> s1.addmarks(67)
>>> s1.addmarks(79)
>>> s1.addmarks(59)
>>> s1.addmarks(75)
>>> s1.marks
[67, 79, 59, 75]
>>> s1.getavg()
70
>>> 

'''
