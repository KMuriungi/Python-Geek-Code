num1 = int(input("Enter the First Number: "))
num2= int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

if ((num1>num2) & (num1>num3)):
    print(num1,"is greater than the three inputs.")
elif((num2>num1) & (num2>num3)):
    print(num2,"is greater than the three inputs.")
else:
    print(num3,"is greater than the three inputs.")