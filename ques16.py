# WRITE A PROGRAM TO PRINT THE FOLLOWING PATTERN
# 1
# 12
# 123
# 1234
# 12345
num = int(input("Enter the numbers of rows:"))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

