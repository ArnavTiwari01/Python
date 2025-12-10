x = ("This", "is", "tuple")
print(x)

y = list(x)

y[1] = "kiwi"
x = tuple(y)

print(x)

a = ("Cherry", "Apple", "Cake")
print(a)

b = list(a)
b.append("Baby")
a = tuple(b)
print(a)

f = ("Cherry", "Apple", "Ladki")
g = ("Ladka",)

f+=g
print(f)

a = ("Fruits", "Flower", "Flow")
b = list(a)
b.remove("Flow")
a = tuple(b)

print(a)

