#strings and string methods
name1="Dhruv" #anything inside a single or double quote is a string. it is a sequence of array/text data
name2="krish"
print(name1,name2)
sentence1="He said, \"I wanted to go out\"" #you cannot put a double quote inside a double quote string directly you must use a blackslash before the doublequote or put the string in single quotes:
sentence2='He said, "I wanted to go out"'
print(sentence1)
print(sentence2)
#for a multiple line string you need to wrap the string in triple single or triple double quotes
sentence3= """Hi Harry,
How are you?
I am good!"""
print(sentence3)

#accesing a particular element of the string using indexing
print(name1[0])
#print(name1[5]) #this gives an error because last charcater is at position 4
print(name1[4]) #accesing the last letter from front since count begins from 0 the last is 4 not 5
print(name1[-1])#accesing the last letter from back by using -1

#printing all characters in the string by looping through the string using for loop
print("\nprinting name1 using for loop:\n")
for character in name1:
    print(character)
