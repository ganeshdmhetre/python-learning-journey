#implicit conversion
a=10
b=1.3
c=a+b
print(c)
d=True
e=a+d
print(e)
#____________________#
#explicit function
s="135"
i=10+int(s)           # we can convert the strint into integer alo in float ,a boolen-int 
f=float(s)            # using str int float
print(i)
print(f)
#____________#
s='geeks'
print(list(s))            # we can convert by uaing list , tuple ,set
print(tuple(s))
print(set(s))
l=['g','e','e','k']
print(str(l))
a=10
b=22
print(str(a)+str(b))     # here when two string are added tehn they both get concantented
c=12.5 
print(str(c))
#______________#
t=(10,20,30)
print(list(t))
s={10,20,30}
print(list(s))
