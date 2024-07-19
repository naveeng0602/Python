# PROBLEM 1:

# name = input("Enter the name: ")
# marks = int(input("Enter the number: "))
# phone = int(input("Enter the phone Number: "))

# p = "The name of the student is {}, his marks are {} and phone number is {}" .format(name,marks,phone)
# print(p) 

#PROBLEM 3:

# table = [str(7*i) for i in range (1,11)]

# s= "\n".join(table)
# print(s)

#PROBLRM: 4

# def divisible5(n):
#     if(n%5==0):
#         return True
#     return False

# a = [1,34,55,65,75,33,45,754,88]

# f= list(filter(divisible5,a))
# print(f)


#PROBLEM 5:
from functools import reduce
a = [1,34,55,65,75,33,45,754,88]
 

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,a))
