# using get to attain a value
thisdict = {
    "model":"A1",
    "car":"ford",
    "quality":"good"
}

a = thisdict["model"]
print(a)
y = thisdict.get("quality")
print(y)
z = thisdict.keys()
print(z)

# adding the color = white in the dictionary
dictionary = {
    "car":"fortuner",
    "model":"latest",
    "year":"2025"
}

x = dictionary.keys()
print(x)
dictionary["color"] = "white"
print(x)
print(dictionary)

# printing the keys and the values both
dict1 = {
    "color":"white",
    "annimal":"latest"
}

print(dict1)
x = dict1.keys()
print(x)
y = dict1.values()
print(y)
z = dict1.items()
print(z)


# Checking
if "model" in dict1:
    print("yes model is in the dict")

else:
    print("model aint in the dictionary")