#_________________________________#
#tuple data type
#These are immutable
t=(10,20,30,'gfg')
print(t)
t=()                #this is called as empty tuple
print(t)
print(type(t))
t=(10)
print(type(t))
t=(10,)            # we need to put the comma to make a tuple with single variable
print(type(t))
# some operations
t=(10,20,30,40,50)
print(t)
print(t[1])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.count(10))
print(t.index(30))
print(id(t))
