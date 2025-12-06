dict1 = {
    'hello' : 'who?',
    'name' : 'dont know'
}

# dict1.clear()
# print(dict1)

x = dict1.copy()
print(x)

x = ("key1", "key2", "key3")
y = 0

dict2 = dict.fromkeys(x, y)
print(dict2)

x = {"hello":"world",
     "my":"welcome"}

y = x.values()
print(y)