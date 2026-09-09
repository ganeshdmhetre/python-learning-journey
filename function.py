def fun():
    print("fun() called")
print("before fun() called")
fun()
print("after fun() called")

def printDate(d,m,y):
    print(d,m,y,sep='-')
print('my date of birth is',end="=")
printDate(6,5,2008)
#by returning values
def printdate(d,m,y):
    return d
print('indepemdance date is',end='=')
d=printdate(15,8,1947)
print(d)
print()
def greet_msg():
    print('hi')
    print('welcome to functions in  python')
def exit_msg():
    print('have a nice day')
    print('bye')
greet_msg()
print('hope you are enjoying')
exit_msg()
print()
#this how function works
def fun2():
    print('inside fun2()')
def fun1():
    print("Before fun2()")
    fun2()
    print("after fun2()")
print("before fun1()")
fun1()
print("after fun1()")
print()
#default arguments
def printDetails(id,name='NA',price='NA'):
    print(f"id is {id}")
    print(f"name is {name}")
    print(f"price is{price}")
printDetails(120,'animal',80000) #this is positional (depend upon the order)
printDetails(102)
printDetails(103,'xyz')
print()
# def printDetails(id,name='NA',price)
# Raise an error
#default and keywards
def printinformation(id,name="NA",price="NA") :
    print(f"id is {id}")
    print(f"name is {name}")
    print(f"price is {price}")
printinformation(id=104,price=50000,name="abc")
printinformation(501,name="asdf")
#while we uses keyword then order is not mattter 
# without keyword order should follow 
print()
print()
def sum(*elements):    # * stand for crate a tuple name elements 
    res=0
    for x in elements :
        res = res + x
    return res
print(sum(10,20,30,40))
print(sum(20,40,60))
print(sum())
print()
def sum_(init_num,*elements): 
    res = init_num
    for x in elements :
        res =res + x
    return res
print(sum_(0,10,20,30,60,70))
print(sum_(9,))
def printDetails(**detail):
    for d,v in detail.items() :
        print(f"{d} is {v}")
printDetails(id=103,name="cjp",price="fair")
def print_detail(id,**detail):
    print(f"id is {id}")
    for d,v in detail.items() :
        print(f"{d} is {v}")
print_detail(102,name='cjp',price="right")
print()
print()
#parameters passing
def fun():
    x=15
x=10
fun()
print(x)
def fun(l):
    l.append(60)
    print(l)
l=[10,20,30]
fun(l)
print(l)
# to clear the topic
def fun(l):
    l.append(15)
    print(id(l))
l=[1,2,3,4]
fun(l)
print(id(l))
#function retuning mutiple function
def add_multiply(x,y):
    sum=x+y
    mul=x*y
    return sum,mul
s,m=add_multiply(10,30)
print(s)
print(m)
print()
def fun():
    a=10
    b=20
    print(a,b,c,d)
c,d=30,40            #this refers that we cannot acess local varible out of function
print(c,d)
print()
##
def fun():
    global x    #it makes x varible local to global
    x=10
x=15
fun()
print(x)
print()
##
def fun():
    y=x+10
    print(y)
x=90
fun()            # we can call a varible outside function inside function
print()
##To change th global varible inside a function
def fun():
    globals()['x']=20       
    print(x)
x=30                        # differce b/w global and globals
fun()                      # global is used to make an local varible into global variable
print(x)                   # globals is used to change/acess the global varible in function
print()
#to get first digit
def getfirstdigit(x):
    while x>10 :
        x=x//10
    return x
print(getfirstdigit(684654564))
#by using math library using log
import math
def get1digit(x):
    d=int(math.log10(x))
    res=x//(10**d)
    return res
x=int(input('enter a number:'))
print(get1digit(x))

