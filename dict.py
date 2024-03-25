#                              Dictionary in Python
# Dictionary is a collection of key value pairs, it is mutable, ordered(used to be unordered before python version 3.7), indexed
# Dictionary is defined by values separated by comma inside braces { }, written as key:value.
# Key is the unique identifier for the value. Value is the data that is stored in the dictionary
# Dictionary can have any data type as key and value, can have multiple key value pairs
# Dictionary can have nested dictionary, list, tuple, set as value

info = {
    "name": "Dhruv",
    "age": 20,
    "country": "India",
}  # name, age, country are keys and Dhruv, 20, India are values
print(info)
print(info["name"])
print(
    info.get("name")
)  # get method is used to get the value of the key both are same line 10 and 11
# using get method if the key is not present in the dictionary then it will return None instead of error. Eg:
print(info.get("city"))  # None

# Accessing multiple values at the same time
print(info.keys())

# or using for
for key in info.keys():
    # print(info[key])
    # making the output look better using fstream:
    print(f"The value coreesponding to the key {key} is {info[key]}")


info2 = {"name": "Atisha", "Age": 20, "Country": "Spain"}
print(info2.items())  # use this or use the for loop:
for key, value in info2.items():
    print(f"the value corrsponding to the key {key} is {value}")

# Dictionary methods
# 1. update method
# update method is used to add multiple key value pairs to the dictionary
emp_performance = {20: "Good", 26: "Average", 24: "Excellent"}
emp_performance.update({22: "Poor"})
print(emp_performance)
emp_performance2 = {23: "Good", 25: "Average"}
emp_performance.update(emp_performance2)
print(emp_performance)

# 2. Pop method
# pop method is used to remove the key value pair from the dictionary
emp_performance.pop(20)
print(emp_performance)

# 3. popitem method
# popitem method is used to remove the last key value pair from the dictionary
emp_performance.popitem()
print(emp_performance)

# 4. clear method
# clear method is used to remove all the key value pairs from the dictionary
emp_performance2.clear()
print(emp_performance2)

# 5. del keyword
# del keyword is used to delete the dictionary
del emp_performance2
# print(emp_performance2) #this will give an error as emp_performance2 is deleted

# for more methods refer to the documentation of python dictionary
