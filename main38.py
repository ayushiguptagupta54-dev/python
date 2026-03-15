# #  Raise error
# a = int(input("Enter any value between 5 to 9: "))
# if a < 5 or a > 9:
#     raise ValueError("value should be between 5 and 9")

a = input("Enter 'quit' to exit: ")
if (a== "quit"):
    print("Program execute successfully")
else:
    raise ValueError ("Value should be other than that")

