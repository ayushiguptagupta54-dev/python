# WRITE A PROGRAM TO FIND A FACTORIAL OF THE NUMBER
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter the number:"))
print("The factorial of", num, "is", factorial(num))
