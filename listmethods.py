#           lists methods
#           append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy
list1 = [11, 29, 13, 4, 75, 29, 29]
print(list1)

# append method
list1.append(6)  # add 6 at the end of the list
print(list1)

# sort method
list1.sort()  # ascending order
print(list1)
list1.sort(reverse=True)  # descending order
print(list1)

# reverse method
print(list1.reverse())  # reverse the list

# index method
print(list1.index(13))  # index of 13

# count method
print(list1.count(29))  # count of 29

# Reference method
# x = list1
# x[0] = 100
# print(
#     list1
# )  # list1 is also changed as x is reference to list1 so any change in x will reflect in list1
# # Thats why we use copy method to create a new list

# copy method
x = list1.copy()
x[0] = 200
print(list1)  # list1 is not changed as x is a new list
print(x)

# insert method
list1.insert(2, 100)  # insert 100 at index 2
print(list1)

n = [9, 10, 11]
# extend method
list1.extend(n)  # add n list to list1 end
print(list1)

# # merge two lists( same as extend method so commenting this code)
# k = list1 + n  # k is a new list with elements of l and m
# print(k)
