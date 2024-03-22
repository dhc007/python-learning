# Greetings of the day!
import time

name = input("Enter your name: ")
timestamp = time.strftime("%H:%M:%S")
hours = int(time.strftime("%H"))
if 4 <= hours < 12:
    print("\nGood Morning ", name, "!")
elif 12 <= hours < 16:
    print("\nGood Afternoon ", name, "!")
else:
    print("\nGood Evening ", name, "!")

print("It is ", timestamp)
