
# Problem 1:

# try:
#     with open ("file.txt", "r") as f:
#      print(f.read())
# except Exception as e:
#    print(e)
   
# try:
#     with open ("file1.txt", "r") as f:
#      print(f.read())
# except Exception as e:
#    print(e)

# try:
#     with open ("file1.txt", "r") as f:
#         print(f.read())

# except Exception as e:
#     print(e)

# print("Thanks")

# PROBLEM 2:

# l = [1,2,3,4,5,6,7,8,9]
 
# for i ,item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)


# PROBLEM 3:

# n=5
# table= [n*i for i in range(1,11)]

# print(table)

# PROBLEM 4
# try:
#     a = int(input("Enter number 1: "))
#     b = int(input("Enter number 2: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("Infinite")

# PROBLEM 5:

a = int(input("Enter the number: "))

table = [i*a for i in range(1,11)]
 
with open("table.txt", "a") as f:
    f.write(str(table)+ "\n")