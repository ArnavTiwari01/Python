#nested dictionaries
child1 = {
    'name':'arnav',
    'age':'17'
}

child2 = {
    'name':'anshi',
    'age':'22'
}

myfamily = {
    "c1" : child1,
    "c2" : child2
}

print(myfamily)

#printing specific
print(myfamily["c2"]["name"])

