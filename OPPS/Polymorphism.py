# Polymorphism means having methods with same name but differnt data 
# MethodOverridding Derived class has samee name and parameters
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printDetails(self):
        print(self.id)
        print(self.name)
class SalesEmployee(Employee):
    def __init__(self,id,name,sid):
        super().__init__(id,name)
        self.salesins=sid
    def printDetails(self):
        print(self.salesins)
        print(self.id)
        print(self.name)

e1=[Employee(101,"ganesh"),SalesEmployee(102,"john",400)]
for i in e1:
    i.printDetails()

# Polyorphism in unrelated class
class employee:
    def fun(self):
        print("fun() of Employee")

class coustomer:
    def fun(self):
        print("fun() of customer")

l=[employee(),coustomer()]
for i in l:
    i.fun()