# else is not limited to be used only by if statement. It can also be used with for loop.

for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
else:
    print("For loop is completed")

# for else loop is used to execute a block of code when the loop is finished. The else block will not be executed if the loop is terminated by a break statement.
# Eg:
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
    if i == 2:
        break
else:
    print("For loop is completed")

# you can also use else block with while loop.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("While loop is completed")

# while with break
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1
else:
    print("While loop is completed")
