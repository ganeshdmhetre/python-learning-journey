#Abstraction is the process of hiding implementation details and exposing only the essential functionality 
# to the user.
from abc import ABC,abstractmethod
class Polygon(ABC):
    def __init__(self,colour):
        self.colour=colour

    @abstractmethod
    def printsides(self):
        pass               # use because not sour with implemention

class Triangle(Polygon):
    def __init__(self,colour):
        super().__init__(colour)
    def printsides(self):
        print("there are three sides")

p=Triangle("Red")
p.printsides()

# p=Polygon("Red")       #implrmrntation of abstract calss do no possible
# p.printsides()

p=Triangle("Red")
# Decorator function
#simple way
def decfun(f):
    def innerfun():
        print("Welcome")
        f()
    return innerfun
def fun():
    print("User")
fun=decfun(fun)
fun()
#using decorator
def decfun(f):
    def innerfun():
        print("Welcome")
        f()
    return innerfun

@decfun
def fun():
    print("Ganesh")
fun()