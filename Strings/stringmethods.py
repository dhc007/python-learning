# String methods
a = "Dhruv"  # Stings are immutable
print(len(a))
print(a.upper())  # using upper() operation makes string uppercase
print(a.lower())


# using strip() operations
b = "   iojewljw!!!!     "
print(b.strip)
# using rstip strips only trailaing
print(b.rstrip("!"))
print(a.replace("Dhruv", "Chawla"))  # using replace function
# split function splits characters seperated by white space into seperate items of a list whatever i write inside split("here") it splits wrt that
st1 = "Hi I am Dhruv Chawla"
print(st1.split(" "))

# Capitalize help in capitalization of things properly:
st2 = "welcome to the end"
print(st2.capitalize())


# center method aligns the string to the center as per the parameters given by the user just for understanding have a look:
print(st2.center(50))
print(len(st2))
print(len(st2.center(50)))


# count returns the number of times a given valur has occured in a given string
st3 = "I am repeating the I 3 times in this string. Yes I am!"
print(st3.count("I"))

# endswith() method checks if the string ends with a given value if yes then true else false
str1 = "this ends with!!!"
print(str1.endswith("!!"))

# we can even check the value in between the string by providing the start and end index position
print(str1.endswith("en", 4, 7))

# using find() method searchs for the first occurance of the given value
print(str1.find("ends"))

print(str1.isalnum())  # isalnum checks if alphanumeric string

# can use islower() and isupper() to check if string is lower or upper
print(st2.islower())

# isprintable() checks if all characters are printable or not if we use \n it will return false
print(st2.isprintable())

# isspace() returns true only if white space anything else in string it is false
st4 = "           "
print(st4.isspace())

# istitle() returns true only if fiest letter of all words in the string are capital
print(st2.istitle())

# startswith("") checks if the string starts with the word in the string
print(st2.startswith("welcome"))

# swapcase() swaps uppercase with lower and vice versa
print(st1.swapcase())

# title() converts the string into a title that is capital first letter of every wor
print(st2.title())
