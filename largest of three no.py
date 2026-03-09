a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if (a >= b) and (a>=c) :
    print(a)
if (b>=a) and (b>=c):
    print(b)
if (c>=a) and (c>=b) :
    print(c)

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>=b :
    if a>=c :
        print(a)
    else :
        print(c)
else :
    if b>=c :
        print(b)
    else :
        print(c)