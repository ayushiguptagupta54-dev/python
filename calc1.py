# Make a simple calculator in python
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
option= int(input("Enter your choice:  " ))
if(option in [1,2,3,4]):
    result = 0
else:
    print("Invalid operion entered")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:  "))


if(option == 1):
  result = num1 + num2
elif(option == 2):
  result = num1 - num2
elif(option == 3):
 result = num1 * num2
elif(option == 4):
 result = num1 // num2

print("result is  {}".format(result))