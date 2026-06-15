# WRITE A PROGRAM TO PRINT A MULTIPLICATION TABLE OF THE NUMBER ENTERED BY THE USER
num = int(input("Enter a number:"))
print("The multiplication table of", num, "is:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    