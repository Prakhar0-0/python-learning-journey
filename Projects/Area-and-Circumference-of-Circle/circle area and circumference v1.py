print("""TO FIND THE ARE AND CIRCUMFERENCE OF A CIRCLE""")
r=int(input("Enter the radius: "))
print("""   1: Area        2:Circumference   """)
b=int(input("Task to perform: "))
c=22/7

def circumference():
       d=2*c*r
       print("Circumference of the circle is:",d)
       
def area():
       e=c*r**2
       print("Area of the circle is:",e)


if b==2:
       circumference()
elif b==1:
       area()       
else:
     print("Input error!!")
 
       
    
    
