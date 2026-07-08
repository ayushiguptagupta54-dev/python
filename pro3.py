#  password guessing number
import random
easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottel", "umbrella", "computer","planet"]
hard_words = ["elephant", "diamond", "computer", "mountain"]

print("Welcome to the password gussing game")
print("Choose a difficulty level: easy, hard, medium")

level = input("enter difficulty:"). lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words) 
elif level == "hard":
    secret = random.choice(hard_words)
else:
     print("Invalid choice. Defaulting to easy level")
     secret = random.choice(easy_words)

attempts = 0
print("\n Guess the secret password")

while True:
    guess = input("Enter your password: ").lower()
    attempts += 1

    if guess == secret:
        print(f'congratulations! you gussed it in {attempts} attempts.')
        break
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)
    print("Game over")


