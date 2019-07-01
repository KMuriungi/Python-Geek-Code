class student:
    def details(self,name,age):
        self.name = name
        self.age = age
        print("The name is {} and the age is {}".format(name,age))

    def __init__(self): # Its used in initializing the initial values
        print("Kithinji Welcomes You")
