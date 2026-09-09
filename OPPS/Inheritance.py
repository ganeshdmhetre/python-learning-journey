#implement is a relation 
# Code reusability
# Method Overridind
# Abstract classes
class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class Employee(Person):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    def printDetails(self):
        print(self.id)
        print(self.name)
        print(self.salary)

e=Employee(101,"ganesh",40000)
e.printDetails()
print('-'*20)
print("Types of inheritance" ,
"\nsingle" ,
"heirarichal" ,
"multipla" ,
"multilevel" ,
"hybrid",sep=",")
#-------------------#
#Multilevel inheritance
class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printDetails(self):
        print(self.name)
        print(self.id)
class Employee(Person):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    def printDetails(self):
        print(self.name)
        print(self.id)
        print(self.salary) 
class SalesEmployee(Employee):
    def __init__(self,id,name,salary,si):
        super().__init__(id,name,salary)
        self.salaryins=si
    def printDetails(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.salaryins)
sal=SalesEmployee(109,"john",35000,2000)
sal.printDetails()
print("-"*20)
# Multiple inheritace (inhereinting from two class)
class Student:
    def __init__(self,sid,dept):
        self.sid=sid
        self.dept=dept
class Faculty:
    def __init__(self,fid,dept):
        self.fid=id
        self.dept=dept

class PhdStudent(Student,Faculty):
    def __init__(self,id,dept):
        super().__init__(id,dept)

phd=PhdStudent(201,"AIML")
print(phd.sid)
 # print(phd.fid)        #this raises an error cause the data store in the student class
print(phd.dept)
#________________#
print('-'*30)
# Diamond promble 
# in which there is phd class who inherit form two classes student and faculty and these two classes are inherita from person class





