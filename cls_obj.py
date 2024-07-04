
# Problem 1
# class programmer:
#     company="MicroSoft"
#     def __init__(self, name, salary, pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# p=programmer("Naveen", 12000, 432242)
# print(f"{p.company} {p.name} {p.salary} {p.pin}")


#Problem 2:

# class Calculator:
#     def __init__(self, num):
#         self.num=num
#     def square(self):
#         print(f"the square of {self.num} is {self.num**2}")
        
#     def cube(self):
#         print(f"the cube of {self.num} is {self.num**3}")
        
#     def root(self):
#         print (f"the root of {self.num} is {self.num** (1/2)}")
    
#     @staticmethod
#     def greet():
#         print("Hello there!")

# p = Calculator(9)
# p.greet()
# p.square()
# p.cube()
# p.root()



#Problem 3:
 
from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    
    def book(self, fro, to):
        print(f"your ticket for train number {self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
        print("your train is on its way")
    
    def getFare(self, fro, to):
        print(f"your fare for train number {self.trainNo} from {fro} to {to} is {randint(222,4444)}")

t = Train(32442)
t.book("Delhi", "Mumbai")
t.getstatus()
t.getFare("Delhi", "Mumbai")