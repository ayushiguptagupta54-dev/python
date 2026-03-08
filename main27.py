# create a program capable of displaying questions to the user like KBC. 
# use list data type to store the questions and their correct answers.
# Dsiplay the final amount the person is taking home agter palying the game.

# #  KBC Game
# list 1 = {
#     "What is the capital of india?" : "New Delhi"
# }
list 2 = {
    "Who is the first prime minister of India?" : "Jawaharlal Nehru"
}
list 3 = {
    "What is the national animal of India?" : "Tiger"
}
list 4 = {
    "What is the national bird of India?" : "Peacock"
}
list 5 = {
    "What is the naional flower of India?" : "Lotus"
}
questions = {list 1, list 2, list 3, list 4, list 5}
answers = {"New Delhi", "Jawaharlal Nehru", "Tiger", "Peacock", "Lotus"}
amount = 0
for question in questions:
    print(question)
    user = input("Enter your answer:")
    if user in answers:
        amount =+ 1000
        print("Correct! You have won Rs.", amount)
        else:
            print("Wrong answer! You have won Rs.", amount)
            break
