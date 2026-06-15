# CREATE A QUIZ GAME WITH SCORE TRACKING
score = 0

questions = {
    "What is the capital of India?": "Delhi",
    "Which language is use for AI and data science?" : "Python",
    "How many continents are there?": "7"
}

for questions, answer in questions.items():
    user_answer = input(questions)

    if user_answer.lower() == answer.lower():
        print("Correct!")
    else:
            print("Wrong!")

print("\nQuiz finished")
print("Your score:", score, "/", len(questions))
