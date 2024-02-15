"""
Dictionaries
"""

# 1
user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

print(user_dictionary)
print(user_dictionary.get("username"))

user_dictionary["married"] = True
print(user_dictionary)
print(len(user_dictionary))

# user_dictionary.pop("age")
# print(user_dictionary)

# user_dictionary.clear()
# print(user_dictionary)

# del user_dictionary

for x in user_dictionary:
    print(x)

for x, y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary2)






















