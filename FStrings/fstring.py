# fstrings in Python
# fstrings are a way to format strings in Python. They are a new feature in Python 3.6. They are used for string formatting. String formatting is a way to insert a variable into a string.
# Eg:
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Dhruv"
print(letter.format(name, country))  # Hey my name is Dhruv and I am from India
print(letter.format(country, name))  # Hey my name is India and I am from Dhruv
# Above is the example of string formatting using format method. Now let's see how to do the same using fstrings
# In fstrings we use f before the string and then use {} to insert the variable like: {name}, the above example using fstrings will be:
print(
    f"Hey my name is {name} and I am from {country}"
)  # Hey my name is Dhruv and I am from India


# if using floating values in fstring method then we can use {variable:.nf} where n is the number of decimal places we want to show
# Eg:
pi = 3.14159
val = f"Value of pi is: {pi:.3f}"  # Value of pi is 3.142
print(val)

# for the same in format method:
txt = "Price is {price:.2f}"  # Price is 30.00
print(txt.format(price=29.1999))

# we can use single statemet also in fstring
print(f"{2*3}")

# to show curly braces in fstring we can use double curly braces eg:
print("We show fstringby: Hey my name is {{name}} and I am from {{country}}")
