# CREATE A SIMPLE CALCULATOR USING FUNCTIONS
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
if num1 + num2:
    print("Addition", num1 + num2)
if num1 - num2:
    print("Subtraction", num1- num2)
if num1 * num2:
    print("Multiplication", num1 * num2) 
if num1 / num2:
    print("Division", num1 / num2) 
else:
    print("The number does'not exist")

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Choose operation (1-4): ")

# if choice == "1":
#     print("Result:", add(num1, num2))
# elif choice == "2":
#     print("Result:", subtract(num1, num2))
# elif choice == "3":
#     print("Result:", multiply(num1, num2))
# elif choice == "4":
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid choice")

