
class Employee:
    compName="gfg"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def setcompName(cls,cName):
        cls.compName=cName



Employee.setcompName("Aethon")
print(Employee.compName)
e=Employee("Ganesh",21)
print(e.compName)


from datetime import date
class Employee:
    compName="gfg"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def getfromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

e=Employee.getfromBirthYear("Ganesh",2008)
print(e.name)
print(e.age)

# Static method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def isAdult(age):
        return (age > 18)

    def printDetails(self):
        print(self.name)
        print(self.age)
        print(Person.isAdult)

p=Person("Ganesh",18)
p.printDetails()
print(Person.isAdult(22))