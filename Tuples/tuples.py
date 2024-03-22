#             Tuples
# Tuples are similar to lists, but they are immutable, meaning that the values inside a tuple cannot be changed. Also, tuples are written within parentheses.
tup = (1, 5, 6)
print(type(tup), tup)
tup2 = 1
print(type(tup2), tup2)  # type int as there is no comma it should be (1,)
# tup[0] = 100  # error as tuples are immutable
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[0:2])  # slicing
print(tup[0:3:2])  # slicing with step
print(tup[-1])  # negative indexing

if 1 in tup:
    print("yes")  # check if 1 is in tuple


#             tuples methods
# you can not change the value of tuple directly but you can change the value of tuple by converting it into list this is to add remove or change the value of tuple and then convert it back to tuple. Example is below:
countries = ("Spain", "France", "India", "Italy", "Sri Lanka")
temp = list(countries)
temp.append("Russia")  # add
temp.pop(3)  # remove
temp[2] = "Japan"  # change
countries = tuple(temp)
print(countries)

# We can concatenate tuples without converting them to list
countries2 = ("Pakistan", "China", "India")
countries3 = countries + countries2
print(countries3)

# The methods that can be used directly in the tuple:
tuple1 = (2, 0, 0, 4, 2, 1, 5, 7, 2, 9, 2, 8)

# 1.count
count2 = tuple1.count(2)  # 4
print("the count of 2 in tuple 1 is :", count2)

# 2.index
index4 = tuple1.index(4)
index2 = tuple1.index(
    2, 5, 11
)  # this check for occurance of 2 betweem 5th and 11th position
print(index4)  # 3
print(index2)  # 8

# 3.len
length = len(tuple1)
print(length)
