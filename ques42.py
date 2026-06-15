# # CREATE A SIMPLE ATM PROGRAM
# balance = 100000

# while True:
#     print("\n==== ATM MEanu =====")
#     print("1. Check balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

#     choice = input("Enter your chocie:")

# if choice == '1':
#         print("Curent balnce:", balance)

# elif choice == "2":
#             amount = float(inpit("Enter deposit amount:"))
#             balance += amount
#             print("Amount Deposited succesfully")


# elif choice == "3":
#         amount = float(input("Enter withdrawal amount:"))

# if amount <= balance:
#             balance -= amount
#             print("Withdrawal sucessfully")
# else:
#         print("Insufficent balance")

# elif choice == "4":
#         print("Thank you!")
#         break

#     else:
#             print("Invalid choice")


balance = 10000

while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
