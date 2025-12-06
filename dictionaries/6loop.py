dict1 = {
    "color":"red",
    "name":"arnav",
    "age":"17"
    }
# keys only
for x in dict1:
    print(x)

# values only
for x in dict1:
    print(dict1[x])

for x in dict1.values():
    print(x)

for x in dict1.keys():
    print(x)

for x,y in dict1.itmes():
    print(x,y)
