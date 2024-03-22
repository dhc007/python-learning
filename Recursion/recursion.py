"""
Recursion
Recursion is a way of programming or coding a problem, in which a function calls itself in a defined manner.
A function that calls itself is called a recursive function.
We call the function inside the funtion because we want to solve the problem in a smaller part and then combine the solution of the smaller part to get the solution of the bigger part.
The base case is the condition that stops the recursion.

Eg: for factorial of a number
factorial of 5 = 5*4*3*2*1 = 5*4*3*2*1 = 5*4!
factorial of 4 = 4*3*2*1 = 4*3!
factorial of 3 = 3*2*1 = 3*2!
factorial of 2 = 2*1 = 2*1!
factorial of 1 = 1

in general:
factorial of n = n*factorial of n-1
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter the number: "))
print(f"The factorial of {num} is: {factorial(num)}")  # using fstring
print("The factorial of", num, "is:", factorial(num))  # using comma
print("The factorial of {} is: {}".format(num, factorial(num)))  # using format method
print("The factorial of %d is: %d" % (num, factorial(num)))  # using % method


# Fibonacci series
# Fibonacci series is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
# The series is 0, 1, 1, 2, 3, 5, 8, etc.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"The fibonacci term at index {num} is {fibonacci(num)}")

"""
example:
fibonacci(7) = fibonacci(6) + fibonacci(5)=8+5=13
fibonacci(6) = fibonacci(5) + fibonacci(4)=5+3=8
fibonacci(5) = fibonacci(4) + fibonacci(3)=3+2=5
fibonacci(4) = fibonacci(3) + fibonacci(2)=2+1=3
fibonacci(3) = fibonacci(2) + fibonacci(1)=1+1=2
fibonacci(2) = fibonacci(1) + fibonacci(0)=1+0=1
fibonacci(1) = 1
"""
