#date=7-2-2026
#type conversion
#two type of conversion implicit and explicit
#implicit
a=10
b=1.5
c=a+b
#here b float convert into integer
d=True
e=a+d
#here d boolen value convert into int (True=1,False=0)
#
#ddExplitcit one
s="134"
i=10+int(s)
#here int() is use convert into integer 
f=float(s) # this float() convert into floating values
s="geeks"
print(list(s))
print(tuple(s))
print(set(s)) #as you can see that set are unoreder , it only contain distinct elements so 'e' will not repeat
#you can convert list into string by 'str(list)', not only but any type
#tuple to list vice versa is also availabe
#_________________________________#
#ARITHEMATIC OPERATION #
x=9
y=1
print(x+y)
print(x-y)
print(x*y)
print(x/y)  #gives you answer after decimal
print(x//y)  #gives you floar means a hole number
print(x % y)  #this gives called modulus gives reminder of divsion
print(x**y)    #this give power x to the y means x raise to y
#if we use all the arithematic opreter at a time which go first 
# the order is 
print(x+y*2**x)
#precendence
#______________________________#
#LOGICAL OPERATERS #
a=10
b=20
c=30
print(a<b and b<c) # AND any one condition is false it's output is false both true o/p true
print(a<b or b<c)  # OR any one condition is true it' o/p is true both false o/p is false'
print(not a>b)    #if o/;p is true convert into the false and vice versa 
#______________________________#
#IDENTITY COMPARISION #
x=10
y=x
print(x is y)
print(x is not y)
# in case of continer values means list tuple set they gives false if the contain same literlas
# at the end it depends on the ids let check
l=[10,20,30]
l_=[10,20,30]
print(id(l),id(l_)) #id's are diff means the meaomery alocate for same list is diff
print(l is l_) # False
#_____________________#
#MEBESHIP TEST#
s="geeksfor geeks"
print("g" in s) # if the vairable s present in the string s the it gives true other wise false
print("i" not in s )
#like this you can use to chesck if the list, tuple, set,dictonary can contain the literals 
#_____________________#
# DAY BERFORE N DAYS
#reaminig
#___________________#
#PRINT() FUNCTION
print('hello')
print('welcome','to','gfg')
print()
print('i am going to complette python in july')
#end sep
print('welcome',end=' ')
print('to gfg') #end end the line with what you provide keep on that line to print another line
print('20','30','40',sep=" ,",end=" + ")
print("40,50")
#INPUT FUNCTION
t=input('enter anyting')
print(t)