# Match Case Statements:
# Case statements are used to match a value with a list of possible values and execute the code block corresponding to the matched value.
x = int(input("Enter a number: "))
match x:
    case 1:
        print("The value of x is 1")
    case 2:
        print("The value of x is 2")
    case 3:
        print("The value of x is 3")
    case 4:
        print("The value of x is 4")
    case 5:
        print("The value of x is 5")
    case _:
        print("The value of x is not in the range 1 to 5")
