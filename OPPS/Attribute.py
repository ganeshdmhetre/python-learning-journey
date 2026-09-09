#CLASS AND INSTANCES
#class Attribute :- Shared with all objects
#Instance Attribute :- Unique to every object
class Employee:
    CompName="gfg"
    def __init__(self,id):
        self.id=id
e=Employee(101)
print(e.id)
print(e.CompName)
print(Employee.CompName)
#Guess output
e1=Employee(101)
e2=Employee(103)
Employee.CompName="geeksforgeeks"
print(e1.CompName)
print(e2.CompName)
print()
#________________#
#instances and classs attribute are can be added after creation
class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def fun(self,n):
        self.age=n
s=Student(21,"krish")
s.fun("infinite")
print(s.age)
s.designation="God"
print(s.designation)
Student.officeAdd="Dwarka"
print(s.officeAdd)
# this is only for s if make an another object s1 or s2 and you try to accces class or instance attibute which are initionalize in s object hten your are anot able to access
#_______________#
#if both class and instance attribute have same name
class Employe:
    def __init__(self,id):
        self.id=id
e=Employe(101)
print(e.id)
Employe.officeAdd="Noida"
e.officeAdd="NCR"
print(e.officeAdd)
print(Employe.officeAdd)
