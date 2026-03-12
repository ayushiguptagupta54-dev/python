#  Exception handling in python
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#    for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("Errot", e)
#     print("PLease enter a valid number")

try:
    num = int(input("enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index out of bounds.")