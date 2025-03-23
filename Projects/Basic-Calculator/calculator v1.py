def loop():
    a=int(input("Enter A number:"))
    c=(input("Enter the type of operation"))
    b=int(input("Enter Second number"))
    if c=="+":
        print("The sum of the numbers is:",a+b)
        loop()
    elif c=="-":
        print("The difference of the numbers is:",a-b)
        loop()
    elif c=="*":
        print("The product of the numbers is:",a*b)
        loop()
    elif c=="/":
        print("The quotient is:",a/b)
        loop()
    else:
        print("Wrong Input")
        loop()
a=int(input("Enter A number:"))
c=(input("Enter the type of operation"))
b=int(input("Enter Second number"))
if c=="+":
    print("The sum of the numbers is:",a+b)
    loop()
elif c=="-":
    print("The difference of the numbers is:",a-b)
    loop()
elif c=="*":
    print("The product of the numbers is:",a*b)
    loop()
elif c=="/":
    print("The quotient is:",a/b)
    loop()
else:
    print("Wrong Input")
    loop()
    
  
