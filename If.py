a = 10
b = 20
c = 30

print("It Prints only the value of \"a\" since its correct")
if(a==10):
    print(a)
elif (b==20):
    print(b)
else:
    print (c)


print("It Prints only the value of \"b\" since \"a\" is false and \"a\" is correct")
if(a==20):
    print(a)
elif (b==20):
    print(b)
else:
    print (c)


print("It Prints only the value of \"c\" since \"a\" and \"b\" are false and \"c\" is then executed")
if(a==20):
    print(a)
elif (b==30):
    print(b)
else:
    print (c)


print("It Prints all the 3 values since its indented")
if(a==10):
    print(a)
    if (b==20):
        print(b)
        if(c==30):
            print (c)
