#Classs and Object
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def print(self):
        print(str(self.real)+"+i"+str(self.img))
    def add(self,c):
        self.real+=c.real
        self.img+=c.img
c1=Complex(5,20)
c1.print()
c2=Complex(50,60)
c1.add(c2)
c1.print()
print()
#_________________#
#__STR()__ Methosd
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age                       #__str()__ it allows us to coustom string representation
    def __str__(self):      
        return f"{self.name} is {self.age} year old"
d=Dog("tommy",3)
print(d)