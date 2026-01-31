#  strings are immutable in python
a = "!!!!!!!!!!!!!!!!!!!!Ayushman!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("man", "i"))
print(a.rsplit("y"))
print(a.index("sh"))
print(a. count("m"))
print(a.isalnum())
print(a.isalpha())
print(a.capitalize())
print(a.endswith("n"))
print(a.find("sh"))
print(a.split("y"))
blogHanding = "ayushman_123"
print(blogHanding.capitalize())
print(blogHanding.upper())
print(blogHanding.lower())

pie = "ApplePie"
print(pie[:5])      # Slicing from Start
print(pie[5:])      # Slicing till End
print(pie[2:6])     # Slicing in between
print(pie[-8:-3])      # Slicing using negative index

alphabets = "ABCDE"
for i in alphabets:
    print(i)

str1 = "Welcome to the Console!!!"
print(str1.center(50))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "        "  # using Spacebar
print(str1.isspace())
str2 = "        "  # using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())

name = "Guzman"
age = 18
# print("My name is" + name + "and my age is" + age)

name = "Guzman"
age = 18
statement = "My name is {} and my age is {}."
print(statement.format(name, age))

quantity = 2
fruit = "Apples"
cost = 120.0
statement = "I want to buy {2} dozen {0} for {1}$"
print(statement.format(fruit, cost, quantity))






























