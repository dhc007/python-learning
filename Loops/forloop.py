# using for loop to not repeat the code
# printing characters of a string
name = "Dhruv"
for i in name:
    print(i)
# nesting for inside for loop on a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)
# using range functions in for loop
# printing numbers from 0 to 10
print("\n")
for num in range(10):  # using range function with one argument makes it start from 0
    print(num + 1)
print("\n")
# using start and end in range function
for k in range(1, 10):  # this will print numbers from 1 to 9 won't include 10
    print(k)

# running range function with step
print("\n")
for l in range(0, 10, 2):  # this will print numbers from 1 to 9 with step of 2
    print(l)
# step means the difference between two numbers
