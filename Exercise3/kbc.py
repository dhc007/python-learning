# Create a program capable of of displaying question to the use like KBC.
# Use list data type to store the questions and the correct answers.
# Display the final amount won by the user.
questions = [
    "Who is the father of our Nation",
    "What is the capital of Goa",
    "Who is the ruling party of India in 2023",
    "Who is George Clooney",
]
options = [
    ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Lal Bhadur Shastri"],
    ["Margao", "Vasco", "Panji", "Mapusa"],
    ["Congress", "AAP", "RJD", "BJP"],
    ["Politician", "Actor", "Singer", "Dancer"],
]
answers = [0, 2, 3, 1]
amount = [10000, 50000, 200000, 10000000]
i = 0
j = 0
total = 0
name = input("Enter your name: ")
print("\n\n\t\tWelcome to the show Kaun Banega Crorepati\n")
print(
    name,
    "ji You will be asked",
    len(questions),
    "questions and you can win upto 1 crore.\n",
)
print("All the best!\n")
while i < len(questions):
    print("Q", i + 1, ":", questions[i])
    for j in range(len(options[i])):
        print("\t", j + 1, ":", options[i][j])
    ans = int(input("\nEnter your answer(1,2,3,4): "))
    if ans == answers[i] + 1:
        print("\nCongratulations", name, "! You have won", amount[i], "Rupees.\n\a")
        total = amount[i]
        i += 1
        if i != len(questions):
            print("Next question for you is:\n")
    else:
        print(
            "Sorry ",
            name,
            "!, That was the wrong answer and you have won",
            total,
            "Rupees.\n",
        )
        break
