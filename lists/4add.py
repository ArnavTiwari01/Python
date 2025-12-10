list1 = ["apple", "banana"]
list1.append("cake")
print(list1)
# adds up to the last

list1.insert(1, "pizza")
print(list1)
# adds to a particular index

thislist = ["apple", "banana", "cherry"]
fruits = ["tropical", "seasonal", "flavored"]

fruits.extend(thislist)
print(fruits)

# could be used in tuples too