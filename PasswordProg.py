password = "kithinji"
name = "Kithinji A. Muriungi"
for i in range(3):
    pwd = input("Enter the Password: ")
    j = 2
    if(pwd == password):
        print("You are Logged into the system as :",name)
        break
    else:
        print("Wrong Password, Chances left:",j-1)
        continue

print("Try Next Time!!!")