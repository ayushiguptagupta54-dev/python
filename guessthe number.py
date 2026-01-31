import random

def guess_the_number():
    num = random.randint(1, 500)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number (1-500): "))
        attempts += 1
        
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"Yay! You guessed it in {attempts} attempts.")
            break

guess_the_number()
