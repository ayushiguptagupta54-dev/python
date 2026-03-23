#  Short hand if else statement
a = 330
b = 3303
print("A" if a > b else "B")

a = 33
b = 54
print("A" if a > b else "=" if a == b else "B")

c = 10 if a > b else 0
print(c)

a = 330000
b = 330
print("A") if a > b else print("B") if a == b else print("B")

c = 9 if a>b else 0
print(c)
