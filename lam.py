# square = lambda x:x*x
# print(square(4))

#problem2 
# JOIN
# a = ["name", "age","Class"]

# final = "--".join(a)
# print(final)


# MAP, FILTER, REDUCE
# MAP

from functools import reduce
l= [1,2,3,4,5,6]

square = lambda x : x*x
sqList = map(square,l)
print(list(sqList))

# FILTER

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

# REDUCE

def sum(a,b):
    return a+b
mul = lambda x,y: x*y
print(reduce(mul,l))
print(reduce(sum,l))