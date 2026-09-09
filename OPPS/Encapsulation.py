class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fun(self):
        print("Hi")
t=Test(10,4)
print(t.x)
print(t.y)
t.fun()
# We use underscore before varible to suggest not to use this
class Test:
    def __init__(self,x,y):
        self._x=x
        self.y=y
t=Test(10,2)
print(t._x)
print(t.y)
# we  use two underscore before the varible to make it inacessable
class Test:
    def __init__(self,x,y):
        self.__x=x
        self.y=y
    def fun(self):
        print("Hi")
t=Test(1,2)
print(t.__x)
print(t.y)
print(t._Test__x)
t._Test__fun()
#Getter and Setter

