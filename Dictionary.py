# Dictionary: Key-Value pairs, Unordered, Mutable
# Only unmutable variable types can be used as a key: 
# number, string, tuples
my_dict = {"name": "Davyd", "age": 101, "city": "Toronto"}
print(my_dict, "\n")

# Convert variables into key/value pairs of dictionary
mydict2 = dict(name = "Oleg", age=20, occupation="Sftwr. Eng.")
print(mydict2, "\n")

# Retrieve value
value = my_dict["name"]
print(value, "\n")

# Add new key/value pair
my_dict["email"] = "email@gmail.com"
print(my_dict["email"], "\n")

# Delete
# del my_dict["email"] 
# or
my_dict.pop("email")
# or to delete last inserted item
my_dict.popitem()

# To check whether the key is in dictionary
if "name" in my_dict:
	print("it's there", "\n")

# Iterate thru dictionary keys
for key in my_dict:
	print(key)

print("\n")

# Iterate thru dictionary values
for value in my_dict.values():
	print(value)

print("\n")

# Iterate thru dictionary key/value pair
for key,value in my_dict.items():
	print(key, " ", value)

print("\n")

# Copy dictionary
my_dictCopy = my_dict.copy()
print(my_dictCopy)

