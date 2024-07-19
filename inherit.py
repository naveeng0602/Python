# PROBLRM 1:

# class TwoD:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#             print(f"the vector is {self.x} + {self.y}")

# class ThreeD(TwoD):
#     def __init__(self, x, y,z):
#         super().__init__(x, y)
#         self.z = z
    
#     def show(self):
#          print(f"the vector is {self.x} + {self.y} + {self.z}")


# a = TwoD(2,5)
# a.show()

# b = ThreeD(4,5,2)
# b.show()


# PROBLEM 2:

# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print(f"BHOW BHOW!")


# d = Dog()
# d.bark()


# Problem 3:


# class Employee:
#     salary = 234
#     increment = 20
#     @property
#     def salaryAfterIncreament(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncreament.setter
#     def salaryAfterIncreament(self, salary):
#         self.increment = ((salary/self.salary) -1)* 100


# e= Employee()
# e.salaryAfterIncreament = 280.8
# print(e.increment)


# Problem 4:

# class Complex:
#     def __init__(self, r, i):
#         self.r= r
#         self.i= i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return Complex(real, imag)


#     def __str__(self):
#         return f"{self.r}i + {self.i}i"
    

# c1= Complex(1,2);
# c2 = Complex(3,4)

# print(c1 + c2)
# print(c1*c2)