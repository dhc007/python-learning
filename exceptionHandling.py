# Exception Handling or Error Handling
# We get errors when we run the code this could be due to many reasons like wrong input, wrong logic, etc. To handle these errors we use exception handling.
# try: block of code that may raise an exception
# except: block of code that will be executed if an exception occurs

# Example 1: code giving invalid input error
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is:")

# for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# #if you enter a string instead of a number, the program will crash. To handle this we use exception handling. if it encounters an error it will not run any further code and will execute the except block.
# print("Consider these to be Some important lines of code")
# print("End of the program")

# Example 1 with exception handling
a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except (
    Exception
) as e:  # Exception is a base class for all exceptions. It will catch all types of exceptions. You can also specify the type of exception you want to catch.
    print(e)  # prints the error message
print("Consider these to be Some important lines of code")
print("End of the program")


# except vs except Exception as e
# except: will catch all types of exceptions
# except Exception as e: will catch all types of exceptions and store the error message in e. You can print this message to know what went wrong.

# Example 2: code giving ZeroDivisionError
a = 4
b = 0
try:
    print(a / b)
except:
    print("Cannot divide by zero")

# specific error handling could be value error, index error, etc. You can specify the type of error you want to catch. you can also catch multiple errors by using except:

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index out of range")
except Exception as e:
    print(e)
