# Docstrings and PEP-8
# Docstrings are string literals that appear right after defination of a fucntion, method, class or module
# Eg:
def square(n):
    # docstring has to be right below the fucntion name/right above the function body
    """This function takes in a number n and returns the square of the number"""
    print(n**2)


square(5)
print(square.__doc__)  # function name.__doc__ will print the docstring of the function

"""
Comments vs Docstrings
Comments are used to explain the code and are for the developers to understand the code. They are not used by the interpreter.
Docstrings are used document and are can access them using the __doc__ attribute of the object.

PEP-8 Python Enhancement Proposal
PEP-8 is a style guide for Python code. It is a set of rules for writing code in Python. It is a good practice to follow PEP-8 guidelines when writing code in Python.

"""

print("\n")
import this

"""

Zen of Python

If i go to the compiler and type: "import this" then it will show the Zen of Python which is a collection of 19 aphorisms that capture the guiding principles of Python's design. It is written by Tim Peters. It is a set of guiding principles for writing computer programs that influence the design of the Python programming language. It is written as a poem and is a good read for any Python programmer.


The Zen of Python, by Tim Peters using import this:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""
