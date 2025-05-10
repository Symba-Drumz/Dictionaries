# PYTHON DICTIONARIES
# A dictionary is a collection of {key: value} pairs. They are ordered and mutable and no duplicates are allowed.

drummer_endorsements = {"Devon Taylor":"DW Drums",
                        "Clemons Poindexter":"TAMA Drums",
                        "Larnell Lewis":"Yamaha Drums",
                        "Calvin Rogers":"Pearl Drums"}

print(drummer_endorsements)

# Finding out methods and attributes of a dictionary
print(dir(drummer_endorsements))
# In depth description of the methods and attributes
print(help(drummer_endorsements))

# Getting the key of a value in the dictionary
print(drummer_endorsements.get("Clemons Poindexter"))

# Returning None if the key is not found
print(drummer_endorsements.get("Rex Hardy jr.")) # this will return None

# Using an if statement to check if the key exists
if drummer_endorsements.get("Rex Hardy jr."):
    print("Rex Hardy jr. is on the endorsement list")
else:
    print("Rex Hardy jr. is not on the endorsement list") # this will return None since the key is not found

# Adding a new key-value pair to the dictionary
drummer_endorsements.update({"Calvin Rogers":"Pearl Drums"})
print(drummer_endorsements)
# Updating an existing key-value pair in the dictionary
drummer_endorsements.update({"Calvin Rogers":"TAMA Drums"})
print(drummer_endorsements)

# Removing a key-value pair from the dictionary
drummer_endorsements.pop("Calvin Rogers")
print(drummer_endorsements)

# drummer_endorsements.popitem() removes the last inserted key-value pair; not doing that now!!
# drummer_endorsements.clear() removes all the key-value pairs from the dictionary; not doing that now!!

# Accessing only the keys in the dictionary
print(drummer_endorsements.keys())
# Accessing only the values in the dictionary
print(drummer_endorsements.values())

# Iterating through the dictionary to get only the keys
for key in drummer_endorsements.keys():
    print(key) # this will print the keys in the dictionary

# Iterating through the dictionary to get only the values
for value in drummer_endorsements.values():
    print(value) # this will print the values in the dictionary

# Returning a dictionary list of items in 2d  tuple format
print(drummer_endorsements.items())

# Iterating through the dictionary to get both the keys and values
for key, value in drummer_endorsements.items():
    print(f"{key}: {value}") # this will print the keys and values in the dictionary



