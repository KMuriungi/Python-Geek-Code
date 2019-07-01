name = input('Enter your Name: \n')

''' In python 2.7, input string
    values should be put in
    brackets "".
    Unlike in python 3.4
'''
age = input("Enter your Age: \n")

print("Your name is",name,"and your Age is",age)

print("\n")

a = input("Number_1 = \n")
b = input("Number_2 = \n")

print(a+b) # It prints both input values as a String in 3.4
            # But as integers in 2.7

print (int(a) + int(b))

print()
print ("Press enter to quit.")
