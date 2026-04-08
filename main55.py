# Game of snake water and gun
            # s w g
# computer =  0 1 2
# player = s 0 d w l
#          w 1 l d w
#          g 2 w l d    
# import random
print("Welcome to the game of snake water and gun!")
print("You have to chances to play the game.")
print("Enter your choice:")
# print("1. Snake")
# print("2. Water")
# print("3. Gun")
choice = ["Snake","Water", "Gun"]
for i in range(2):
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        user_choice = "Snake"
    elif user_input == 2:
            user_choice = "Water"
    elif user_input == 3:
                user_choice = "Gun"
    else:
        print("Invalid input! Please enter a valid choice: 1,2,3")
        # computer_choice = random.choice(choice)
        # print(f"Computer choice: {computer_choice}")
