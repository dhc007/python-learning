# using functions in python
# function is a block of code runs when it is called
# you can make a function to do a specific task
# we create a funftion and can use it multiple times


# defining a function
def HW():
    print("Hello World")


# calling a function
HW()


# function with arguments
def add(a, b):
    print(a + b)


# calling a function with arguments
add(2, 3)


# funtion for which number is greater
def greater(a, b):
    if a > b:
        print(a, "is greater")
    elif a == b:
        print("both are same")
    else:
        print(b, "is greater")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
greater(num1, num2)


# function without body
def fun():
    pass  # pass is a keyword in python which is used when you don't want to execute any code


# if pass is not used then it will give an error

# user defined functions are also funtions that user first define and then use it multiple times
# inbuilt functions are already defined in python e.g print(), input(), int(), str(), float(), etc
