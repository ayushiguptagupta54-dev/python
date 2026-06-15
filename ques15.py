#  WRITE A PROGRAM TO PRINT THE STAR PATTERNS LIKE THIS
# *
#  **
# ***
# ****
# *****

num = int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print()

