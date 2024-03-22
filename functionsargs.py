# Function arguements
# 1.required arguments
# required arguments are the arguments that are required to pass in the function
def average(a, b):  # a and b are required arguments

    print("Average of the 2 numbers is: ", (a + b) / 2)


average(10, 20)  # 15.0


# 2.default arguments
# default arguments are the arguments that are already defined in the function optional to pass in the function


def average(a=10, b=20):  # a and b are default arguments
    print("Average of the 2 numbers is: ", (a + b) / 2)


average(3, 5)  # 4.0, this will give the values of a and b as 3 and 5
average()  # 15.0, this will give the default values of a and b
average(3)  # 11.5, this will give the value of a only
average(b=3)  # 6.5, giving the value of b only


# 3.variable length arguments
# variable length arguments are the arguments that are used when we don't know how many arguments are passed in the function
# *args is used to pass the variable length arguments in the function


# using lists with variable length arguments
def avg(
    *numbers,
):  # *numbers is used to pass the variable length arguments in the function
    print(type(numbers))  # <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average of the numbers is: ", sum / len(numbers))


avg(10, 20, 30, 40, 50)


# using dictionary with variable length arguments, Keyword arbitary arguments
def name(
    **name,
):  # **name is used to pass the variable length arguments in the function
    print(type(name))  # <class 'dict'>
    print("Hello, ", name["fname"], name["mname"], name["lname"])


name(mname="James", fname="Donny", lname="Barnes")


# 4.keyword arguments
# We can provide the arguments in the function with key=value,the intrepreter will recognize the arguments by their key i.e parameter name. Hence the order of the arguments does not matter
def name(fname, mname, lname):
    print("Hello, ", fname, mname, lname)


name(mname="James", fname="Donny", lname="Barnes")  # Hello,  Donny James Barnes


# using return statement in function
# return statement is used to return the value of the function to the caller of the function
def add(a, b):
    return a + b


# without return statement the function will not return any value
# if there are multiple return statements in the function then the function will return the value of the first return statement

c = add(2, 3)
print(c)  # 5
