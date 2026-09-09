import sys 
print(""" Please select opration: 
      1.addition
      2.multiplication
      3.subtraaction
      """)
choice= int(input("Select opraation from 1,2&3:"))
if choice not in (1,2,3):
    print("invalid choice")
    sys.exit ()
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if choice==1:
        print("result is",a+b)
elif choice==2:
        print("result is ",a*b)
else :
        print("result is ",a-b)
