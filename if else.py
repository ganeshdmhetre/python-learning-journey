#if else elif
x=int(input("enter a number:"))
if x % 2==0 :
    print("entered number is even")
else :
    print("entered number is odd")
    
#___Positive, Negative , zero____#
n=int(input("enter a number"))
if n >0 :
    print("positve")
elif n <0 :
    print("negative")
else:
    print("zero")
#___to decide no. is =even, +odd,-even,-odd,zero___#
n=int(input("enter a no."))
if n >0 :
    print("positive",end=" ")
    if n %2 ==0:
        print("even")
    else:
        print("odd")
elif n <0 :
    print("Negative")
    if n %2 ==0 :
        print("even")
    else:
        print("odd")
else:
    print("zero") 
#____promblem solution___#
a=int(input("enter a number :"))
b=int(input("enter another number:"))
if a >b:
    print("a is grater then b")
elif b >a:
    print("b is greater than a")
else :
    print("a & b both are same")