#a=int(input("enter the first number of A.P:"))
#d=int(input("enter the common differnce of A.P:"))
#n=int(input("enter the required term:"))
ans=a+(n-1)*d
print("The required term is",ans)
print()
print()
#a=int(input("enter the 1st term:"))
#r=int(input("enter the common ratio:"))
#n=int(input("enter the requied term:"))
ans=a*(r**(n-1))
print("required term of G.P is",ans)
#print last digit of number
#x=input("enter a more than 3 digit num:")
list(x)
print(x[-1])
#y=int(input("enter a more than 3 digit num:"))
ld= y % 10
print(ld)
#___________________#
#if else elif
x=int(input("enter a number:"))
if (x % 2 == 0) :
    print("entered number is even")
else :
    print("entered number is odd")