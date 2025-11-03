# Variables 
# def: values which are not constant or are temporary
# def: constant: constant are fixed values and can not be changed the way variables can be

x = 5
y = "john"

print(x)
print(y)
# Output: 5
# Output: john 

x = 4
x = "sally"

print(x)    # the latest value will be the ans
# output: sally

# Casting
x = str(7)
y = float(7)
z = int(7)

print(x)    # Output: 7
print(y)    # Output: 7.0   
print(z)    # Output: 7

# Get the type

x = 5
y = "john"

print(type(x))  # Output: int
print(type(y))  # Output: str

a = "tiwari"
A = "Arnav"

print(A)    # No uppercase() error will be shown as A will not overwrite a
#   Output: "Arnav"

# There are only few exceptions for variable typing

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Illegal varaible names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

x, y, z = "camel", "horse", "lion"
print(x, y, z)  #output: camel, horse, lion

x = y = z = "orrange"
print(x, y, z)  #output: orrange

# Unpacking lists
list = ["apple", "banana", "cheetah"]
x, y, z = list

print(x, y, z)      #output: apple, banana, cheetaah 

x = "python is awesome"
print(x)

y = "python"
a = "is"
b = "awesone"

print(y + a + b)    #output: python is awesome (same date types collab)

x = 15
y = "john"

print(x+y)      #output: error because diff date types cant be added

a = 10
b = 5
print(a+b)      #output: 15 [same data types]

f = "john"
x = 1

print(f, x)     #output: no error because we are not summing up we are just printing them line by line.

# Global Variables

x = "hello"

def hello():
    print("my name is", x)

hello()

# output: my name is hello 
# we can define any function from ourself 
# as well as we can import some functions from various libraries for ex: panda, random etc.

x = "my name"

def anotherone():
    x = "my only name"
    print("hello arnav is", x)

anotherone()

print("hello arnav is the", x)

#output: 1. hello arnav is my only name 
#output  2. hello arnav is the my name.

# anything added under a self defined function will be used under it even if the variable is same above the function.

