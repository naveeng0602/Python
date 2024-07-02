# p = int(input("Enter number:"))
# for i in range(10):
#     print(p, "x", i, "=", p*i)


# l = ["Harry", "Sohan", "Naveen" , "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(name)
    
  
n = int(input("Enter the number: "))

for i in range (2,n):
    if(n%i)==0:
        print("Not a prime number")
        break
    else:
        print("Prime number")
        break   