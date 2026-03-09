x=10
y=20
temp=x
x=y
y=temp
print(x)
print(y)
#another
x=100
y=200
x,y=y,x
print(x)
print(y)
#____________________________________#
#ID function
print(id("geeksforgeeks"))
z="yz"
y="yz"
print(id(z))
print(id(y))
print(id(5))
a=10
b=10
print(a is b)
c=a
print(b is c)
c=20
print(b is c)
#____________________________________#
#Type function
a=10
print(type(a))
b=3.9
print(type(b))
c='hype'
print(type(c))
d=2+4j
print(type(d))
