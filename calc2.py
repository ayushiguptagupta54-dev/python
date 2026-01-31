print("1-ADD")
print("2-SUBTRACT")
print("3-MULTIPLY")
print("4-DIVIDE")
option= int(input("Enter your choice:  " ))
if(option in [1,2,3,4]):
    result = 0
else:
    print("Invalid operion entered")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:  "))


if(option == 1):
  result = num1 + num2
elif(option == 2):
  result = num1 - num2
elif(option == 3):
 result = num1 * num2
elif(option == 4):
 result = num1 / num2

print("result is  {}".format(result))