# Set is a collection of well defined objects. It is an unordered collection of unique elements. It is defined by values separated by comma inside braces { }.
# Sets are used to perform mathematical set operations like union, intersection, symmetric difference etc.
# Sets are used to eliminate duplicate entries from a list or tuple.
# Sets are mutable i.e. we can add or remove elements from it. but we cannot change the elements of a set.
# Sets are unindexed i.e. we cannot access elements using index.
# We use set to remove duplicate elements from a list or tuple
# Eg:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List with duplicate elements: ", list1)
list2 = list(set(list1))
print("List without duplicate elements: ", list2)

info = {"Dhruv", 20, "India", "Dhruv"}
print(info)

s = {2, 3, 2, 6}
print(s)

s1 = {}
print(
    type(s1)
)  # <class 'dict'> as it is empty dictionary not set so to create empty set we use set() method
s2 = set()
print(type(s2))  # <class 'set'> as it is empty set


# using for loop to print the elements of set
for i in info:
    print(i)


#                       Set methods
# Methods to manupulate the set
# 1. Union() & Update() in set
# Eg1:
set1 = {1, 2, 5, 6}
set2 = {3, 6, 7}
print(
    set1.union(set2)
)  # union is a method to combine two sets and remove the duplicate elements
print(set1 | set2)  # | is also used for union
# In the above set1 and set2 are untouched
print(set1)
print(set2)
# To update the set1 with the union of set1 and set2 we use update method
set1.update(set2)
print(set1, set2)  # set1 is updated with the union of set1 and set2


# Eg2:
cities = {"Delhi", "Mumbai", "Kolkata", "Berlin", "Tokyo"}
cities2 = {"Chennai", "Banglore", "Delhi", "Mumbai", "Tokyo"}
cities3 = cities.union(cities2)
print(cities3)

cities.update(cities2)
print(cities)

# 2. Intersection() and intersection_update() in set:
cities4 = {"Delhi", "Mumbai", "Kolkata", "Berlin", "Tokyo"}
cities5 = {"Chennai", "Banglore", "Delhi", "Mumbai", "Tokyo"}
cities6 = cities4.intersection(
    cities5
)  # returns the common elements in cities and cities2
print(cities6)

cities4.intersection_update(cities5)
print(cities4)  # cities4 is updated with the common elements of cities4 and cities5


# 3. Symmetric_difference() and symmetric_difference_update() in set:
# symmetric_difference() returns the elements that are not common in both the sets
# symmetric_difference_update() updates the set with the elements that are not common in both the sets
cities7 = {"Delhi", "Mumbai", "Kolkata", "Berlin", "Tokyo"}
cities8 = {"Chennai", "Banglore", "Delhi", "Mumbai", "Tokyo"}
cities9 = cities7.symmetric_difference(
    cities8
)  # elements in cities7 and cities8 that are not common
print(cities9)
cities7.symmetric_difference_update(cities8)
print(
    cities7
)  # cities7 is updated with the elements that are not common in cities7 and cities8
# if we do cities8.symmetric_difference_update(cities7) then cities8 will be updated with the elements that are not common in cities7 and cities8


# 4. isdisjoint() in set:
# isdisjoint() returns True if the sets have no common elements
# Eg:
set3 = {1, 2, 3, 4, 5}
set4 = {6, 7, 8, 9, 10}
print(set3.isdisjoint(set4))  # True as set3 and set4 have no common elements
set5 = {1, 2, 3, 4, 5}
set6 = {5, 6, 7, 8, 9}
print(set5.isdisjoint(set6))  # False as set5 and set6 have common element 5

# 5. issubset() and issuperset() in set:
# issubset() returns True if all the elements of the set are present in the other set
# issuperset() returns True if all the elements of the other set are present in the set
# Eg:
set7 = {1, 2, 3, 4, 5}
set8 = {1, 2, 3}
print(set8.issubset(set7))  # True as all the elements of set8 are present in set7
print(set7.issuperset(set8))  # True as all the elements of set8 are present in set7


# 6. add() and update() in set:
# add() is used to add a single element in the set
# remove() is used to remove a single element from the set
# Eg:
set9 = {1, 2, 3, 4, 5}
set9.add(6)
print(set9)
set9.update({7, 8, 9})
# 7. remove() and discard() in set:
# remove() is used to remove a single element from the set
# discard() is used to remove a single element from the set
# difference between remove and discard is that if the element is not present in the set then remove will give an error and discard will not give an error
# Eg:
set9.remove(6)
print(set9)
set9.discard(7)
print(set9)

# 8. pop()
# pop() is used to remove the last element from the set but as the set is unindexed so we cannot say which element will be removed
# Eg:
cities10 = {"Delhi", "Mumbai", "Kolkata", "Berlin", "Tokyo"}
print(cities10.pop())

# 9.del and clear in set:
# del is used to delete the set
# clear is used to remove all the elements from the set
# Eg:
cities10.clear()
print(cities10)
del cities10
# print(cities10)  # error as cities10 is deleted
