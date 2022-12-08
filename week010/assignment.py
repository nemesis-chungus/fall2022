quiz = [
    {
        "question": "Who is the most powerful villian?",
        "choices": [
            "Darth Vader",
            "Thanos",
            "Bane",
            "The Lich",
            "The Wither"
        ],
        "answer": "The Lich"
    },
    {
        "question": "Who is the strongest hero?",
        "choices": [
            "Luke Skywalker",
            "Iron Man",
            "The Dark Knight",
            "Spider Man"
        ],
        "answer": "The Dark Knight"
    },
    {
        "question": "Who would win?",
        "choices":[
            "Luke Skywalker and Darth Vader",
            "Iron Man and Spider Man"
        ],
        "answer": "Luke Skywalker and Darth Vader"
    }
]

problemNumber = 0
correct = 0
import random
random.shuffle(quiz)
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f"  {choice}")

    guess = input("Your guess: ")
    if guess == problem['answer']:
         correct += 1
         print(f"You Are One Smart Cookie!")
    else:
         print("Better Luck Next Time.")

    print()  # print a blank line for space

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")

