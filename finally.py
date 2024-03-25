#                              Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# finally clause is also a parrt of exception handling. It is used to execute a block of code whether an exception is thrown or not. It is generally used to release external resources like file handling, database connections, etc.
# this is used for clean ups where in whatever condition the code is, the finally block will always be executed.

try:
    l = [1, 2, 3]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("Finally block is executed1")


# Finally block used rather than just exexcting a function outside the try block. the most important use is to return a value from a function.
# Example:
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 0
#     finally:
#         print("Finally block is executed2")


# x = divide(4, 0)
# print(x)

# In the above example, the finally block is executed after the return statement. It is used to clean up the resources. It is generally used to release external resources like file handling, database connections, etc.


def func1():
    try:
        a = [1, 2, 3]
        b = int(input("Enter the index: "))
        print(a[b])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("Finally block is executed2")


x = func1()
print(x)
# In the above example, the finally block is executed after the return statement. It is used to clean up the resources. It is generally used to release external resources like file handling, database connections, etc.
