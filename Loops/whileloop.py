# while loops in python
# while loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in program is executed.

# In the below example, the value of i is 0 and the condition is i<=5, so the loop will run until the value of i is less than or equal to 5. The value of i is incremented by 1 in each iteration. The loop will run 6 times and print the value of i from 0 to 5.

i = 0
while i <= 5:
    print(i)
    i += 1  # i=i+1
print("End of while loop\n")

# In the below example user can enter any number and the loop will run until the user enters 0
num = int(input("Enter a number: "))
while num != 0:
    print(num)
    num = int(input("Enter a number: "))
print("End of while loop\n")

# decrementing while loop
num = 5
while num > 0:
    print(num)
    num -= 1  # num=num-1
print("\n")

# using while loop with else
i=5
while i>0:
    print(i)
    i=i-1
else:
    print("numbeer is 0")
