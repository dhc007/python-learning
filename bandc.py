# break and continue statement
# break -> skip the loop and exit
# continue -> skip the iteration

# printing tables but putting break after the first print
for i in range(12):
    print("5 X", i + 1, "=", 5 * (i + 1))
    if i == 10:
        break  # this will still excecute i==10
print("left the loop")


# placing the break condition before the printing:
for i in range(12):
    if i == 10:
        break  # this will break before entering the print statement
    print("5 X", i + 1, "=", 5 * (i + 1))
print("left the loop")

# using continue:
for i in range(12):
    print("5 X", i + 1, "=", 5 * (i + 1))
    if i == 10:
        continue  # this will still excecute i==10
print("left the loop")


for i in range(12):
    if i == 10:
        break
    print("5 X", i + 1, "=", 5 * (i + 1))
print("left the loop")

# using continue to skip the iteration wherethe number is divisible by 5
for i in range(21):
    if i % 5 == 0:
        print("is divisible by 5")
        continue
    print(i)
print("left the loop")
# the for loop is running till i=20, but range is 21, so it runs till 20 and then exit


# to emulate do while loop in python
i = 0
while True:
    print(i)
    i += 1
    if i % 5:
        break
print("left the loop")
# the code above is emting the do while loop in python
# the loop will run till i=4 and then exit
# it runs before checking the condition
