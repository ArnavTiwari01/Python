# pop -  removes a particular item from the list.
dict1 = {
    "name":'arnav',
    'age':'16',
    'sub':'pcm'
}
print(dict1)
dict1.pop("age")
print(dict1)

# # # pop item - removes the last item from the list or the latest added item 
dict1.popitem()
print(dict1)

# # del same as 'pop'
del dict1["name"]
print(dict1)

# clear - empties the whole dictionary
dict1.clear()
print(dict1)