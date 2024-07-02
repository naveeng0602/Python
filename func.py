# # FUNCTION & RECURSION


# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)

# n = int(input("Enter the number: "))
# print(f"factorial of {n} is {factorial(n)}")

# PROBLEM 1:

# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# print(greatest(5,6,3))

# PROBLEM 2:

# def cel():
#     f = int(input("Enter the temperature in fahrenheit: "))
#     c = (f-32)*5/9
#     print(f"Temperature in celcius is {c}")

# cel()

# PROBLEM 3:

# def natural(n):
#     if(n==1):
#         return 1
#     else:
#         return n+natural(n-1)
# n = int(input("Enter the number: "))
# print(natural(n))

# PROBLEM 4:

# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# n = int(input("Enter the number: "))
# pattern(n);

#PROBLEM 5:

# def i_cm(n):
#     if(n==0):
#         return 0
#     else:
#         return n*2.54
# n=int(input("Enter the number: "))

# print(i_cm(n))


#PROBLEM 6:
 
def rem(l, word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n

l= ["Harry", "Aman","Rohan", "anup"]

n = input("Enter word: ")
print(rem(l,n))