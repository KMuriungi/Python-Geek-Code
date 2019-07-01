class person: # The Main class with the major functions
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Name is {} and Age is {}.".format(self.name,self.age))

class teacher(person): # Class inheritance
    def print(self,name,age): # it also inherits the arguments in the previous class
        person.__init__(self,name,age) # To initialize the values

class student(person): # Class inheritance
    def print(self,name,age): # it also inherits the arguments in the previous class
        person.__init__(self,name,age) # To initialize the values