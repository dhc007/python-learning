"""               lists
 1.Lists are ordered collection of items.
 2.They store multiple items in a single variable.
 3.Lists are mutable i.e. they can be changed after their creation. Unlike tuples.
 4.Lists are written with square brackets. 
 Syntax: 
           list = [item1, item2, item3, ...]
"""

# creating a list
marks = [10, 20, 30, 40, 50]
print(marks)  # [10, 20, 30, 40, 50]
print(type(marks))  # <class 'list'>

#          list index
# list index starts from 0
print(marks[0])  # 10
print(marks[1])  # 20
print(marks[2])  # 30
print(marks[3])  # 40
print(marks[4])  # 50

details = ["Dhruv", 20, "M", 7.5]  # list can store different types of data

if 10 in marks:  # checking if 10 is in the list
    print("Yes")
else:
    print("No")

# jumpindex in list
print(marks[0:3])  # [10, 20, 30]
print(
    marks[1:4:2]
)  # [20, 40], 2 is the jump index that means it will print the pl˙aces with the difference of 2

print(marks[:])  # here python will use 0 as start and len(marks) as ending

#          list comprehension
# list comprehension is a way to create lists in python
# it is a short way to create a list
# syntax:
# [expression for item in iterable]    # this is used for simple list
# [expression for item in iterable if condition]   # this is used for if condition
# [expression if condition else expression for item in iterable]  # this is used for if else condition
# [expression for item in iterable for item in iterable]   # this is used for nested loops

lst = [i for i in range(10)]  # this will create a list of numbers from 0 to 9
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = [
    i for i in range(10) if i % 2 == 0
]  # this will create a list of even numbers from 0 to 9
print(lst)  # [0, 2, 4, 6, 8]

lst = [
    i if i % 2 == 0 else "odd" for i in range(10)
]  # this will create a list of even numbers and odd string from 0 to 9
print(lst)  # [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']
