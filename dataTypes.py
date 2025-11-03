# Data Types

"""
    Text Type: 	str
    Numeric Types: 	int, float, complex
    Sequence Types: 	list, tuple, range
    Mapping Type: 	dict
    Set Types: 	set, frozenset
    Boolean Type: 	bool
    Binary Types: 	bytes, bytearray, memoryview
    None Type: 	NoneType

"""

# Python Numbers
x = 10
print(type(x))  #output: int


x = 1.10
print(type(x))  #output: float

x = 45e3
y = 122e4

print(type(x, y))   #output: float
# float can also be donoted by 'e' as it means to the power 10.

x = 34+5j
y = -5j

print(type(x, y)) #output: complex
# complex number always have 'j' as a letter in their word  behind

# Python casting

x = int(2.0)
y = int(2j)
z = int("2")

print(x, y, z)

# output: 2,2,2
# in casting we can change the date type of any variable we want to.
