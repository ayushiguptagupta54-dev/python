# #  Global variables and local variables in python
# x = 4
# print(x)

# def hello():
#     x = 5
#     y = 4
#     print(f"The local x is {x}")
#     print("Hello ayush")

#     print(f"The global x is {x}")
#     hello()
#     x = 6
#     print(f"The global x is {x}")
   
# x = 10 
# def my_function():
#     y = 5
#     print(y)
#     my_function()
#     print(x)
#     print(y)

x = 10  # global variable


def my_function():
  global x
  y = 5  # local variable
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function